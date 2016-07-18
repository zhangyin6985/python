#input()返回的是str,不能直接和数字比较
#birth = input('birth:')

age = input('birth:')
birth=int(age)

if birth < 2000:
    print("old man!")
else:
    print("young boy!")
