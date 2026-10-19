# Navratri 2026: our own soft bhajan-style background music (founder 18 Oct: "I don't have music. Can you add a soft
# beautiful music that sounds like a Devi Bhajan"). Made here from scratch, so no licence questions: a tanpura drone,
# a soft harmonium playing an original slow melody in the Bhairavi mood (komal Re Ga Dha Ni, the colour of many Devi
# bhajans; a first try in Bhupali rising Sa Re Ga sounded like the national anthem), with small glides between notes, a temple bell at the start, and from the second line a gentle dholak and
# manjira in an eight-beat keherwa. The first line (0 to 6.4 s) and the second (6.4 to 12.8 s) come back to Sa, so the
# 13 s Reel ends at rest; 8 s versions fade out inside the second line.
# Usage: python3 navratri_bhajan_music.py <out.wav> [seconds, default 26]
import sys, wave, numpy as np
from navratri_music import pluck, bell
SR = 44100
SA = 293.66                                  # D4: the harmonium's Sa; the drone sits an octave below
BEAT = 0.8                                   # 75 beats a minute, eight beats a line
SW = {'S': 0, 'r': 1, 'g': 3, 'm': 5, 'P': 7, 'd': 8, 'n': 10, "S'": 12, '.n': -2, '.d': -4, '.P': -5}
# each line is eight beats; '-' holds the note before
LINES = [
    "P - d n S' - n d",
    "P m g m g r S -",
    ".n S r g m - P -",
    "d P m g r - S -",
]


def hz(sw):
    return SA * 2 ** (SW[sw] / 12)


def harmonium(freqs, amp):
    """A two-reed harmonium voice following a per-sample frequency curve, with a little bellows swell."""
    ph1 = 2 * np.pi * np.cumsum(freqs) / SR; ph2 = 2 * np.pi * np.cumsum(freqs * 1.0035) / SR
    out = np.zeros_like(freqs)
    for n in range(1, 12):
        a = (1 / n) * (0.6 if n % 2 == 0 else 1.0) * np.exp(-n / 9)
        out += a * (np.sin(n * ph1) + 0.8 * np.sin(n * ph2 + 0.3 * n))
    t = np.arange(len(freqs)) / SR
    return out * amp * (1 + 0.04 * np.sin(2 * np.pi * 0.35 * t))


def melody(secs):
    n = int(SR * secs); f = np.full(n, SA); amp = np.zeros(n)
    notes = []                                                       # (start, length in beats, swara)
    for li, line in enumerate(LINES * 4):
        b0 = li * 8
        for bi, tok in enumerate(line.split()):
            if tok == '-': notes[-1][1] += 1
            else: notes.append([b0 + bi, 1, tok])
    for k, (b, L, s) in enumerate(notes):
        i0, i1 = int(b * BEAT * SR), int((b + L) * BEAT * SR)
        if i0 >= n: break
        i1 = min(i1, n); f[i0:i1] = hz(s)
        g = int(0.09 * SR)                                           # a short glide (meend) into the next note
        if k + 1 < len(notes) and i1 - g > i0 and i1 < n:
            f[i1 - g:i1] = np.geomspace(hz(s), hz(notes[k + 1][2]), g)
        e = np.ones(i1 - i0); a = min(int(0.07 * SR), len(e)); e[:a] = np.linspace(0, 1, a)
        r = min(int(0.12 * SR), len(e)); e[-r:] *= np.linspace(1, 0.55, r)  # the bellows never fully stop
        amp[i0:i1] = e * (1.0 if L == 1 else 0.95)
    amp = np.convolve(amp, np.ones(400) / 400, 'same')
    return harmonium(f, amp)


def drone(secs):
    out = np.zeros(int(SR * (secs + 4))); low = SA / 2; notes = [low * 3 / 4, low, low, low / 2]
    t, k = 0.0, 0
    while t < secs:
        s = pluck(notes[k % 4], 3.5, seed=k); i = int(t * SR)
        out[i:i + len(s)] += s[:len(out) - i] * (0.9 if k % 4 == 3 else 0.7)
        t += 0.62 + (0.5 if k % 4 == 3 else 0); k += 1
    return out[:int(SR * secs)]


def dholak(kind):
    t = np.arange(int(SR * 0.6)) / SR
    if kind == 'dha':                                                # low, round, with a small pitch drop
        f = 95 + 60 * np.exp(-t / 0.03); ph = 2 * np.pi * np.cumsum(f) / SR
        return np.sin(ph) * np.exp(-t / 0.22) + 0.25 * np.sin(2 * np.pi * 380 * t) * np.exp(-t / 0.05)
    return 0.55 * np.sin(2 * np.pi * 420 * t) * np.exp(-t / 0.06) * (1 + 0.3 * np.random.default_rng(1).standard_normal(len(t)) * np.exp(-t / 0.01))


def manjira():
    t = np.arange(int(SR * 0.9)) / SR; out = np.zeros_like(t)
    for fr, a in [(2960, 1), (4170, .7), (5230, .5), (6810, .35)]:
        out += a * np.sin(2 * np.pi * fr * t)
    return out * np.exp(-t / 0.35) * np.minimum(1, t * 3000) / 2.5


def percussion(secs):
    out = np.zeros(int(SR * (secs + 1)))
    pattern = ['dha', 'na', 'na', 'dha', 'dha', 'na', 'na', None]     # a soft keherwa
    b = 8                                                            # starts with the second line
    while b * BEAT < secs:
        i = int(b * BEAT * SR); p = pattern[b % 8]
        if p: s = dholak(p) * (0.8 if p == 'dha' else 0.45); out[i:i + len(s)] += s[:len(out) - i]
        if b % 4 == 0: s = manjira(); out[i:i + len(s)] += s[:len(out) - i] * 0.5
        b += 1
    return out[:int(SR * secs)]


def reverb(x, secs=2.2, seed=0):
    rng = np.random.default_rng(seed); t = np.arange(int(SR * secs)) / SR
    ir = rng.standard_normal(len(t)) * np.exp(-t / (secs / 6.9)); ir[0] = 0
    ir = np.convolve(ir, np.ones(8) / 8, 'same'); ir /= np.sqrt(np.sum(ir ** 2))
    n = len(x) + len(ir); F = 1 << (n - 1).bit_length()
    return np.fft.irfft(np.fft.rfft(x, F) * np.fft.rfft(ir, F), F)[:len(x)]


def main(path, secs):
    mel = melody(secs); dr = drone(secs); pc = percussion(secs)
    b = bell(4.0); bl = np.zeros_like(mel); bl[:len(b)] += b[:len(bl)]
    dry = 0.55 * mel / np.max(np.abs(mel)) + 0.35 * dr / np.max(np.abs(dr)) + 0.35 * pc / (np.max(np.abs(pc)) + 1e-9) + 0.3 * bl
    L = dry + 0.35 * reverb(dry, seed=1); R = dry + 0.35 * reverb(dry, seed=2)
    st = np.stack([L, R], 1); st /= np.max(np.abs(st)); st *= 0.85
    with wave.open(path, 'wb') as w:
        w.setnchannels(2); w.setsampwidth(2); w.setframerate(SR); w.writeframes((st * 32767).astype(np.int16).tobytes())


if __name__ == '__main__':
    main(sys.argv[1], float(sys.argv[2]) if len(sys.argv) > 2 else 26.0)
