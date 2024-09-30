import time

my_time=int(input("Enter the time in seconds :"))

if my_time>0:
    for x in range(my_time,0,-1):
        seconds = x % 60
        minutes = int(x/60)%60
        hours = int(x/3600)
        print(f"{hours:02}:{minutes:02}:{seconds:02}")
        time.sleep(1)
else:
    print("Invalid Operation")
    if my_time==0:
        print("The time is already Zero.")
    elif my_time<0:
        print("You can't go in past")
    # else:
        # print("Only Whole Positive Integers allowed")

print("TIME'S UP!!") 
