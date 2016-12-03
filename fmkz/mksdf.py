from rdkit import Chem
from pychembldb import *
import click


@click.command()
@click.argument("chembl_id")
def chemblid2sdf(chembl_id):
    assay = chembldb.query(Assay).filter_by(chembl_id=chembl_id).first()
    w = Chem.SDWriter("{}.sdf".format(chembl_id))
    for activity in assay.activities:
        m = Chem.MolFromMolBlock(activity.compound.molecule.structure.molfile)
        act = activity.standard_value
        m.SetProp("ACTIVITY", str(act))
        w.write(m)


if __name__ == '__main__':
    chemblid2sdf()
