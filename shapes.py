import math
import img_gen

def MakeShapes():
	"""Make all the shapes (5 total). Saves them in the working directory as PNG files."""
	MakeBullseye()
	MakeSpiral()
	MakeFadedSpiral()
	MakeTriangle()
	MakeTriad()

def MakeBullseye():
	"""Make a black and white bullseye symbol. Saves it in the working directory as a PNG file."""
	img_gen.MakeImage(pfBullseye, name="bullseye", size=64, channels="L")

def MakeSpiral():
	"""Make a grayscale spiral. Saves it in the working directory as a PNG file."""
	img_gen.MakeImage(pfSpiral, name="spiral", size=128, channels="L")

def MakeFadedSpiral():
	"""Make a grayscale spiral with added alpha fade. Saves it in the working directory as a PNG file."""
	img_gen.MakeImage(pfFadedSpiral, name="faded_spiral", size=256, channels="LA")

def MakeTriangle():
	"""Make a black and white triangle. Saves it in the working directory as a PNG file."""
	img_gen.MakeImage(pfTriangle, name="triangle", size=64, channels="L")

def MakeTriad():
	"""Make a black and white triple triangle. Saves it in the working directory as a PNG file."""
	img_gen.MakeImage(pfTriad, name="triad", size=256, channels="L", multisample=8)

def pfBullseye(x, y):
	"""Painting function for the bullseye symbol. Should be provided as argument for img_gen.MakeImage."""
	l = math.sqrt(x * x + y * y)
	if l > 1:
		return 0
	if l > 0.8:
		return 255
	if l > 0.5:
		return 0
	return 255

def pfSpiral(x, y):
	"""Painting function for the opaque spiral. Should be provided as argument for img_gen.MakeImage."""
	l = math.sqrt(x * x + y * y)
	t = math.atan2(y, x)
	A = math.cos(0.5 * t + 6 * l)
	A = A * A
	return (int(255 * A),)

pfFadedSpiral = img_gen.softCutout(pfSpiral)

def isInHalfPlane(x, y, u, v, h):
	"""Check if the point (x, y) is within the half plane defined by its normal (u, v) and its cutoff value h."""
	return x * u + y * v >= h

s60 = math.sin(math.pi / 3.0)
c60 = math.cos(math.pi / 3.0)
minY = 1 - math.sqrt(3.0)
# centerY = 1 - 0.5 * math.sqrt(3.0)

def isInUnitTriangle(x, y):
	"""Check if the point (x, y) is within the maximum equilateral triangle that fits in the box [-1,+1]x[-1,+1], has a horizontal base, and has top vertex (0,1)."""
	test1 = isInHalfPlane(x, y, s60, -c60, -c60)
	test2 = isInHalfPlane(x, y, -s60, -c60, -c60)
	test3 = isInHalfPlane(x, y, 0.0, 1.0, minY)
	return test1 and test2 and test3

def pfTriangle(x, y):
	"""Painting function for the 'unit triangle', as described in 'isUnitTriangle'. Should be provided as argument for img_gen.MakeImage."""
	if isInUnitTriangle(x, y):
		return 255
	else:
		return 0

def pfTriad(x, y):
	"""Painting function for the triple triangle. Should be provided as argument for img_gen.MakeImage.""" 
	if not isInUnitTriangle(x, y):
		return 0
	if isInUnitTriangle(2.0 * x, -2.0 * y - 0.5):
		return 0
	return 255

if __name__ == "__main__":
	MakeShapes()