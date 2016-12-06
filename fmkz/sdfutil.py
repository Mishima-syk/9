from rdkit import Chem
from rdkit.Chem import AllChem
from rdkit import DataStructs
from joblib import Memory
import numpy as np

memory = Memory(cachedir="/tmp", verbose=0)


@memory.cache
def sdf_to_desc(sdf_file):
    fps = []
    targets = []
    nfps = []

    for mol in Chem.SDMolSupplier(sdf_file):
        fps.append(AllChem.GetMorganFingerprintAsBitVect(mol, 2))  # fingerprint
        targets.append(float(mol.GetProp("ACTIVITY")))  # activity

    for fp in fps:
        nfp = np.zeros((1,))
        DataStructs.ConvertToNumpyArray(fp, nfp)
        nfps.append(nfp)

    return (np.array(nfps), np.array(targets))


if __name__ == '__main__':
    descs, targets = sdf_to_desc("CHEMBL3301363.sdf")
    print descs.shape
    print targets.shape
