# DeepMedic+ Preprocessing Pipeline
## Preprocessing Pipeline for "Deep learning for brain metastasis detection and segmentation in longitudinal MRI data"
This is the preprocessing pipeline, which PD Dr. Florian Putz used to preproce our T1 MPRAGE data.
This is one part of the official code repository for our Medical Physics paper "Deep learning for brain metastasis detection and segmentation in longitudinal MRI data": https://doi.org/10.1002/mp.15863
 
 ## Citation
 To use these codes, please cite our paper:
 
 [1] Y. Huang, C. Bert, P. Sommer, B. Frey, U. Gaipl, L. V. Distel, T. Weissmann, M. Uder, M. A. Schmidt, A. Dörfler, A. Maier, R. Fietkau, and F. Putz, “Deep learning for brain metastasis detection and segmentation in longitudinal mri data,” Medical Physics, vol. 49, no. 9, pp. 5773–5786, 2022.
 
 Latex Bibtex:  
 @article{huang2022deep,  
 author = {Huang, Yixing and Bert, Christoph and Sommer, Philipp and Frey, Benjamin and Gaipl, Udo and Distel, Luitpold V. and Weissmann, Thomas and Uder, Michael and Schmidt, Manuel A. and Dörfler, Arnd and Maier, Andreas and Fietkau, Rainer and Putz, Florian},  
 title = {Deep learning for brain metastasis detection and segmentation in longitudinal MRI data},  
journal = {Medical Physics},  
volume = {49},  
number = {9},  
pages = {5773-5786},  
keywords = {brain metastasis, deep learning, ensemble, loss function, MRI, sensitivity specificity},  
doi = {https://doi.org/10.1002/mp.15863},  
url = {https://aapm.onlinelibrary.wiley.com/doi/abs/10.1002/mp.15863},  
eprint = {https://aapm.onlinelibrary.wiley.com/doi/pdf/10.1002/mp.15863},  
year = {2022}  
}  

## Pipeline Steps
### a. N4 bias correction
 This is a [3D Slicer](https://www.slicer.org/) Python model.
 
You can create a new Slicer module by the following steps:

Edit -> Application Setting -> modules -> Additional module paths: -> Add

Add the folder containing the python script. At the first selection, you only see an empty folder. But it is fine. Select ok and restart Slicer, you will see the new module.

Note that we use 3D Slicer version [4.10.2](https://slicer-packages.kitware.com/#collection/5f4474d0e1d8c75dfc70547e/folder/60add36eae4540bf6a89be73)    Latest versions have compatibility issues.

### b. Skull striping using the [HD-BET](https://github.com/MIC-DKFZ/HD-BET) deep learning model developed by DKFZ

### c. Registration and intensity normalization
A template volume named "OwnTemplate.nii.gz" is provided for registration.

## Pipeline without 3D Slicer
If you are not familiar with 3D Slicer, you can follow the steps posted [here](https://github.com/YixingHuang/DeepMedicPlus/issues/5) by DK.
