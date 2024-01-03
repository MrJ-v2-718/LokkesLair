import codecs

def main():
	# Encode and decode ROT13, but beware the Ides of March
	print("Welcome to the ROT13 converter.")
	to_convert = input("Please enter a sequence to convert: ")
	to_convert = codecs.encode(to_convert, 'rot_13')
	print(to_convert)
main()

