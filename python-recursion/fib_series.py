def gen_fib_series_rec(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return (gen_fib_series_rec(n-2) + gen_fib_series_rec(n-1))

if __name__ == "__main__":
    nums = int(input("Enter length of series to be generated: "))
    for n in range(0,nums):
        print(gen_fib_series_rec(n))