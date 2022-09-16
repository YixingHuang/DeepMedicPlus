import os

#Test for high-sensitivity model:
cmd = 'python deepMedicRun -model ./examples/configFiles/deepMedicPlus/model/modelConfig_wide1_deeper.cfg -test ./examples/configFiles/deepMedicPlus/test/testConfig.cfg -load ./examples/output/saved_models/pretrainedModels/deepMedicWide1.high_sensitivity.model.ckpt -dev cuda0'


#Test for high-specificity model:
cmd2 = 'python deepMedicRun -model ./examples/configFiles/deepMedicPlus/model/modelConfig_wide1_deeper.cfg -test ./examples/configFiles/deepMedicPlus/test/testConfig.cfg -load ./examples/output/saved_models/pretrainedModels/deepMedicWide1.high_precision.model.ckpt -dev cuda0'

# new training
cmd3 = 'python deepMedicRun -model ./examples/configFiles/deepMedicPlus/model/modelConfig_wide1_deeper.cfg  -train ./examples/configFiles/deepMedicPlus/train/trainConfigwide.cfg  -dev cuda1'

os.system(cmd3)
