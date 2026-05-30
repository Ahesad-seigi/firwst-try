def get_numbers():
    a = int(input('请输入第一个数字：'))
    b = int(input('请输入第二个数字：'))
    return a, b

def choose_fuhao():
    c = input('请输入符号 (+, -, *, /)：')
    return c

def calculate():
    a, b = get_numbers()
    c = choose_fuhao()
    if c == '+':
        return a + b
    elif c == '-':
        return a - b
    elif c == '*':
        return a * b
    elif c == '/':
        if b == 0:
            return "除数不能为0哦！"
        return a / b
    else:
        return "输入的符号不认识哦！"

print("计算结果是：", calculate())