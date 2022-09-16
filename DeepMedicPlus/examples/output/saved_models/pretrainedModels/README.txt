high sensitivity model:
deepMedicWide1.TPTNwMean0996_retest_bs10.final.2021-09-24.19.06.13.044084.model.ckpt

high precision model:
deepMedicWide1.TPTNwMean0996_retest_bs10.final.2021-09-28.19.32.33.582391.model.ckpt


inference/test command line:
-model ./examples/configFiles/deepMedicBMDualPath/model/modelConfig_wide1_deeper.cfg -test ./examples/configFiles/deepMedicBMDualPath/test/testConfig.cfg -load ./examples/output/saved_models/deepMedicWide1.TPTNwMean0995_retest_bs10.final.2021-09-28.19.32.33.582391.model.ckpt -dev cuda0

put the main test volume paths in \examples\configFiles\deepMedicBMDualPath\test\testChannels_t1c.cfg
put the corresponding prior volume paths in \examples\configFiles\deepMedicBMDualPath\test\testPriorChannels_t1c.cfg

If no prior volume, simply put the path to a volume with Zero values only.