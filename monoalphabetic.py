import math
 
#alohabet variables
alpha = ["a","b","c",'d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
alpha2 = alpha[:]
ciphAlphaP = []
ciphAlpha = []
alphaBool = False
boolBoi = False
 
#keyword variables
keywordA =[]
repeatsL = []
repeatsLet = []
changeKey = False
keywordString = ""
 
#plain text variables
plainTextPos = []
cipherText = ""
 
#decision variables
decisionF = ""
decision = ""
 
def keyRepeat():
    global keyword
    global keywordString
    global changeKey
    keyword1 = input("What is your keyword?\n")
    keyword = keyword1.lower()
 
    #keyword put into list
    for i in keyword:
        keywordA.append(i)
 
    #checks if there are reapeting letters in keyword
    for i in keywordA:
        index = 0
        redRes = 0
        for index in range(0,len(keyword)):
            if i == keywordA[index]:
                redRes+=1
                if redRes > 1: # if this value is larger than one, then it will add repeating 
                               # letters' positions into a list
                    repeatsL.append(index)
                    changeKey = True
            
    #takes out repeating letters of repeatsL list
    repeatsLet = list(set(repeatsL))
 
 
    index = 0
    #deletes repeating letters in keywordA 
    for i in repeatsLet:
        del keywordA[i-index] #as the loop detetes terms, the list shorterns as well 
                              # in order to compensate we decrease the value of the numbers and then delete that position
    
        index+=1
 
    #adds new keyword (without repeating letters) into string
    for i in keywordA:
        keywordString += i
        
 
    #if this conditional is met, the program sends a message to user with updated string
    if changeKey == True:
        print(f'Due to your keyword having repeating letters, it was changed to {keywordString}\n')
 
def cipherAlpha():
    global keywordA
    global alpha
    global finalAlph
 
     #takes the letters in keywords from the alpha List
    alphaIndex = 0
    index = 0
    for i in keywordA:
        index = 0
        alphaBool = False
        while alphaBool == False:
            if i == alpha[index]:
                del alpha[index]
                alphaBool = True
            else:
                index += 1
 
    print(alpha)
 
    finalAlph = keywordA[:]
 
    def findVal(list):
        return 26-len(list)
 
    for i in range(0,findVal(keywordA)):
        finalAlph.append(alpha[i])
 
 
    print(finalAlph)
 
decisionF = input("Would you like to encrypt or decrypt a message?:\n")
decision = decisionF.lower()
 
if (decision != "encrypt" and decision != "decrypt"):
        checkInput = False
        print("Please type encrypt or decrypt") #making sure they type encrypt or decrypt
        
        while (checkInput == False):
            decisionF = input("Would you like to decrypt or encrypt a word?\n")
            decision = decision.lower()
            if (decision == "encrypt" or decision == "decrypt"):
                checkInput = True
            else:
                print("Please type encrypt or decrypt")
 
 
if decision == "encrypt":
 
    keyRepeat()
    #input string you want to be encrypted
 
    plaintext = input("Enter your plaintext: \n")
 
    print(f'{keyword} and {plaintext}')
 
    #this function is not needed but I like it
    def alphaC():
        global ciphAlpha
        global ciphAlphaP
 
        for letter in keyword:
            ciphAlphaP.append(letter)
        
        print(ciphAlphaP)
        alphaBool = False
        checkL = False
 
        #convert letters into numbers
        alphaIndex = 0
        for letters in ciphAlphaP:
            #each letter in list
            index = 0
            print(letters)
            checkL = False
            
            while checkL == False:
                #sees if certain letter from list is the same as one in the alpha list
                if alpha[index] == ciphAlphaP[alphaIndex]:
                    ciphAlpha.append(index)
                    alphaIndex += 1
                    print(alphaIndex)
                    checkL = True
 
                else:
                    index += 1
 
        print(ciphAlpha)
 
 
    #takes the letters in keywords from the alpha List
    cipherAlpha()
 
    #we have gotten the new alphabet to go with the keyword
 
    #convert plaintext using cipher alphabet here \/
 
    #get position of letters in plaintext in relation to plain ALphabet
    for i in plaintext:
        alphaBool = False
        index = 0
        while alphaBool == False:
            if i == alpha2[index]:
                plainTextPos.append(index)
                alphaBool = True
            else:
                index+= 1
 
    #print (plainTextPos)
 
    for i in plainTextPos:
        cipherText += finalAlph[i]
 
        
 
    print(f'Your encrypted message is {cipherText}')
    print(f"Remember your keyword")
 
elif decision == "decrypt":
    #get keyword and determine if there are repeats
    keyRepeat()
    #determine the new alphabet from keyword
    cipherAlpha()
 
    ciphTextR = input("Enter your cipher text:\n")
    ciphText = ciphTextR.lower()
 
    #keyword, cipher alphabet, cupher text --> plaintext
    for i in ciphText:
        alphaBool = False
        index = 0
        while alphaBool == False:
            if i == finalAlph[index]:
                plainTextPos.append(index)
                alphaBool = True
            else:
                index+= 1
 
    #print (plainTextPos)
 
    for i in plainTextPos:
        cipherText += alpha2[i]
 
    print(f'Your encrypted message is {cipherText}')
    print(f"Remember your keyword")
 
 
 
 

