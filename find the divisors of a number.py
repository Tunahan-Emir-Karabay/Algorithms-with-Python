print("""-----------------------
Find divisors of a number
-----------------------""")
def find_divisors(number):
    list_ofdiv=[]
    for i in range(1,number+1):
        if (number % i == 0):
            list_ofdiv.append(i)
    return list_ofdiv

while True:
    number=int(input("Enter a number:"))
    if (number == "q"):
        print("Exiting the system..")
        break
    else:
        print("Divisors of number:")
        print(find_divisors(number))
    break


