# database(having and keeping all datas), File(Datas save in this) = handle(open, read, write, close), Escapint = \, Enter = \n
# for, debugging File for spaces in for, ipython solving our problems, """"x""", fin(File Input)
# Usauly we doin mistake and we say is python fault but most to found our fault, Average, readline(), readlines(), mode("r". "w")
# cat, \t = tab
File = open("c:/users/persatech/desktop/seeme.txt")
print(File, type(File))
print(File.read())


File = open("c:/users/persatech/desktop/seeme.txt")
Counter = 0


for vibration in File:
    Counter += 1
    print(Counter, vibration)


print("This spaces in file is for spaces in text")
Enter = """Mohammad is the Hacker
"""
print(Enter)
print("this space is for space Enter key in codding")
print(Enter.strip())
print("This space gone by Enter.strip()")

fin = open("c:/users/persatech/desktop/seeme.txt")
Counter_2 = 0


for vibration in fin:
    vibration = vibration.strip()
    Counter_2 += int(vibration)
    print(vibration)


print("The sum Number is", Counter_2)


fin = open("c:/users/persatech/desktop/seeme.txt")
Counter_3 = 0
Sum = 0

for vibration in fin:
    vibration = vibration.strip()
    Counter_3 += 1
    Sum += int(vibration)
    Average = Sum / Counter_3


print("The average number of zero to nine is", Average)

fin = open("c:/users/persatech/desktop/seeme.txt")
print(fin.read())

fin = open("c:/users/persatech/desktop/seeme.txt")
print(fin.readline(1))

fin = open("c:/users/persatech/desktop/seeme.txt")
print(fin.readlines())

fin = open("c:/users/persatech/desktop/seeme.txt", "w")
print(fin)
Average = str(Average)

fin.write(Average)
fin.close()
