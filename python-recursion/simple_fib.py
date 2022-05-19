def simple_fib(n):
    first = 0
    second = 1
    sum = 0
    count = 1
    while (count<=n):
        print(sum)
        count += 1
        first = second
        second = sum
        sum = first + second

n = int(input("Enter number: "))
simple_fib(n)