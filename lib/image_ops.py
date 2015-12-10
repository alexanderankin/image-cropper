import os
from PIL import Image, ImageFilter

class ImageWrapper(object):
	"""This class is not the PIL image class, it is the class that
	is instantiated each time a new image is processed to store 
	information about that image. image_obj is the PIL image object.
	"""

	def __init__(self, path, filename):
		super(ImageWrapper, self).__init__()
		self.path = path
		self.filename = filename
		self.image_obj = Image.open(path)
		
	def crop(self, left, upper, right, lower):
		box = (left, upper, right, lower)
		self.image_obj = self.image_obj.crop(box)

	def save_im(self, outdir):
		self.image_obj.save(outdir + self.filename, 'png')

def ls(startx, starty, endx, endy, in_dir=os.getcwd()+'/in'):
	for i in os.listdir(in_dir):
		if i.startswith('.'): continue
		fulli = in_dir + "/" + i # need full file path
		j = ImageWrapper(fulli, i)
		j.crop(startx, starty, endx, endy)
		# get parent of directory, php string manipulation style
		parent_of_in_directory = \
			((in_dir[::-1])[(in_dir[::-1]).find("/"):])[::-1]
		
		j.save_im(parent_of_in_directory + "out/")
		del j
