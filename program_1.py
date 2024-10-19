# Program #1: Rainfall
# Design a program that lets the user enter the total rainfall for each of 12 months into a list.
# The program should calculate and display the total rainfall for the year,
# the average monthly rainfall, # and the months with the highest and lowest amounts.
import statistics
def rainfall():
    total = 1
    monthly_rain = []
    while total<= 12:
        months = int(input("enter monthly rain: "))
        monthly_rain.append(months)
        total = total+1
    total_rain = (sum(monthly_rain))
    average_rain = round(total_rain/(len(monthly_rain)),2)
    most_rain = max(monthly_rain)
    least_rain = min(monthly_rain)
    print("The total rain was "+str(total_rain)+" inches")
    print("The average rain was "+str(average_rain)+" inches")
    print("The most rain in one month was "+str(most_rain)+" inches")
    print("The least rain in one month was "+str(least_rain)+" inches")
rainfall()
