
Till = ([0, 0, 0, 0, 0, 0], [0, 0, 0, 0])
Tillnames = ([" 5c: ", "10c: ", "20c: ", "50c: ", " $1: ", " $2: "], [" $5: ", "$10: ", "$20: ", "$50: "])
Tillmultiplyer = ([0.05, 0.1, 0.2, 0.5, 1, 2], [5, 10, 20, 50])

comp = ([float, float, float])
compn = ("MYOB Cash totals?:      $", "MYOB EFTPOS totals?:    $", "EFTPOS machine totals?: $")

def advintinput(inputtext):
    x = input(inputtext)
    y = True
    while (x is not float) and (y == True):
        try:
            if (x == "/"):
                change()
                y = False
                if (inputtext == "Press any key to close window when done..... or enter / to make changes: "):
                    tt1 = sum(Till[0])+(sum(Till[1]))
                    tt2 = sum(Till[0])+(sum(Till[1]))-250
                    print()
                    print("Till total = $", round((tt1),3))
                    print("Till takings = $ ", round((tt2),3))
                    finish(tt2)
                return (advintinput(inputtext))
            elif ((x == "")and(inputtext=="Press any key to close window when done..... or enter / to make changes: ")):
                exit()
            else:
                x = float(x)
                y = False
                return float(x)
        except ValueError:
            print("Wrong Entry, Please enter a number....")
            return (advintinput(inputtext))


def intinput(inputtext):
    x = input(inputtext)
    y = True
    while (x is not int) and (y == True):
        try:
            x = int(x)
            y = False
            return int(x)
        except ValueError:
            print("Wrong Entry, Please enter a number....")
            y = False
            return (intinput(inputtext))
    if (x is int):
        return int(x)

def floatinput(inputtext):
    x = input(inputtext)
    y = True
    while (x is not float) and (y == True):
        try:
            x = float(x)
            y = False
            return float(x)
        except ValueError:
            print("Wrong Entry, Please enter a number....")
            y = False
            return (intinput(inputtext))
    if (x is float):
        return float(x)

def change():
    print()
    print("What would you like to change?")
    print("Please enter the ID of the Selection (From 1 - 10)")
    print("----------------------------------------")
    print(" 1: 5c  = ", int(((Till[0][0])/Tillmultiplyer[0][0])))
    print(" 2: 10c = ", int(((Till[0][1])/Tillmultiplyer[0][1])))
    print(" 3: 20c = ", int(((Till[0][2])/Tillmultiplyer[0][2])))
    print(" 4: 50c = ", int(((Till[0][3])/Tillmultiplyer[0][3])))
    print(" 5: $1  = ", int(((Till[0][4])/Tillmultiplyer[0][4])))
    print(" 6: $2  = ", int(((Till[0][5])/Tillmultiplyer[0][5])))
    print()
    print(" 7: $5  = ", int(((Till[1][0])/Tillmultiplyer[1][0])))
    print(" 8: $10 = ", int(((Till[1][1])/Tillmultiplyer[1][1])))
    print(" 9: $20 = ", int(((Till[1][2])/Tillmultiplyer[1][2])))
    print("10: $50 = ", int(((Till[1][3])/Tillmultiplyer[1][3])))
    print("----------------------------------------")

    d = True
    while d == True:
        x = intinput(": ")
        if (x >=1 and x<=6):
            Till[0][x-1] = (floatinput("What did you want to change it to?: "))*Tillmultiplyer[0][x-1]
            print("----------------------------------------")
            print()
            print(Tillnames[0][x-1], round(((Till[0][x-1])/Tillmultiplyer[0][x-1]), 3), " (Change Successful)")
            d = False
        elif (x >=7 and x<=10):
            Till[1][x-7] = (floatinput("What did you want to change it to?: "))*Tillmultiplyer[1][x-7]
            print("----------------------------------------")
            print()
            print(Tillnames[1][x-7], round(((Till[1][x-7])/Tillmultiplyer[1][x-7]), 3), " (Change Successful)")
            d = False
        else:
            print("Wrong Selection, please choose a number from 1 - 10")
            d = False
            d = True
        

def comptotals():
    print()
    print("Please input the following then press enter.... ")
    print()

    x = True
    i = 0
    while (x == True):
        comp[i] = advintinput(compn[i])

        if (i < 2):
             i+=1
        else:
            x = False
            Tillf()
    
def Tillf():
    print()
    print("Enter quanity of each coin and note, then press enter....")
    print("(Tip: Enter / if you make a mistake and want to change somthing)")
    print()
    x = True
    i = 0
    level = 0
    while (x == True):
        try:
            Till[level][i] = advintinput(Tillnames[level][i])*Tillmultiplyer[level][i]
            i += 1
            if (i > 5) or (level == 1):
                level = 1
                if (i > 5):
                    i = 0
                    print("Coin totals = $", round(sum(Till[0]),3))
                    print()
                if ((i > 3) and (level == 1)):
                    x = False
                    tt1 = sum(Till[0])+(sum(Till[1]))
                    tt2 = sum(Till[0])+(sum(Till[1]))-250
                    print("Till total = $", round((tt1),3))
                    print("Till takings = $ ", round((tt2),3))
                    finish(tt2)
            else:
                x = True

        except ValueError:
            print("Wrong Entry, Please enter a number....")

def finish(tt2):
    print()
    print("----------------------------------------")
    print("Till is up by $", round((tt2-comp[0]), 3))
    print("----------------------------------------")
    print("EFT machine is up by $", round((comp[2] - comp[1]), 3))
    print("----------------------------------------")
    print()


comptotals()

advintinput("Press any key to close window when done..... or enter / to make changes: ")



    









