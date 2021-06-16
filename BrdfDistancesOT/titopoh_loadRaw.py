'''
This file contains utility functions to load titopo (Theta_in / Theta_out / Phi_out) brdf Files into Keras
Titopo files are generated by BrdfModifier with the -O option
'''

import struct
import numpy as np
import math
import BvqmFiles
import string
import os.path

def LoadTitopo(material_name):
#returnBrdf = np.empty((3,90,90,360))
	titopoh_file = material_name

	if os.path.isfile(material_name) == False:
		titopoh_file = BvqmFiles.merlDirectory()+"/"+material_name

	titopoData = open(titopoh_file,'rb').read()
	#length = 45*45*180*3
	length = 90*90*360*3

	returnBrdf = np.array(struct.unpack_from(str(length) +'f',titopoData))
	returnBrdf[np.isnan(returnBrdf)] = 0

	return returnBrdf
