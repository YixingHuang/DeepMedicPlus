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
# Preprocess_N4
#

class Preprocess_N4:
  def __init__(self, parent):
    parent.title = "Preprocess_N4"
    parent.categories = ["#Preprocessing_Brain"]
    parent.dependencies = []
    parent.contributors = ["Florian Putz [FAU Erlangen]"] 
    parent.helpText = "N4 Biasfield correction applied to an input folder"
    parent.acknowledgementText ="Florian Putz [FAU Erlangen]"
    
    self.parent = parent
    parent.icon = qt.QIcon("C:\\Python\\LevelTracingPro.png")



class Preprocess_N4Widget(ScriptedLoadableModuleTest):
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
    sampleCollapsibleButton.text = "N4-Biasfield Correction"
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


  def onReload(self,moduleName="Preprocess_N4"):
    """Generic reload method for any scripted module.
    ModuleWizard will subsitute correct default moduleName.
    """

    globals()[moduleName] = slicer.util.reloadScriptedModule(moduleName)


  def cleanup(self):
    print("Module closed\n")


  def PerformCorrections(self):

   SourcePath = "C:\\data\\input\\mri\\mri_unseg\\"
   TargetPath = "C:\\data\\output\\n4_output\\"

   filenames = []

   for key in os.listdir(SourcePath):
     filenames.append(key)

   for eachfilename in filenames:

     SaveandExport=slicer.util.findChildren(name='FileCloseSceneAction')[0]
     SaveandExport.trigger()

     EachDataset = slicer.util.loadVolume(SourcePath+eachfilename)

     print ("Performing N4 on "+eachfilename)

     parametersN4 = {
        'inputImageName' : EachDataset,
        'outputImageName' : EachDataset
     }

     cmdLineN4 = slicer.cli.runSync(slicer.modules.n4itkbiasfieldcorrection , parameters=parametersN4)
     self.assertIsNotNone(cmdLineN4)

     slicer.util.saveNode(EachDataset, TargetPath+eachfilename.replace(".nii.gz","_n4.nii.gz"), properties={})
    


