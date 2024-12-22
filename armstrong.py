# Assisted by watsonx Code Assistant 
def is_armstrong_number(num):
    n = len(str(num))
    sum = 0
    temp = num
    while temp > 0:
        digit = temp % 10
        sum += digit ** n
        temp //= 10
    return sum == num

n = int(input("Enter the number of digits in the armstrong number: "))
start = 10 ** (n - 1)
end = 10 ** n

for i in range(start, end):
    if is_armstrong_number(i):
        print(i)
