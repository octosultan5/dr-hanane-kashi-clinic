import sys
from pathlib import Path
import shutil

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")


CLINIC = Path(r"C:\Users\USER\.gemini\antigravity\scratch\dr-hanane-kashi-clinic")
DESKTOP = Path(r"C:\Users\USER\Desktop\dr-hanane-kashi-clinic")

for f in CLINIC.glob("*.html"):
    c = f.read_text(encoding="utf-8")
    if 'href="#" class="dropdown-toggle"' in c:
        c = c.replace('href="#" class="dropdown-toggle"', 'href="javascript:void(0)" class="dropdown-toggle"')
        f.write_text(c, encoding="utf-8")
        shutil.copy2(f, DESKTOP / f.name)

print("✅ Perfect: All dropdown toggle links replaced with javascript:void(0) and synced to Desktop!")
