# calc area
def calculate_area(sidea, sideb):
	return sidea * sideb

def calculate_perimeter(sidea, sideb):
	return 2 * sidea + 2 sideb

if __name__ == "__main__":
	sidea = int(input('Enter side A: '))
	sideb = int(input('Enter side B'))

	area = calculate_area(sidea, sideb)
	perimeter = calculate_perimeter(sidea, sideb)

	print("Area ", area)
	print("Perimeter ", perimeter)