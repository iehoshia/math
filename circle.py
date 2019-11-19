# calc area
from math import pi

def calculate_area(ratio):
	return pi * ratio ** 2

def calculate_perimeter(ratio):
	return 2 * pi * ratio

if __name__ == "__main__":
	ratio = int(input('Enter ratio: '))

	area = calculate_area(ratio)
	perimeter = calculate_perimeter(ratio)

	print("Area ", area)
	print("Perimeter ", perimeter)