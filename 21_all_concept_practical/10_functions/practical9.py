# Task:
    # 1. add_numbers(*args) naam ka function banao.
    # 2. Function ke andar args mein milne wale sabhi numbers ka total calculate karke return karo.
    # 3. Function ko 10, 20, 30, 40 arguments ke saath call karo.
    # 4. Returned total ko print karo.
# Expected output:
    # 100

def add_numbers(*args):
    return sum(args)

print(add_numbers(10, 20, 30, 40))
