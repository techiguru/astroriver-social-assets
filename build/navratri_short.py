# Navratri 2026: the short Reel (founder 12 Oct: "with music only 7 to 8 secs reel"). Same page as navratri_photo.py,
# with the timeline tightened to 8 s: name 0.9 s, English line 1.6 s, shloka 2.4 s, meaning 3.6 s, end card 6.2 s.
# Usage: python3 navratri_short.py <day> <absolute outdir>   (the flute track is laid on afterwards with ffmpeg)
import os, sys, asyncio, subprocess
from playwright.async_api import async_playwright
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
import navratri_photo as P
DUR = 8.0
SWAP = [('animation:push 13.0s', f'animation:push {DUR}s'), ('animation:in 1.2s 1.4s', 'animation:in 1s .7s'),
        ('animation-delay:.2s', 'animation-delay:0s'), ('animation-delay:.6s', 'animation-delay:.3s'),
        ('animation-delay:1.8s', 'animation-delay:.9s'), ('animation-delay:2.8s', 'animation-delay:1.6s'),
        ('animation-delay:4.0s', 'animation-delay:2.4s'), ('animation-delay:5.8s', 'animation-delay:3.6s'),
        ('animation:fi 1s 10.4s', 'animation:fi .8s 6.2s')]

async def main(day, out):
    D = P.DAYS[day]; html = P.page(day)
    for a, b in SWAP:
        assert a in html, a
        html = html.replace(a, b)
    fn = os.path.join(out, f'navratri-day{day}-{D["slug"]}-short.html'); open(fn, 'w').write(html)
    mp4 = os.path.join(out, f'navratri-day{day}-{D["slug"]}-short-8s.mp4')
    async with async_playwright() as p:
        b = await p.chromium.launch(); pg = await b.new_page(viewport={'width': P.W, 'height': P.H})
        await pg.goto('file://' + fn); await pg.evaluate('document.fonts.ready'); await pg.wait_for_timeout(600)
        await pg.evaluate('document.getAnimations().forEach(a=>a.pause())')
        async def at(t): await pg.evaluate(f'document.getAnimations().forEach(a=>{{a.currentTime={t*1000}}})')
        ff = subprocess.Popen(['ffmpeg', '-v', 'error', '-y', '-f', 'image2pipe', '-framerate', str(P.FPS), '-i', '-', '-c:v', 'libx264',
                               '-pix_fmt', 'yuv420p', '-crf', '17', '-preset', 'medium', '-movflags', '+faststart', mp4], stdin=subprocess.PIPE)
        for i in range(int(DUR * P.FPS)):
            await at(i / P.FPS); ff.stdin.write(await pg.screenshot(type='jpeg', quality=95))
        ff.stdin.close(); ff.wait()
        for t in (1.0, 5.5, 7.6):
            await at(t); await pg.screenshot(path=os.path.join(out, f'_short-check-{t}.png'))
        await b.close()

if __name__ == '__main__':
    asyncio.run(main(int(sys.argv[1]), sys.argv[2]))
