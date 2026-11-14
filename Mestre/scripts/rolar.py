"""Rolador de dados do mestre.

Rola dados com gerador aleatório do sistema (secrets), pra que o mestre nunca
escolha o resultado de uma rolagem de NPC. Mostra cada dado, o que foi mantido
e o total.

Uso:
    python rolar.py EXPRESSAO [EXPRESSAO ...] [-r "rótulo"]

Expressões:
    1d20        um d20
    3d20h       3d20, fica com o maior   (h = high)
    2d20l       2d20, fica com o menor   (l = low)
    3d20h+10    3d20, maior, +10
    2d6+3       soma dos dados +3
    1d8-1       soma dos dados -1

Exemplos:
    python rolar.py 2d20h+5 -r "zumbi: ataque"
    python rolar.py 1d8+2 -r "zumbi: dano"
    python rolar.py 1d20 2d20h 3d20h -r "iniciativa dos três cultistas"
"""

import argparse
import re
import secrets
import sys

PADRAO = re.compile(r"^(\d*)d(\d+)([hl]?)([+-]\d+)?$", re.IGNORECASE)


def rolar(expr: str) -> str:
    m = PADRAO.match(expr.strip())
    if not m:
        raise ValueError(f"expressão inválida: {expr!r} (ex.: 3d20h+5, 2d6+3, 2d20l)")
    qtd = int(m.group(1) or 1)
    faces = int(m.group(2))
    modo = m.group(3).lower()
    mod = int(m.group(4) or 0)
    if qtd < 1 or qtd > 100 or faces < 2 or faces > 1000:
        raise ValueError(f"fora dos limites: {expr!r}")

    dados = [secrets.randbelow(faces) + 1 for _ in range(qtd)]
    if modo == "h":
        base, como = max(dados), "maior"
    elif modo == "l":
        base, como = min(dados), "menor"
    else:
        base, como = sum(dados), "soma"
    total = base + mod

    mod_txt = f" {'+' if mod >= 0 else '-'} {abs(mod)}" if mod else ""
    um_dado = modo in ("h", "l") or qtd == 1
    nat = "  (20 natural)" if faces == 20 and um_dado and base == 20 else ""
    return f"{expr}: {dados} -> {como} {base}{mod_txt} = {total}{nat}"


def main() -> int:
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
        sys.stderr.reconfigure(encoding="utf-8")
    p = argparse.ArgumentParser(description="Rolador de dados do mestre")
    p.add_argument("expr", nargs="+", help="ex.: 3d20h+5, 1d8+2, 2d20l")
    p.add_argument("-r", "--rotulo", default="", help="o que está sendo rolado")
    a = p.parse_args()
    if a.rotulo:
        print(f"# {a.rotulo}")
    try:
        for e in a.expr:
            print(rolar(e))
    except ValueError as err:
        print(f"erro: {err}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
