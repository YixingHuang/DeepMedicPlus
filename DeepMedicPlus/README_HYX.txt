
Trained models are saved in the folder of DeepMedicDualPath\examples\output\saved_models\TPTNwMean0995_retest_bs10

High sensitivity model:
deepMedicWide1.TPTNwMean0995_retest_bs10.final.2021-09-24.19.06.13.044084.model.ckpt

High precision model:
deepMedicWide1.TPTNwMean0995_retest_bs10.final.2021-09-28.19.32.33.582391.model.ckpt


inference/test command line:
-model ./examples/configFiles/deepMedicBMDualPath/model/modelConfig_wide1_deeper.cfg -test ./examples/configFiles/deepMedicBMDualPath/test/testConfig.cfg -load ./examples/output/saved_models/pretrainedModels/deepMedicWide1.TPTNwMean0995_retest_bs10.final.2021-09-28.19.32.33.582391.model.ckpt -dev cuda0

Put the main test volume paths in \examples\configFiles\deepMedicBMDualPath\test\testChannels_t1c.cfg
put the corresponding prior volume paths in \examples\configFiles\deepMedicBMDualPath\test\testPriorChannels_t1c.cfg

If no prior volume, simply put the path to a volume with Zero values only.


numpy version:1.19.5    it seems that there is compatibility problems with the latest numpy versions.

I run our codes in a Windows system with Python 3.7, CUDA 11.0; Higher versions should be okay.
