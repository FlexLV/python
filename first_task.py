from datetime import date

name = "Ernests"
current_date = date.today()
year = current_date.year
birthyear = 2004
age = year - birthyear

print("Hi, I am " + name + " and I am " + str(age) + " years old")
