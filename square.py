# calc area

def calculate_area(side):
	return side ** 2

def calculate_perimeter(side):
	return 4 * side

side = int(input('Enter side size: '))

area = calculate_area(side)
perimeter = calculate_perimeter(side)


if __name__ == "__main__":
	print("Area ", area)
	print("Perimeter ", perimeter)