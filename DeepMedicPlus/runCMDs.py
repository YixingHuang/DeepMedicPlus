import os

#Test for high-sensitivity model:
cmd = 'python deepMedicRun -model ./examples/configFiles/deepMedicBMDualPath/model/modelConfig_wide1_deeper.cfg -test ./examples/configFiles/deepMedicBMDualPath/test/testConfig.cfg -load ./examples/output/saved_models/pretrainedModels/deepMedicWide1.TPTNwMean0995_retest_bs10.final.2021-09-28.19.32.33.582391.model.ckpt -dev cuda0'


#Test for high-specificity model:
cmd2 = 'python deepMedicRun -model ./examples/configFiles/deepMedicBMDualPath/model/modelConfig_wide1_deeper.cfg -test ./examples/configFiles/deepMedicBMDualPath/test/testConfig.cfg -load ./examples/output/saved_models/pretrainedModels/deepMedicWide1.TPTNwMean0995_retest_bs10.final.2021-09-28.19.32.33.582391.model.ckpt -dev cuda0'

# new training
cmd3 = 'python deepMedicRun -model ./examples/configFiles/deepMedicBMDualPath/model/modelConfig_wide1_deeper.cfg  -train ./examples/configFiles/deepMedicBMDualPath/train/trainConfigwide.cfg  -dev cuda1'

os.system(cmd3)
