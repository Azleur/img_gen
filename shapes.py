import math
from img_gen import MakeImage

def MakeShapes():
	MakeBullseye()
	MakeSpiral()

def MakeBullseye():
	MakeImage(pfBullseye, name="bullseye", size=64, channels="L")

def MakeSpiral():
	MakeImage(pfSpiral, name="spiral", size=128, channels="L")

def pfBullseye(x, y):
	l = math.sqrt(x * x + y * y)
	if l > 1:
		return 0
	if l > 0.8:
		return 255
	if l > 0.5:
		return 0
	return 255

def pfSpiral(x, y):
	l = math.sqrt(x * x + y * y)
	t = math.atan2(y, x)
	A = math.cos(0.5 * t + 6 * l)
	A = A * A
	return int(255 * A)

if __name__ == "__main__":
	MakeShapes()