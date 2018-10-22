"""Example use for img_gen: create country flags programmatically."""
import math
import img_gen

def pfTricolor(x, y, rgb1, rgb2, rgb3, horizontal=False):
	"""Create tricolor flags, either horizontal or vertical."""
	if horizontal:
		x = -y
	if x < -1.0 / 3.0:
		return rgb1 + (255,)
	if x < +1.0 / 3.0:
		return rgb2 + (255,)
	return rgb3 + (255,)

def MakeFlags():
	"""Make all the flags (9 total). Saves them in the working directory as PNG files."""
	MakeBritishFlag()
	MakeCatalanFlag()
	MakeSpanishFlag()
	MakeSwedishFlag()
	MakeNorwegianFlag()
	MakeFrenchFlag()
	MakeItalianFlag()
	MakeRussianFlag()
	MakeGreekFlag()

def MakeBritishFlag():
	"""Make the Union Jack (simplified). Saves it in the working directory as a PNG file."""
	img_gen.MakeImage(pfBritish, "en")

def MakeCatalanFlag():
	"""Make the Catalan flag. Saves it in the working directory as a PNG file."""
	img_gen.MakeImage(pfCatalan, "ca")

def MakeSpanishFlag():
	"""Make the Spanish flag (without shield). Saves it in the working directory as a PNG file."""
	img_gen.MakeImage(pfSpanish, "es")

def MakeSwedishFlag():
	"""Make the Swedish flag. Saves it in the working directory as a PNG file."""
	img_gen.MakeImage(pfSwedish, "se")

def MakeNorwegianFlag():
	"""Make the Norwegian flag. Saves it in the working directory as a PNG file."""
	img_gen.MakeImage(pfNorwegian, "no")

def MakeFrenchFlag():
	"""Make the French flag. Saves it in the working directory as a PNG file."""
	img_gen.MakeImage(pfFrench, "fr")

def MakeItalianFlag():
	"""Make the Italian flag. Saves it in the working directory as a PNG file."""
	img_gen.MakeImage(pfItalian, "it")

def MakeRussianFlag():
	"""Make the Russian flag. Saves it in the working directory as a PNG file."""
	img_gen.MakeImage(pfRussian, "ru")

def MakeGreekFlag():
	"""Make the Greek flag. Saves it in the working directory as a PNG file."""
	img_gen.MakeImage(pfGreek, "gr")

@img_gen.circleCutout()
def pfBritish(x, y):
	"""Paint function for the Union Jack (simplified). Should be provided as argument for img_gen.MakeImage."""
	if abs(x) < 0.15 or abs(y) < 0.15:
		return (255, 60, 60, 255)
	if abs(x) < 0.25 or abs(y) < 0.25:
		return (255, 255, 255, 255)
	
	u = (x + y) / 2.0
	v = (x - y) / 2.0
	if abs(u) < 0.08 or abs(v) < 0.08:
		return (255, 60, 60, 255)
	if abs(u) < 0.14 or abs(v) < 0.14:
		return (255, 255, 255, 255)
	
	return (50, 50, 220, 255)

@img_gen.circleCutout()
def pfCatalan(x, y):
	"""Paint function for the Catalan flag. Should be provided as argument for img_gen.MakeImage."""
	u = (x + 1.0) / 2.0
	sign = (u * 9) % 2
	if sign < 1:
		return (255, 255, 70, 255)

	return (220, 80, 50, 255)

@img_gen.circleCutout()
def pfSpanish(x, y):
	"""Paint function for the Spanish flag (without shield). Should be provided as argument for img_gen.MakeImage."""
	if abs(y) < 0.5:
		return (250, 250, 60, 255)

	return (250, 70, 60, 255)

@img_gen.circleCutout()
def pfSwedish(x, y):
	"""Paint function for the Swedish flag. Should be provided as argument for img_gen.MakeImage."""
	if abs(x + 0.25) < 0.2 or abs(y) < 0.2:
		return (255, 255, 60, 255)
	
	return (80, 80, 255, 255)

@img_gen.circleCutout()
def pfNorwegian(x, y):
	"""Paint function for the Norwegian flag. Should be provided as argument for img_gen.MakeImage."""
	xx = x + 0.25
	if abs(xx) < 0.15 or abs(y) < 0.15:
		return (30, 30, 255, 255)
	if abs(xx) < 0.25 or abs(y) < 0.25:
		return (255, 255, 255, 255)
	
	return (255, 70, 70, 255)

@img_gen.circleCutout()
def pfFrench(x, y):
	"""Paint function for the French flag. Should be provided as argument for img_gen.MakeImage."""
	return pfTricolor(x, y, (40, 30, 250), (255, 255, 255), (250, 40, 50))

@img_gen.circleCutout()
def pfItalian(x, y):
	"""Paint function for the French flag. Should be provided as argument for img_gen.MakeImage."""
	return pfTricolor(x, y, (50, 220, 80), (255, 255, 255), (240, 40, 45))

@img_gen.circleCutout()
def pfRussian(x, y):
	"""Paint function for the Russian flag. Should be provided as argument for img_gen.MakeImage."""
	return pfTricolor(x, y, (255, 255, 255), (30, 25, 240), (240, 30, 40), horizontal=True)

@img_gen.circleCutout()
def pfGreek(x, y):
	"""Paint function for the Greek flag. Should be provided as argument for img_gen.MakeImage."""
	white = (255, 255, 255, 255)
	blue = (20, 40, 200, 255)
	# Remap x,y from -1..+1 to 0..9 and reverse y.
	x = (x + 1.0) * 4.5
	y = (1.0 - y) * 4.5
	
	if x < 5 and y < 5:
		if math.floor(x) == 2 or math.floor(y) == 2:
			return white
		else:
			return blue
	else:
		if (y % 2) < 1:
			return blue
		else:
			return white

if __name__ == "__main__":
	MakeFlags()