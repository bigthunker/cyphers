import math

alpha = ["a","b","c",'d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
strSpecial = "ab cd ef "
#alphabet
cryptArray = []
cryptNumerical = []
cryptNumChange = []
finalwordArray = []
finalString = ""  
index = 0
checkInput = True

spaceCheck = False
spaceArray = []
spacePosition = []

rawWord = ""
changeNum = 0

crypTypeRaw = input("Would you like to decrypt or encrypt a word?\n")
crypType = crypTypeRaw.lower() #making the variable, cryptoTypeRaw, lowercase


def check():

    global crypTypeRaw
    global crypType
    global index
    global spaceArray
    global spacePosition
    global strSpecial

    rawWord = input("What word would you like to encrypt?\n")
    changeNum = input("How many spaces would you like to move it?\n")

    index = 0
    print(rawWord)
    for i in rawWord:
        
        cryptArray.append(rawWord[index])
        print(cryptArray)
        #putting individual letters into the decrypt array and making them lowercase
        index+=1

        #turn letters into numbers
        print(spaceArray)
    
        for i in cryptArray:
            checkInput = False
            index = 0

            while checkInput == False: 
                if i == alpha[index]:
                    cryptNumerical.append(index)
                    checkInput = True
                elif i == " ":
                    spacePosition.append(index)
                    index+=1
                else: 
                    index += 1

    

def intro():
    
    global crypTypeRaw
    global crypType
    if (crypType != "encrypt" and crypType != "decrypt" and crypType != "all"):
        checkInput = False
        print("Please type encrypt or decrypt") #making sure they type encrypt or decrypt
        
        while (checkInput == False):
            crypTypeRaw = input("Would you like to decrypt or encrypt a word?\n")
            crypType = crypTypeRaw.lower()
            if (crypType == "encrypt" or crypType == "decrypt" or crypType == "all"):
                checkInput = True
            else:
                print("Please type encrypt or decrypt")

    else:
        checkInput = True

def encrypt():
    global cryptArray
    global cryptNumerical
    global cryptNumChange
    global index
    global finalString

    rawWord = input("What word would you like to encrypt?\n")
    changeNum = input("How many spaces would you like to move it?\n")
    for i in rawWord:
        cryptArray.append(rawWord[index].lower())
        #putting individual letters into the decrypt array and making them lowercase
        index+=1

    #turn letters into numbers

    for i in cryptArray:
        checkInput = False
        index = 0

        while checkInput == False:
            if i == alpha[index]:
                cryptNumerical.append(index)
                checkInput = True
            else: 
                index += 1

     

    changeInt = int(changeNum)

    

    for i in cryptNumerical:
        if (i+changeInt > 25):
            modNumber = changeInt%26
            if (i+modNumber)>25 :
                cryptNumChange.append((i+modNumber)-26)
            else:
                cryptNumChange.append((i+modNumber))
            
        else:
            cryptNumChange.append(i+changeInt)

    
    
    for i in cryptNumChange:
        finalwordArray.append(alpha[i])
    
    
    for i in finalwordArray:
        finalString += i
    
    print(f'Your encrypted word is {finalString}')

def decrypt():
    global cryptArray
    global cryptNumerical
    global cryptNumChange
    global index
    global finalString

    rawWord = input("What word would you like to decrypt?\n")
    changeNum = input("How many spaces would you like to move it?\n")
    for i in rawWord:
        cryptArray.append(rawWord[index].lower())
        #putting individual letters into the decrypt array and making them lowercase
        index+=1

    #turn letters into numbers

    for i in cryptArray:
        checkInput = False
        index = 0

        while checkInput == False:
            if i == alpha[index]:
                cryptNumerical.append(index)
                checkInput = True
            else: 
                index += 1

      

    changeInt = int(changeNum)

    

    for i in cryptNumerical:
        if ((i-changeInt) < 0):
            modNumber = (changeInt%26)
            if (i-modNumber)< 0 :
                cryptNumChange.append((i-modNumber)+26)
            else:
                cryptNumChange.append((i-modNumber))
        else:
            cryptNumChange.append(i-changeInt)

    
    
    
    for i in cryptNumChange:
        finalwordArray.append(alpha[i])
    
    
    for i in finalwordArray:
        finalString += i
    
    print(f'Your decrypted word is {finalString}')

def all():
    global cryptArray
    global cryptNumerical
    global cryptNumChange
    global index
    global finalString

    rawWord = input("What word would you like to encrypt?\n")
    for i in rawWord:
        cryptArray.append(rawWord[index].lower())
        #putting individual letters into the decrypt array and making them lowercase
        index+=1    
    
    for i in cryptArray:
        checkInput = False
        index = 0

        while checkInput == False:
            if i == alpha[index]:
                cryptNumerical.append(index)
                checkInput = True
            else: 
                index += 1
    print(cryptNumerical)

    #numerical versions of letters are in cryptNumerical 

    checkInput = False
    index = 1


    while checkInput == False: 

        print("Every possible option:\n")

        for t in range(1,26):
            
            changeInt = index
            cryptNumChange = []
            finalwordArray=[]
            finalString = ""

            for i in cryptNumerical:
                if (i+index > 25):
                    modNumber = changeInt%26
                    cryptNumChange.append((i+index)-26)
                else:
                    cryptNumChange.append(i+index) 

            for i in cryptNumChange:
                finalwordArray.append(alpha[i])
        

            for i in finalwordArray:
                finalString += i

            print(f'{finalString}\n')

            index += 1
        checkInput = True


intro()
if crypType == "encrypt":
    encrypt()
elif crypType == "decrypt":
    decrypt()
elif crypType == "all":
    all()

