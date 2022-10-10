year = input("Enter a 4-digit year: ")
year = int(year)
if year%100 == 0:
    if year%400 == 0:
        print("Year " + str(year) + " is a leap year")
    else:
        print("Year " + str(year) + " is not a leap year")
elif year%4 == 0:
    print("Year " + str(year) + " is a leap year")
else:
    print("Yaer" + str(year) + " is not a leap year")
