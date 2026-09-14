year = input("Enter a year: ")
year = int(year)

if year % 4 == 0:
	if year % 100 == 0:
		if year % 400 != 0:
			print("Not a leap year!")
		else: # year % 4 == 0
			print("It is a leap year!")
	else: # year % 100 != 0
		print("It is a leap year!")
else: # year % 4 != 0
	print("Not a leap year!")