# coding=utf-8
from __main__ import vtk, qt, ctk, slicer
import os
import unittest
from slicer.ScriptedLoadableModule import *
import logging
import EditorLib
from EditorLib.EditOptions import HelpButton
from EditorLib.EditOptions import EditOptions
from EditorLib import EditUtil
from EditorLib import DilateEffect
from EditorLib import LabelEffect
from EditorLib import Effect
from EditorLib import LabelEffectLogic
from copy import copy, deepcopy
import numpy as np
import datetime
import SimpleITK as sitk
import sitkUtils
import subprocess
import vtkITK
import ScreenCapture
import time
#


#
# Preprocess_RegNorm
#

class Preprocess_RegNorm:
  def __init__(self, parent):
    parent.title = "Preprocess_RegNorm"
    parent.categories = ["#Preprocessing_Brain"]
    parent.dependencies = []
    parent.contributors = ["Florian Putz [FAU Erlangen]"] 
    parent.helpText = "Resampling according to template and intensity normalization"
    parent.acknowledgementText ="Florian Putz [FAU Erlangen]"
    
    self.parent = parent
    parent.icon = qt.QIcon("C:\\Python\\LevelTracingPro.png")



class Preprocess_RegNormWidget(ScriptedLoadableModuleTest):
  def __init__(self, parent = None):


    if not parent:
      self.parent = slicer.qMRMLWidget()
      self.parent.setLayout(qt.QVBoxLayout())
      self.parent.setMRMLScene(slicer.mrmlScene)
    else:
      self.parent = parent
    self.layout = self.parent.layout()
    if not parent:
      self.setup()
      self.parent.show()

  def setup(self):
    self.reloadButton = qt.QPushButton("Reload Module")
    self.reloadButton.toolTip = "Reload this module."
    self.reloadButton.name = "Charting Reload"
    self.layout.addWidget(self.reloadButton)
    self.reloadButton.connect('clicked()', self.onReload)

    # Collapsible button
    sampleCollapsibleButton = ctk.ctkCollapsibleButton()
    sampleCollapsibleButton.text = "Resampling according to template and intensity normalization"
    self.layout.addWidget(sampleCollapsibleButton)

    # Layout within the sample collapsible button
    sampleFormLayout = qt.QFormLayout(sampleCollapsibleButton)
    PutzHeading = qt.QLabel("Florian Putz [FAU Erlangen]")
    sampleFormLayout.addWidget(PutzHeading)

    NeueZeile = qt.QLabel("\nFlorian Putz [FAU Erlangen]\n")
    sampleFormLayout.addWidget(NeueZeile)


    LabelTestButton = qt.QPushButton("Start Batch")
    sampleFormLayout.addWidget(LabelTestButton)

    LabelTestButton.connect('clicked(bool)', self.PerformCorrections)


  def onReload(self,moduleName="Preprocess_RegNorm"):
    """Generic reload method for any scripted module.
    ModuleWizard will subsitute correct default moduleName.
    """

    globals()[moduleName] = slicer.util.reloadScriptedModule(moduleName)


  def cleanup(self):
    print("Module closed\n")


  def PerformCorrections(self):

   SourcePath = "<SourcePath>"
   TargetPath = "<TargetPath>"
   TemplatePath = "<TemplatePath>\\OwnTemplate.nii.gz"

   filenames = []

   for key in os.listdir(SourcePath):
     filenames.append(key)

   for eachfilename in filenames:

    SaveandExport=slicer.util.findChildren(name='FileCloseSceneAction')[0]
    SaveandExport.trigger()

    EachDataset = slicer.util.loadVolume(SourcePath+eachfilename)

    print ("Performing Resampling and Normalization on "+eachfilename)

    print ("Autoresampling according to template dataset")
    outputTransform = slicer.vtkMRMLLinearTransformNode()
    slicer.mrmlScene.AddNode(outputTransform)

    OwnTemplate = slicer.util.loadVolume(TemplatePath)

    print ("Loaded OwnTemplate")

    print ("Registering "+eachfilename)

    parameters = {
      'fixedVolume' : OwnTemplate,
      'movingVolume' : EachDataset,
      'linearTransform' : outputTransform,
      'transformType' : "Rigid",
      'initializeTransformMode' : "useGeometryAlign",
      'samplingPercentage' : "0.02"
    }

    slicer.cli.runSync(slicer.modules.brainsfit, parameters=parameters)

    print ("Resampling "+eachfilename)

    parametersResample = {
      'referenceVolume' : OwnTemplate,
      'inputVolume' : EachDataset,
      'warpTransform' : outputTransform,
      'outputVolume' : EachDataset,
      'pixelType' : "float",
      'interpolationMode' : "Linear",
    }

    slicer.cli.runSync(slicer.modules.brainsresample, parameters=parametersResample)

    EachDataset.RemoveNodeReferenceIDs("transform")

    slicer.util.saveNode(EachDataset, TargetPath+eachfilename.replace(".nii.gz","_res.nii.gz"), properties={})

    t1c_itk = sitk.ReadImage(sitkUtils.GetSlicerITKReadWriteAddress(EachDataset))
    normalizefilter = sitk.NormalizeImageFilter()
    t1c_itk = normalizefilter.Execute(t1c_itk)
    sitk.WriteImage(t1c_itk, sitkUtils.GetSlicerITKReadWriteAddress(EachDataset))

    slicer.util.saveNode(EachDataset, TargetPath+eachfilename.replace(".nii.gz","_res_norm.nii.gz"), properties={})
    slicer.util.saveNode(outputTransform, TargetPath+eachfilename.replace(".nii.gz",".mat"), properties={})

    print ("Autoresampling has finished")

