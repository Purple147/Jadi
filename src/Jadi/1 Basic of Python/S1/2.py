# Itterations(for), (). [], {}, Petterns(Like x += 1)
for room in range(47):
    if room % 2 == 0:
        print(room, room**room)
        if room**room > 741**741:
            break


List = ["Hacker", "Programmer", "Robot", "147"]


Count = -1
for Mohammad in List:
    Count += 1
    print(Count, "Hello", Mohammad)

Number = input("Give me your Number: ")
RealNumber = int(Number)
Number_Counts = 0
Number_Sum = 0
Number_Average = 0


while RealNumber != -1:
    Number_Counts += 1
    Number_Sum += RealNumber
    Number_Average = Number_Sum / Number_Counts
    Number = input("Give me your Number: ")
    RealNumber = int(Number)
    if RealNumber == -1:
        print(Number_Counts, Number_Sum, Number_Average)
