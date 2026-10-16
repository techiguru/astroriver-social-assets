# Navratri 2026: our own subtle background music (founder 12 Oct: the flute "isn't cutting it"; it "has to be subtle").
# A synthesised tanpura drone (Pa, Sa, Sa, low Sa, plucked in a slow cycle) and, optionally, a soft temple bell
# struck as her name appears and as the end card comes in. Made here from scratch, so no licence questions.
# Usage: python3 navratri_music.py <out.wav> <seconds> [bell times, comma-separated]
import sys, wave, numpy as np
SR = 44100

def pluck(freq, dur, decay=0.9993, bright=0.5, seed=0):
    # Karplus-Strong string with a long ring, then a light jawari-like buzz from a soft clip
    rng = np.random.default_rng(seed); n = int(SR / freq)
    buf = rng.uniform(-1, 1, n); out = np.zeros(int(SR * dur))
    for i in range(len(out)):
        j = i % n; prev = buf[j - 1]
        out[i] = buf[j]; buf[j] = decay * (bright * buf[j] + (1 - bright) * prev)
    return np.tanh(2.2 * out) * 0.5

def bell(dur, base=528.0):
    t = np.arange(int(SR * dur)) / SR; out = np.zeros_like(t)
    for r, a, d in [(1, 1, 3.2), (2.0, .55, 2.2), (2.76, .4, 1.6), (4.07, .22, 1.1), (5.4, .12, .8)]:
        out += a * np.sin(2 * np.pi * base * r * t) * np.exp(-t / d)
    return out * np.minimum(1, t * 400) / 2.3

def main(path, secs, bells):
    total = np.zeros(int(SR * (secs + 4)))
    sa = float(__import__("os").environ.get("SA", "138.59"))  # C#3 by default; SA=277.18 for C#4 (phone speakers)
    notes = [sa * 3 / 4, sa, sa, sa / 2]  # Pa (below), Sa, Sa, low Sa
    step, k, t = 0.62, 0, 0.0
    while t < secs:
        f = notes[k % 4]; s = pluck(f, 3.5, seed=k); i = int(t * SR)
        total[i:i + len(s)] += s[:len(total) - i] * (0.9 if k % 4 == 3 else 0.7)
        t += step + (0.5 if k % 4 == 3 else 0); k += 1
    for b in bells:
        s = bell(4.0); i = int(b * SR); total[i:i + len(s)] += s[:len(total) - i] * 0.35
    total = total[:int(SR * secs)]
    total /= np.max(np.abs(total)) + 1e-9; total *= 0.8
    pcm = (total * 32767).astype(np.int16)
    with wave.open(path, 'wb') as w:
        w.setnchannels(1); w.setsampwidth(2); w.setframerate(SR); w.writeframes(pcm.tobytes())

if __name__ == '__main__':
    bells = [float(x) for x in sys.argv[3].split(',')] if len(sys.argv) > 3 and sys.argv[3] else []
    main(sys.argv[1], float(sys.argv[2]), bells)
