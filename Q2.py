# It is commonly said that one human year is equivalent to 7 dog years. However, this simple conversion
# must recognize that dogs reach adulthood in approximately two years. As a result, some people
# believe that it is better to count each of the first two human years as 10.5 dog years and then count
# each additional human year as 4 dog years. Write a program that implements the conversion from
# human to dog years described in the previous paragraph. Ensure that your program works correctly
# for conversions of less than two human years and conversions of two or more human years. Your
# program should display an appropriate error message if the user enters a negative number.

human_1yr = 7 #dog years
dogs_adult = 2 #years
human_2yr_count = 10.5 #years
additional_human_yr = 4 #years
age = int(input('Enter the age: '))
if (age == 1):
    print(human_1yr)
elif(age>1 and age<=2):
    print(human_2yr_count)
elif(age>2):
    print(human_2yr_count+(age*additional_human_yr))
else:
    print('Error, Age cannot be negative')
