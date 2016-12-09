from rdkit import Chem
from pychembldb import *
import click


def doc_check():
    for assay in chembldb.query(Assay).all():
        if assay.doc.journal == "J. Med. Chem.":
            act_num = len(assay.activities)
            if act_num > 100:
                print act_num, assay.chembl_id, assay.description


If __name__ == '__main__':
    doc_check()
