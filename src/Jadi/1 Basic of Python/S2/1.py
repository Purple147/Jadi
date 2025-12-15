# Strings, Classes(Metodes), upper, dir(), lower(), count(), find(), strip(), startswith(), %s/f/i
Mohammad = "Purple147"
print("a" in Mohammad)
print(Mohammad == "Hacker")
print(Mohammad == "Purple14")
print("A" < "Z")
print("a" > "A")
print(Mohammad > "Hacker")
print(Mohammad.upper())
print(dir(Mohammad))
print(Mohammad.zfill(3), Mohammad.capitalize())
help(str.__add__)
print(Mohammad, Mohammad.lower())
print(Mohammad.find("l"))
print("Mohammad is a Hacker".find("a", 4))
print("   Start to Game   ".strip())
print(Mohammad.startswith("H"))
print(Mohammad.startswith("P"))
print(Mohammad.startswith("Pur"))
important_things_in_Strings = Mohammad.lower().upper().strip().find("p")
print(important_things_in_Strings)
randomate = "My age is %i and i'm very happy" % 47
print(randomate)
randomate_2 = "i thinkink about %s and this is %s becouse my number is %i" % (
    "Possy",
    "Fuckness",
    98901,
)
print(randomate_2)
