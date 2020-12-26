import random
import time
print("""*********************

NUMBER PREDİCTİON GAME

Find number 1 to 50 


************************""")
random_number =random.randint(1,50)
rightof_estimate =6
while True:
    estimate =int(input("Your Forecast:"))
    if (estimate < random_number):
        print("Checking...")
        time.sleep(1)
        print("Enter the number that is larger than your forecast")
        rightof_estimate -=1
    elif (estimate > random_number):
        print("Checking...")
        time.sleep(1)
        print("Enter the number that is smaller than your forecast")
        random_number -=1
    else:
        print("Checking...")
        time.sleep(1)
        print("Congratulations number is",random_number)
        break
    if (rightof_estimate == 0):
        print("Fail")
        print("Number is",random_number)
        break