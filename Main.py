from ast import Sub
from contextlib import AsyncExitStack
from dataclasses import replace
from http.client import FORBIDDEN
import os
from re import A, sub
from unicodedata import category
from venv import create


def createCategoryFolder(assetCategory, numberOfAssets, assetCategoryDestination):
    os.makedirs(assetCategory) #Creates category destination
    assetCategoryDestination=assetCategoryDestination+'\\'+assetCategory
    os.chdir(assetCategoryDestination) #goes to asset category destination

    assetDirectory = assetCategoryDestination #assetName='FO' #Asset Number Name Here example: FO
    assetNumberStart=1   #Asset Number Starting Number example: 1

    for i in range(assetNumberStart,numberOfAssets+1): 
        os.chdir(assetDirectory)
        if i<10:
            newFolder=assetCategory + '-' + '0' + str(i)
        else:
            newFolder=assetCategory + '-' + str(i)

        #Check existence of directory, cancel if already existing
        try:
            if not os.path.exists(newFolder):
                os.makedirs(newFolder)
            
            #Create subdirectory under main asset directory
            #Subdirectories without subfolders
            subFolderWithoutSubfolders= ['MAN', 'TRB', 'TRG','PRG', 'IOT', 'SFT']
            for k in subFolderWithoutSubfolders:
                subDirectory=assetDirectory+'\\'+newFolder
                os.chdir(subDirectory)
                os.makedirs(k)
            
            #Subdirectories with subfolders
            subDirectory=assetDirectory+'\\'+newFolder

            os.chdir(subDirectory)
            subFolder='PAR'
            os.makedirs(subFolder)
            subSubDirectory=subDirectory+'\\'+subFolder
            os.chdir(subSubDirectory)
            os.makedirs('ELE')
            os.makedirs('MEC')

            os.chdir(subDirectory)
            subFolder='SRS'
            os.makedirs(subFolder)
            subSubDirectory=subDirectory+'\\'+subFolder
            os.chdir(subSubDirectory)
            os.makedirs('REF')
            os.makedirs('QUO')

            os.chdir(subDirectory)
            subFolder='UGS'
            os.makedirs(subFolder)
            subSubDirectory=subDirectory+'\\'+subFolder
            os.chdir(subSubDirectory)
            os.makedirs('REF')
            os.makedirs('QUO')

            os.chdir(subDirectory)
            subFolder='OPR'
            os.makedirs(subFolder)
            subSubDirectory=subDirectory+'\\'+subFolder
            os.chdir(subSubDirectory)
            os.makedirs('MST')
            os.makedirs('IMP')
            os.makedirs('PRC')       
            os.makedirs('DST')       
            
        except OSError:
            print('Error: Directory exists, change the folder name')


def assetLetterFolders (assetLetterFolderDestination, assetLetter):
    os.chdir(assetLetterFolderDestination) #Goes to Letter Destination 
    os.makedirs(assetLetter) #Creates Letter 
    assetLetterFolderDirectory=assetLetterFolderDestination+'\\'+assetLetter
    

    myDictionary = {'TB':50}# Example {'FO': 12} 
    for key in myDictionary:
        os.chdir(assetLetterFolderDirectory)
        assetCategory = key
        numberOfAssets = myDictionary[key]
        createCategoryFolder(assetCategory , numberOfAssets, assetLetterFolderDirectory)


assetLetterFolderDestination = "C:\\PythonApps\\2022_04\\Folder_Dump"
assetLetter= 'ZZ'
assetLetterFolders(assetLetterFolderDestination, assetLetter)
print(assetLetterFolderDestination)



