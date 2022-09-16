For more details about our algorithm, please check our arXiv paper:
Huang Y, Bert C, Sommer P, Frey B, Gaipl U, Distel LV, Weissmann T, Uder M, Schmidt MA, Dörfler A, Maier A., Fietkau R., Putz F., Deep learning for brain metastasis detection and segmentation in longitudinal MRI data. arXiv preprint arXiv:2112.11833. 2021 Dec 22. 

Since our paper has not been officially published (currently under review of Medical Physics), please use the codes only internally and do not share the code and pretrained models with externals. Thanks.


trained models are saved in the folder of DeepMedicDualPath\examples\output\saved_models\TPTNwMean0995_retest_bs10

high sensitivity model:
deepMedicWide1.TPTNwMean0995_retest_bs10.final.2021-09-24.19.06.13.044084.model.ckpt

high precision model:
deepMedicWide1.TPTNwMean0995_retest_bs10.final.2021-09-28.19.32.33.582391.model.ckpt


inference/test command line:
-model ./examples/configFiles/deepMedicBMDualPath/model/modelConfig_wide1_deeper.cfg -test ./examples/configFiles/deepMedicBMDualPath/test/testConfig.cfg -load ./examples/output/saved_models/pretrainedModels/deepMedicWide1.TPTNwMean0995_retest_bs10.final.2021-09-28.19.32.33.582391.model.ckpt -dev cuda0

put the main test volume paths in \examples\configFiles\deepMedicBMDualPath\test\testChannels_t1c.cfg
put the corresponding prior volume paths in \examples\configFiles\deepMedicBMDualPath\test\testPriorChannels_t1c.cfg

If no prior volume, simply put the path to a volume with Zero values only.


numpy version:1.19.5    it seems that there is compatibility problems with the latest numpy versions.

I run our codes in a Windows system with Python 3.7, CUDA 11.0; Higher versions should be okay.