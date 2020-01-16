from password_generator import PasswordGenerator

def main():
	pwo = PasswordGenerator()
	pwo.minlen = 16 # (Optional)
	pwo.maxlen = 16 # (Optional)
	pwo.minuchars = 4 # (Optional)
	pwo.minlchars = 4 # (Optional)
	pwo.minnumbers = 8 # (Optional)
	pwo.minschars = 0 # (Optional)
	passwd = pwo.generate()

if __name__ == '__main__':
	main()