# 0,1,1,2,3,5,8,13,21,34

def generate_fibonacci(n):
    if n <= 0:
        print("Incorrect number.")
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return generate_fibonacci(n-1) + generate_fibonacci(n-2) 

if __name__ == '__main__':
    num = int(input("Enter the number: "))
    print(generate_fibonacci(num))