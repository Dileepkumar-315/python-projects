def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
def div(a,b):
    return a/b



operations_dict={
    '+':add,
    '-': sub,
    '*': mul,
    '/':div
}
def calculator():
    n1 = int(input("enter first number:"))
    for i in operations_dict:
        print(i)
    flag = True
    while flag:
        op = input("pick an operation:")
        n2 = int(input("enter next number:"))
        cal_fun = operations_dict[op]
        result = cal_fun(n1, n2)
        print(f"{n1} {op} {n2}={result}")
        further = input(f"enter 'y' to continue calculation with {result} or 'n' to start new calculation or 'x' to end the calculation:").lower()
        if further == 'y':
            n1 = result
        elif further == 'n':
            flag=False
            calculator()
        else:
            exit()

calculator()
