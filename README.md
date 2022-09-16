# DeepMedic+
## Deep learning for brain metastasis detection and segmentation in longitudinal MRI data
This is the official code repository for our Medical Physics paper "Deep learning for brain metastasis detection and segmentation in longitudinal MRI data": https://doi.org/10.1002/mp.15863
 
 The backbone of our implementation is from the [original DeepMedic repository](https://github.com/deepmedic/deepmedic). Therefore, almost all the instructions from the original DeepMedic repository still apply to our implementation.
 
 ## Citation
 To use these codes, please cite our paper:
 
 [1] Y. Huang, C. Bert, P. Sommer, B. Frey, U. Gaipl, L. V. Distel, T. Weissmann, M. Uder, M. A. Schmidt, A. D¨orfler, A. Maier, R. Fietkau, and F. Putz, “Deep learning for brain metastasis detection and segmentation in longitudinal mri data,” Medical Physics, vol. 49, no. 9, pp. 5773–5786, 2022.
 
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

## Graphical abstract

![Graphical abstract](GraphicalAbstract.png)

## Contents
This repository contains our DeepMedic+ implementation with prior volumes and proposed volume-level sensitivity-specificity (VSS) loss, as well as the pretrained high-sensitivity and high-precision model weights.
For retraining on your own datasets, our preprocessing pipeline is also shared.

### Pretrained models
Pretrained models are located at 
[DeepMedicDualPath\examples\output\saved_models\pretrainedModels](./DeepMedicPlus/examples/output/saved_models/pretrainedModels/)

