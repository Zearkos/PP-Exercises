## I did this before but I also appreantly don't understand how to use git, and deleted all my work.

import datetime
today = datetime.date.today()
year = today.year

name = str(input("What is your name? "))
age = int(input("How old are you? "))

print (f"{name.capitalize()}, you will turn 100 in the year {year + (100-age)} (if you can live that long!)")