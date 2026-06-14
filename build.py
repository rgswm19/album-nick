#!/usr/bin/env python3
# Gera o index.html (offline, tudo embutido) a partir do app-source.html.
# Uso:  python3 build.py
import base64, pathlib, json

root = pathlib.Path(__file__).resolve().parent
html = (root / 'app-source.html').read_text()

def datauri(p, mime):
    return f'data:{mime};base64,' + base64.b64encode(p.read_bytes()).decode()

# logos + fundo -> data URI
for name, mime in [('assets/wave-blue.jpg', 'image/jpeg'),
                   ('assets/logo26-white.png', 'image/png'),
                   ('assets/logo26-black.png', 'image/png')]:
    html = html.replace(name, datauri(root / name, mime))

# bandeiras -> mapa FLAGS embutido
flags = {f.stem: datauri(f, 'image/png') for f in sorted((root / 'assets/flags').glob('*.png'))}
html = html.replace("/* ============ DADOS ============ */",
                    "\nvar FLAGS=" + json.dumps(flags) + ";\n/* ============ DADOS ============ */", 1)
html = html.replace("function flagSrc(g){return 'assets/flags/'+g.code+'.png';}",
                    "function flagSrc(g){return (window.FLAGS&&FLAGS[g.code])||('assets/flags/'+g.code+'.png');}")

(root / 'index.html').write_text(html)
print('index.html (offline) gerado:', round((root / 'index.html').stat().st_size / 1024), 'KB')
