'''specify data individually'''
for num in [1,2,3,4,5]:
    print(num)

'''specify data's range'''
for num in range(10):
    print("num=" + str(num))
    print("num*num=" + str(num*num))

'''while: run n times until a defined condition is no longer met'''
count = 5
while count > 0:
    print(str(count))
    count -= 1

'''"break;": break the loop'''
while True:
    value = int(input("yen"))
    if value == 0:
        print("0 is inputted.")
        break;
    print(100 / value)

'''"continue": continue this loop'''
remain = 5
while remain > 0:
    print(str(remain))
    value = int(input("what?"))
    if value == 0:
        print("0 is inputted.")
        continue;
    print(100 /value)
    remain -= 1

    
'''output index and value from a list'''
city = ["Tokyo", "Beijing", "Hongkong", "Shenzhen"]
for i, c in enumerate(city):
    # string.format() function
    print("{}: {}".format(i, city[i]))

    
'''output from multiple list, use function zip()'''
city = ["Tokyo", "Beijing", "Shanghai", "hangzhou"]
code = [0, 1, 2, 3]

for i,j in zip(city, code):
    # because in loop, so (i, j) not (city, code)
    print("{}({})".format(i,j))
    
    
'''excetions'''
try:
    # run this code
    linux_interaction()
except AssertionError as error:
    # run this code when there is exception
    print(error)
else:
    # no exceptions? run this code
    try:
        with open('file.log') as file:
            read_data = file.read()
    except FileNotFoundError as fnf_error:
        print(fnf_error)
finally:
    # always run this code
    print('clean up')
    
# Example:    
for i in range(5):
    value = int(input("integer?"))
    try:
        print(100 / int(value))
    except ValueError:
        print("not integer")
        break
    except ZeroDivisionError:
        print("not 0")
        break
print("over")








    
    
