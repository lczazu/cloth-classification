from skimage import io, transform
import os
import numpy as np

import warnings
import matplotlib.pyplot as plt
warnings.filterwarnings("ignore")

def pro_images( dir, pro_dir, delete = [16,16],size = [128,128] ):
	i = 0

	for file in os.listdir( dir ):

		if i % 1000 == 0:
			print( 'step', i )
		file_path = os.path.join( dir,file)
		image = io.imread( file_path )

		if len( image.shape ) != 3:
			print( image.shape )
		if image.shape[2] != 3:
			print( image.shape )
			plt.figure( )
			plt.imshow( image[:,:,:3] )


		# image = image[:,:,:3]
		# image = image[:,delete[0]:-delete[1]]
		# image = transform.resize( image, size)
		# image = image * 255
		# image = np.round( image )
		# image = image.astype(np.uint8)
		# new_file = os.path.join( pro_dir, file )
		# io.imsave( new_file, image )

		i = i + 1


pro_images( 'data/image/train', 'data/image/pro_train' )
pro_images( 'data/image/test', 'data/image/pro_test')

# file_path = 'data/image/train/1208413131_0.jpg'
# image = io.imread( file_path )
# print( image.shape )
# plt.imshow( image[:,:,:3] )
plt.show( )
