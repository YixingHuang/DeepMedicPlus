high sensitivity model:
deepMedicWide1.high_sensitivity.model.ckpt

high precision model:
deepMedicWide1.high_precision.model.ckpt


inference/test command line:
-model ./examples/configFiles/deepMedicPlus/model/modelConfig_wide1_deeper.cfg -test ./examples/configFiles/deepMedicPlus/test/testConfig.cfg -load ./examples/output/saved_models/deepMedicWide1.high_sensitivity.model.ckpt -dev cuda0

put the main test volume paths in \examples\configFiles\deepMedicBMDualPath\test\testChannels_t1c.cfg
put the corresponding prior volume paths in \examples\configFiles\deepMedicBMDualPath\test\testPriorChannels_t1c.cfg

If no prior volume, simply put the path to a volume with Zero values only.
