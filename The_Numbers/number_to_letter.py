continue_decoding = "y"

while continue_decoding == "y":
	outfile = open("NumberToLetter.txt","a")
	number_to_decode = input("Please enter a number to decode: ")
	
	if number_to_decode == "1":
		outfile.write("a")
	elif number_to_decode == "2":
		outfile.write("b")
	elif number_to_decode == "3":
		outfile.write("c")
	elif number_to_decode == "4":
		outfile.write("d")
	elif number_to_decode == "5":
		outfile.write("e")
	elif number_to_decode == "6":
		outfile.write("f")
	elif number_to_decode == "7":
		outfile.write("g")
	elif number_to_decode == "8":
		outfile.write("h")
	elif number_to_decode == "9":
		outfile.write("i")
	elif number_to_decode == "10":
		outfile.write("j")
	elif number_to_decode == "11":
		outfile.write("k")
	elif number_to_decode == "12":
		outfile.write("l")
	elif number_to_decode == "13":
		outfile.write("m")
	elif number_to_decode == "14":
		outfile.write("n")
	elif number_to_decode == "15":
		outfile.write("o")
	elif number_to_decode == "16":
		outfile.write("p")
	elif number_to_decode == "17":
		outfile.write("q")
	elif number_to_decode == "18":
		outfile.write("r")
	elif number_to_decode == "19":
		outfile.write("s")
	elif number_to_decode == "20":
		outfile.write("t")
	elif number_to_decode == "21":
		outfile.write("u")
	elif number_to_decode == "22":
		outfile.write("v")
	elif number_to_decode == "23":
		outfile.write("w")
	elif number_to_decode == "24":
		outfile.write("x")
	elif number_to_decode == "25":
		outfile.write("y")
	elif number_to_decode == "26":
		outfile.write("z")
	else:
		print("Error")
	
	outfile.close()

	continue_decoding = input("Would you like to continue decoding? (y/n) ")

