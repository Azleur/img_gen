import os
from PIL import Image

def MakeImage(paintFunction, name="img", size=256, channels='RGBA', multisample=4):
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