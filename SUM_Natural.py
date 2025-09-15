num=int(input("Enter a number: "))
sum=0
if num < 0:
    print("Sum is not defined for negative numbers")
else:
    for i in range(1, num + 1):
        sum += i
    print(f"Sum of first {num} natural numbers is {sum}");