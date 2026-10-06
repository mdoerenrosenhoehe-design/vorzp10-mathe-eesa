import sys
from pathlib import Path
try:
    import qrcode
except ImportError:
    print('Bitte zuerst installieren: pip install qrcode[pil]')
    raise SystemExit(1)
url=sys.argv[1] if len(sys.argv)>1 else input('URL der veröffentlichten Website: ').strip()
out=Path(__file__).parent/'assets'/'qr-code.png'
qrcode.make(url).save(out)
print(f'QR-Code gespeichert: {out}')
