import re
from tkinter import messagebox


def rational(math_note):
    def find_num(a):
        res = re.split(r'[\+\-\*\/]', a)
        list_digit = [float(item) for item in res]
        return list_digit

    def find_oper(a):
        list_operate = ['+', '-', '/', '*']
        list_oper = []
        for i in a:
            if i in list_operate:
                list_oper.append(i)
        return list_oper

    def calculate(list_digit, list_oper):
        for n in range(len(list_digit)):
            i = 0
            while i < len(list_oper):
                if list_oper[i] == '*' or list_oper[i] == '/':
                    if list_oper[i] == '*':
                        list_digit[i] *= list_digit[i + 1]
                    if list_oper[i] == '/':
                        list_digit[i] /= list_digit[i + 1]
                    del list_digit[i + 1]
                    del list_oper[i]
                    i -= 1
                i += 1
            # i = 0
            # while i < len(list_oper):
            #     if list_oper[i] == '/':
            #         list_digit[i] /= list_digit[i + 1]
            #         del list_digit[i + 1]
            #         del list_oper[i]
            #     i+=1

            i = 0
            while i < len(list_oper):
                if list_oper[i] == '-':
                    list_digit[i] -= list_digit[i + 1]
                    del list_digit[i + 1]
                    del list_oper[i]
                i += 1
            i = 0
            while i < len(list_oper):
                if list_oper[i] == '+':
                    list_digit[i] += list_digit[i + 1]
                    del list_digit[i + 1]
                    del list_oper[i]
                i += 1
            return list_digit

    def calculate_in_brackets(a):
        for i in a:
            if i == '(':
                part = a[a.find("("):a.find(")") + 1]
                part = part[1:len(part) - 1]
                res = calculate(find_num(part), find_oper(part))
                a = a.replace(a[a.find("("):a.find(")") + 1], str(res[0]))
        return a

    def total_result(a):
        no_brackets = calculate_in_brackets(a)
        result = calculate(find_num(no_brackets), find_oper(no_brackets))
        # return print(f'{a} =', result)
        return result

    try:
        lost_note = total_result(math_note)
        return lost_note[0]

    except:
        messagebox.showerror('Error')
