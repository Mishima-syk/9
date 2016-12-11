# -*- coding: utf-8 -*-

from rdkit import Chem
from rdkit.Chem import Draw
import click


@click.command()
@click.argument("sdffile")
@click.option("--out", "-o", default="output.png")
def draw_mol_grid(sdffile, out):
    num = 200
    suppl = Chem.SDMolSupplier(sdffile.encode("utf-8"))
    ms = [x for x in suppl if x is not None]
    img = Draw.MolsToGridImage(ms[:num],
                               molsPerRow=10,
                               subImgSize=(150, 150),
                               legends=[x.GetProp("ACTIVITY") for x in ms[:num]])
    img.save(out)


if __name__ == '__main__':
    draw_mol_grid()
