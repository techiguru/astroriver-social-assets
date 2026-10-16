# Navratri 2026, Day 5: the Reels rebuilt on the founder's moving clip (15 Oct, "Final"). The founder made the clip in
# Grok from our clean picture: she smiles and looks down at the baby, Skanda waves (crown, vibhuti and vel kept), the
# lion blinks and stays facing us. Here: the Grok mark in the corner is filled from its surroundings, the 720p clip is
# enlarged to 1080 x 1920, played forward then backward so it loops smoothly, and the same text layer as
# navratri_day5.py (name, shloka, meaning, end card) is laid over it.
# Usage: python3 navratri_day5_video.py <clip.mp4> <absolute outdir>
import os, sys, asyncio, subprocess
import numpy as np, cv2
from playwright.async_api import async_playwright
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
import navratri_day5 as P
W, H, FPS = 1080, 1920, 24
MARK = (646, 1242, 710, 1268)          # the Grok mark in the 720 x 1280 clip (x0, y0, x1, y1)


def base(clip, out):
    """The clip with the mark filled in, enlarged to 1080 x 1920 (lossless intermediate)."""
    probe = subprocess.run(['ffprobe', '-v', 'error', '-select_streams', 'v:0', '-show_entries', 'stream=width,height',
                            '-of', 'csv=p=0', clip], capture_output=True, text=True).stdout.strip().split(',')
    w, h = int(probe[0]), int(probe[1])
    dec = subprocess.Popen(['ffmpeg', '-v', 'error', '-i', clip, '-f', 'rawvideo', '-pix_fmt', 'bgr24', '-'], stdout=subprocess.PIPE)
    enc = subprocess.Popen(['ffmpeg', '-v', 'error', '-y', '-f', 'rawvideo', '-pix_fmt', 'bgr24', '-s', f'{W}x{H}', '-r', str(FPS), '-i', '-',
                            '-c:v', 'libx264', '-crf', '8', '-preset', 'medium', '-pix_fmt', 'yuv444p', out], stdin=subprocess.PIPE)
    x0, y0, x1, y1 = MARK; mask = np.zeros((h, w), np.uint8); mask[y0:y1, x0:x1] = 1
    n = 0
    while True:
        buf = dec.stdout.read(w * h * 3)
        if len(buf) < w * h * 3: break
        f = np.frombuffer(buf, np.uint8).reshape(h, w, 3).copy()
        f = cv2.inpaint(f, mask, 5, cv2.INPAINT_TELEA)
        big = cv2.resize(f, (W, H), interpolation=cv2.INTER_LANCZOS4)
        blur = cv2.GaussianBlur(big, (0, 0), 1.4)
        big = cv2.addWeighted(big, 1.45, blur, -0.45, 0)                    # gentle sharpening after enlarging
        enc.stdin.write(big.tobytes()); n += 1
    enc.stdin.close(); enc.wait(); dec.wait()
    return n


def pingpong(src, out, dur):
    # forward, then backward (she looks back up, the baby's hand comes down), then hold the first frame
    subprocess.run(['ffmpeg', '-v', 'error', '-y', '-i', src, '-filter_complex',
                    f'[0:v]split[a][b];[b]reverse[r];[a][r]concat=n=2:v=1,tpad=stop_mode=clone:stop_duration=3,trim=0:{dur},setpts=PTS-STARTPTS[v]',
                    '-map', '[v]', '-c:v', 'libx264', '-crf', '8', '-preset', 'medium', '-pix_fmt', 'yuv444p', out], check=True)


OVERLAY_CSS = 'html,body{background:transparent!important} .cam{display:none!important}'


async def render(clip, out):
    work = os.path.join(out, '_d5v'); os.makedirs(work, exist_ok=True)
    fwd = os.path.join(work, 'forward.mp4'); n = base(clip, fwd); print('frames', n)
    async with async_playwright() as p:
        b = await p.chromium.launch(); pg = await b.new_page(viewport={'width': W, 'height': H})
        for mode in ('full', 'short'):
            D = P.T[mode]['dur']; tag = 'reel' if mode == 'full' else 'short-8s'
            bg = os.path.join(work, f'bg-{tag}.mp4'); pingpong(fwd, bg, D)
            fn = os.path.join(out, f'navratri-day5-skandamata-video-{tag}.html'); open(fn, 'w').write(P.page(mode))
            await pg.goto('file://' + fn); await pg.evaluate('document.fonts.ready'); await pg.evaluate('window.ready')
            await pg.add_style_tag(content=OVERLAY_CSS); await pg.wait_for_timeout(800)
            await pg.evaluate('document.getAnimations().forEach(a=>a.pause())')
            mp4 = os.path.join(out, f'navratri-day5-skandamata-video-{tag}.mp4')
            ff = subprocess.Popen(['ffmpeg', '-v', 'error', '-y', '-i', bg, '-f', 'image2pipe', '-framerate', str(FPS), '-c:v', 'png', '-i', '-',
                                   '-filter_complex', '[0:v][1:v]overlay=0:0:format=auto,format=yuv420p[v]', '-map', '[v]',
                                   '-c:v', 'libx264', '-crf', '16', '-preset', 'slow', '-movflags', '+faststart', '-t', str(D), mp4],
                                  stdin=subprocess.PIPE)
            for i in range(int(D * FPS)):
                t = i / FPS
                await pg.evaluate(f'document.getAnimations().forEach(a=>{{a.currentTime={t*1000}}})')
                ff.stdin.write(await pg.screenshot(type='png', omit_background=True))
            ff.stdin.close(); ff.wait()
            print('done', mp4)
        await b.close()

if __name__ == '__main__':
    asyncio.run(render(sys.argv[1], sys.argv[2]))
