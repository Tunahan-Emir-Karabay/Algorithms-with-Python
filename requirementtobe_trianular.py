print("""*********************************************
Find out if there is a triangle by looking at the sides
*********************************************""")
import time
while True:
    a=int(input("a:"))
    b=int(input("b:"))
    c=int(input("c:"))
    x = a+c
    y = a-c
    if b < x and b > abs(y):
        print("Checking...")
        time.sleep(1)
        print("There is a trinagular that have these sides.")
    else:
        print("Checking...")
        time.sleep(1)
        print("There isn't a trinagular that have these sides.")
    break
