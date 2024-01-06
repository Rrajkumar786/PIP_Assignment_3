month = input('Enter the name of the month(First Letter should be capital): ')
Month = ["January","Febuary","March","April","May","June","July","August","September","October","November","December"]
days = [31,28,31,30,31,30,31,31,30,31,30,31]
Month[month] = days[Month]
print(Month)
