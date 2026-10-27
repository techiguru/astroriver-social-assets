#!/bin/sh
# Downloads the four SIL OFL fonts the templates use into fonts/ (not committed).
cd "$(dirname "$0")" && mkdir -p fonts && B=https://raw.githubusercontent.com/google/fonts/main/ofl
for f in "cormorantgaramond/CormorantGaramond%5Bwght%5D.ttf" "inter/Inter%5Bopsz,wght%5D.ttf" "cinzel/Cinzel%5Bwght%5D.ttf" "tirodevanagarihindi/TiroDevanagariHindi-Regular.ttf"; do
  n=$(basename "$f" | sed 's/%5B/[/g;s/%5D/]/g'); [ -f "fonts/$n" ] || curl -sSfL "$B/$f" -o "fonts/$n"
done
