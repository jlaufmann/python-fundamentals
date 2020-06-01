'''
Write a program with 3 functions. Each function must call
at least one other function and use the return value to do something.

'''

def useless1(s1):
    capped = s1.upper()
    print(f"UPPERCASE TEXT: {capped}")
    return capped

def useless2(s2):
    s2list = list(s2)
    s2listsorted = sorted(s2list)
    s2sorted = ''.join(s2listsorted)
    print(f"Other text: {s2sorted}")
    return len(s2sorted)

def useless3(num3):
    res3 = 1
    for i in range(num3):
        res3 += i
    print(f"{res3} is not a magic number today")
    return res3

text_input = input("Enter some text: ")
useless3(useless2(useless1(text_input)))
