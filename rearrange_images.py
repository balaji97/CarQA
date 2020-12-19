#Script to rearrange training images into their respective class folders as specified by 'cars_train_annos.mat'

from mat4py import loadmat
import os

trainAnnons = loadmat('cars_train_annos.mat')

numberOfFiles = len(trainAnnons['annotations']['fname'])

#First we need to make folders for each class
#for className in range(1, 197):
#	os.mkdir('./cars_train/' + str(className))

for imageNumber in range(numberOfFiles):

	currentImageLocation = './cars_train/' + str(trainAnnons['annotations']['class'][imageNumber]) + '/' + str(trainAnnons['annotations']['fname'][imageNumber])
	newImageLocation = './cars_train/' + str(trainAnnons['annotations']['fname'][imageNumber])

	os.rename(currentImageLocation, newImageLocation)