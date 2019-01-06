# Write a program that prints the next 20 leap years.
# Need to know current year - input required. 
    #Evaluate if current year is leap year. If not, update year +1, evaluate if leap year, if it is: year +4 = next leap year. Start loop for next 20 leap years.
# Need to calculate the next leap year; occurs every 4 years:
# If the year is evenly divisible by 4, go to step 2. ... if year % 4==0. True
# If the year is evenly divisible by 100, go to step 3. ...if year % 100==0. True
# If the year is evenly divisible by 400, go to step 4. ...if year % 400==0. True
# Update the leap year 20 times; range(20): print(year)
import datetime
#year = int(datetime.datetime.now().year)
year = 2021
leap = 0
while leap != year:
    if year % 4==0 and year % 100!=0: 
        leap = year
    elif year % 4==0 and year % 100==0 and year % 400==0:
        leap = year
    elif year % 4!=0:
        year=year+1
        print(year)
        continue
for yr in range(20):
    print("Next leap year is: ", leap)
    leap = leap+4               ## years are not checked in this loop. If range was higher some years % 400!=0 and therefore not be leap years. 



# Simple leap year
#try:
   # leap = int(input("Enter the last leap year: "))
    #if leap!= 2016:
      #  quit()
   # for year in range(20):
      #  leap = leap +4
      #  print("Next leap year is: ",leap)
#except:
   # print('No go.')
