import os
import nibabel as nib
import numpy as np

root = r"C:\Users\agarw\Downloads\COCA\cocacoronarycalciumandchestcts-2\Train_Subset\coca_project\data_canonical\images"

for f in os.listdir(root):
    if f.endswith("_seg.nii.gz"):
        seg = nib.load(os.path.join(root, f)).get_fdata()
        nz = np.sum(seg > 0)
        if nz > 0:
            print(f, nz)
