"""Image generation utility module."""
import math
import os
from PIL import Image

def MakeImage(paintFunction, name="img", size=256, channels='RGBA', multisample=4):
	"""Save a square PNG image in the current directory, as defined by a resolution-independent painting function.
	
	Mandatory argument:
	paintFunction -- Painting function. Takes in two floating point parameters (x, y) (coordinates in range -1..+1) and returns an integer tuple corresponding to the color of one pixel.
	
	Keyword arguments:
	name -- Saved image name, without termination. A count will be added if the name is already in use.
	size -- Final image size, in pixels per side (it will be a square image).
	channels -- Color mode for the saved file. Options include 'RGB' and 'RGBA' for color, 'L' and 'LA' for grayscale, '1' for one-bit black and white.
	multisample -- The image is processed at a higher resolution and downsampled before saving. This parameter determines the additional working resolution.
	"""
	fullSize = size * multisample
	scaleFactor = 2.0 / (fullSize - 1)
	
	filename = name + ".png"
	filename_counter = 0
	while os.path.exists(filename):
		filename = "%s-%2d.png" % (name, filename_counter)
		filename_counter += 1

	workingImage = Image.new(channels, (fullSize, fullSize))
	pixels = workingImage.load()

	for y in range(fullSize):
		for x in range(fullSize):
			xx = x * scaleFactor - 1.0 # -1..+1
			yy = 1.0 - y * scaleFactor # -1..+1
			pixels[x, y] = paintFunction(xx, yy)

	finalImage = workingImage.resize((size, size), Image.LANCZOS)
	finalImage.save(filename, 'PNG')

def circleCutout(numChannels=4):
	"""Decorator factory. Add to a paint function to apply a circular alpha mask to the image.
	
	Keyword arguments:
	numChannels -- Number of channels the paint function returns (default: 4).
	"""
	def decorator(paintFunction):
		def wrapper(x, y):
			if x * x + y * y > 1:
				return (0,) * numChannels
			else:
				return paintFunction(x, y)
		return wrapper
	return decorator

def softCutout(paintFunction):
	"""Decorator. Add to a non-transparent paint function to apply a fading alpha mask to the image."""
	def wrapper(x, y):
		l = math.sqrt(x * x + y * y)
		t = 0 if l > 1 else 1.0 - l
		smooth = t * t * t * (10.0 + t * (-15.0 + 6.0 * t)) # Smootherstep
		a = int(255 * smooth)
		return paintFunction(x, y) + (a,)
	return wrapper
