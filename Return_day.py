# '''
# return_day(1) # "Sunday"
# return_day(2) # "Monday"
# return_day(3) # "Tuesday"
# return_day(4) # "Wednesday"
# return_day(5) # "Thursday"
# return_day(6) # "Friday"
# return_day(7) # "Saturday"
# return_day(41) # None
# '''
# def return_day():
#     pass
#
import random

num = random.randint(1,7)  # numbers 1 - 7

def return_day(num):
    days = ["Sunday","Monday", "Tuesday","Wednesday","Thursday","Friday","Saturday"]
    # Check to see if num valid
    if num > 0 and num <= len(days):
        # use num - 1 because lists start at 0 
        return days[num-1]
    return None
print(f"Numer {num} refers to {return_day(num)}")

    # print(f"{index}: {colors[index]}")