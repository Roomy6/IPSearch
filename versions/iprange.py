ip = input ("Enter the IP: ")
splitip = ip.split(".") # remove the '.' from ip

print (splitip)

dot = "."

startNum = int(input("Start number (1 - 255): "))
#split1 = int(input("Enter first max range: "))
#split2 = int(input("Enter second max range: "))
#split3 = int(input("Enter third max range: "))
#split4 = int(input("Enter fourth max range: "))

# I have no idea what i am doing lol
# im just trying to learn here

while True:
    for a in range(startNum, 255 + 1):
        #print(str(a) + dot + str(a) + dot + str(a) + dot + str(a))
        print(splitip[0] + dot + splitip[1] + dot + splitip[2] + dot + str(a))

        if a == 255:
            for b in range(startNum, 255 + 1):
                print(splitip[0] + dot + splitip[1] + dot + str(b) + dot + splitip[3])
