#!/usr/bin/env python3
##!/usr/bin/local python3

import json
import os.path
from os import path

globalDataJson = None
globalFileList = None

def resetAll():
  """ Reset all variables to the default value.
  """
  globalDataJson = None
  globalFileList = None

def readConfigurationFileExtension():
  """ Read JSON file with defined file extensions for sort process.
  """
  with open('configuration-file-extension.json') as configFileJson:
    dataJson = None
    dataJson = json.load(configFileJson)

    if dataJson != None:
      globalDataJson = dataJson
      for p in dataJson['fileExtensions']:
        print(p['name'] + ": " + str(p['extension']))

def sortFilesFromGivenDirectoryPath(pathName=None):
  """
  Method sort all files from given path to the defined extensions file.
  All correct files will be moved to a named folder.
  If a file is not passing to an extension, then will this file not moved!
  """
  if pathName != None:
    print('')
    print('Sort all files form directory path "' + pathName + '".')

    if os.path.exists(pathName) and os.path.isdir(pathName):
      fileList = os.listdir(pathName)
      if fileList != None and len(fileList) > 0:
        print('File count: ' + str(len(fileList)))
        globalFileList = fileList
      else:
        print('No files in directory!')
  else:
    print("Path is not set!")

def createNewFolder(pathName=None, directoryName=None):
  """
  Method creates a new folder with given name, if a file has the right extension name.
  """
  if pathName != None and directoryName != None:
    print("Create new folder: '" + directoryName + "'")

def moveFileToFolder(pathFolderName=None, pathFileName=None):
  """
  Method moves file with right extension to folder.
  """
  if pathFolderName != None and pathFileName != None:
    print("Move file '" + pathFileName + "' to folder '" + pathFolderName + "'.")

# sort files from given path
## check if path exist and is a directory
## check if are file in the directory
# # check if file is from config extensions then create new folder if it not exists and move file to there 

resetAll()
readConfigurationFileExtension()
sortFilesFromGivenDirectoryPath("/Users/stefanschultz/development/projects-python/StanszFileSorterPy/test/")