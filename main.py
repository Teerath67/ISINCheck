import os

codesFile = open("Isincode.txt")
codes = codesFile.readlines()

values = { 'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15, 'G': 16, 'H': 17, 'I': 18, 'J': 19, 'K': 20, 'L': 21, 'M': 22, 'N': 23, 'O': 24, 'P': 25, 'Q': 26, 'R': 27, 'S': 28, 'T': 29, 'U': 30, 'V': 31, 'W': 32, 'X': 33, 'Y': 34, 'Z': 35 }


for code in codes:
    actCode = code.replace(' ', '').replace("\n", '')

    if (len(actCode) == 12):
        verificationDigit = int(actCode[11])

        otherChars = actCode[0:11]

        step1 = []

        for char in otherChars:
            if char.isdigit():
                step1.append(int(char))
            else:
                step1.append(int(str(values[char])[0]))
                step1.append(int(str(values[char])[1]))

        mult = [1, 2]
        step = 1
        step2 = []

        for number in reversed(step1):
            step2.append(number * mult[step % 2])
            step += 1

        step3 = []

        for number in reversed(step2):
            if number >= 10:
                step3.append(int(str(number)[0]))
                step3.append(int(str(number)[1]))
            else:
                step3.append(number)
        
        somme = sum(step3)
        gettenth = (int(str(somme)[0]) + 1) * 10

        if (somme % 10 == 0):
            finalNumber = 0
        else:
            finalNumber = gettenth - somme
        

        if finalNumber == verificationDigit:
            print("Le code ISIN " + actCode + " est valide !")
        else: 
            print("Le code ISIN " + actCode + " n'est pas valide !")

    else:
        print("Le code n'est pas valide !")
