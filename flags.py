from img_gen import MakeImage

def MakeFlags():
	MakeEnglishFlag()
	MakeCatalanFlag()
	MakeSpanishFlag()
	MakeSwedishFlag()
	MakeNorwegianFlag()
	MakeFrenchFlag()

def MakeEnglishFlag():
	MakeImage(pfEnglish, "en")

def MakeCatalanFlag():
	MakeImage(pfCatalan, "ca")

def MakeSpanishFlag():
	MakeImage(pfSpanish, "es")

def MakeSwedishFlag():
	MakeImage(pfSwedish, "se")

def MakeNorwegianFlag():
	MakeImage(pfNorwegian, "no")

def MakeFrenchFlag():
	MakeImage(pfFrench, "fr")

def pfEnglish(x, y):
	l2 = (x * x + y * y)
	if l2 > 1:
		return (0, 0, 0, 0)
	
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

def pfCatalan(x, y):
	l2 = (x * x + y * y)
	if l2 > 1:
		return (0, 0, 0, 0)

	u = (x + 1.0) / 2.0
	sign = (u * 9) % 2
	if sign < 1:
		return (255, 255, 70, 255)

	return (220, 80, 50, 255)

def pfSpanish(x, y):
	l2 = (x * x + y * y)
	if l2 > 1:
		return (0, 0, 0, 0)

	if abs(y) < 0.5:
		return (250, 250, 60, 255)

	return (250, 70, 60, 255)

def pfSwedish(x, y):
	l2 = (x * x + y * y)
	if l2 > 1:
		return (0, 0, 0, 0)
	
	if abs(x + 0.25) < 0.2 or abs(y) < 0.2:
		return (255, 255, 60, 255)
	
	return (80, 80, 255, 255)

def pfNorwegian(x, y):
	l2 = (x * x + y * y)
	if l2 > 1:
		return (0, 0, 0, 0)
	
	xx = x + 0.25
	if abs(xx) < 0.15 or abs(y) < 0.15:
		return (30, 30, 255, 255)
	if abs(xx) < 0.25 or abs(y) < 0.25:
		return (255, 255, 255, 255)
	
	return (255, 70, 70, 255)

def pfFrench(x, y):
	l2 = (x * x + y * y)
	if l2 > 1:
		return (0, 0, 0, 0)
	
	if x < -1.0 / 3.0:
		return (40, 30, 250, 255)
	if x > +1.0 / 3.0:
		return (250, 40, 50, 255)
	
	return (255, 255, 255, 255)

if __name__ == "__main__":
	MakeFlags()