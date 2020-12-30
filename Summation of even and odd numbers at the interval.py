print("""---------------------------
Find the summation of even and
odd numbers at the interval (a,b)
---------------------------""")
list=[]
list2 =[]
a =int(input("Enter a:"))
b =int(input("Enter b:"))

for i in range(a,b):
    if (i % 2 == 0):
        list.append(i)
    else:
        list2.append(i)
print("Summation of Even numbers:")
print(sum(list))
print("Summation of Odd numbers:")
print(sum(list2))