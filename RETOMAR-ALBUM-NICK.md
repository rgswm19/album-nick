# Álbum do Nick — como retomar / fazer a v2

App de figurinhas da Copa 2026 do Nick (PWA, funciona offline no iPhone/iPad).

## Links e onde está tudo
- **No ar (o app):** https://rgswm19.github.io/album-nick/
- **Pasta no Mac:** ~/figurinhas-nickolas
- **GitHub:** rgswm19/album-nick
- **Versão atual salva como:** tag `v1` (dá pra voltar a ela sempre)

## Como retomar (jeito fácil)
Abrir uma nova sessão do Claude Code e dizer:
> "Abre o Álbum do Nick em ~/figurinhas-nickolas. Quero fazer a versão 2 (ou tal correção)."

O Claude lê o código e faz. Não precisa saber nada técnico.
(Obs.: o Claude já guardou esse projeto na memória dele, então deve lembrar sozinho.)

## Estrutura (pra quem for mexer)
- **app-source.html** = o código de verdade (editar aqui).
- **index.html** = versão que fica no ar. NÃO editar na mão. É gerada por `python3 build.py`.
- **assets/** = logos e as 48 bandeiras.
- **README.md** = instruções técnicas.

## Publicar uma mudança (3 passos, no terminal dentro da pasta)
1. Editar `app-source.html`
2. `python3 build.py`
3. `git add -A && git commit -m "mudanca" && git push`
O site atualiza sozinho em ~1 minuto.

## Bom saber
- O **link nunca muda** e ninguém precisa reinstalar. Reabrir com internet uma vez e pronto.
- O **progresso do Nick não se perde** em atualizações (fica salvo no aparelho dele).
- Marcar: **toque** soma (falta > tem > repetida 1,2,3...), **segurar** apaga.
