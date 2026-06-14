# Álbum do Nickolas — figurinhas Copa 2026

App (PWA offline) pra marcar figurinhas que tem / faltam / repetidas, com busca e relatório A4.

- **No ar:** https://rgswm19.github.io/album-nick/
- **Fonte editável:** `app-source.html` (este é o arquivo que se edita)
- **Servido no site:** `index.html` (GERADO automaticamente, não edite à mão)
- **Bandeiras/logos:** `assets/`

## Como atualizar (numa nova sessão do Claude Code)

1. Edite `app-source.html`.
2. Regere o arquivo offline:
   ```
   python3 build.py
   ```
3. Publique:
   ```
   git add app-source.html index.html
   git commit -m "ajuste"
   git push
   ```
O site atualiza sozinho em ~1 min. **O link continua o mesmo** e o **progresso do Nick (salvo no aparelho) não se perde**.

## Dados do Nick
A lista de faltantes inicial está embutida em `app-source.html` na constante `INITIAL_MISSING`
(só vale na primeira abertura; depois valem as marcações feitas no aparelho).
