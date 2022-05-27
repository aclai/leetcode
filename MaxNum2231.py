#find number combination with greatest value while allowed to swap digits with equal parity

#main program
def maxNum(usrAns):
 
    oddNum = 9
    evenNum = 8
        
    #make string into array
    usrInpt = mkary(usrAns)
    
    #check array for 9's & 8's, then 7's & 6's ... 3's &2's. Note: not 1's & 0's for they are the smallest
    while oddNum > 1:
        
        #test
        #print ("most outter loop")
        #print (oddNum)
        #print (evenNum)

        #generate greatest value according to the rules - type array
        usrInpt = biggestDigit(usrInpt, oddNum, evenNum)
        
        #decrease 9 & 8 to 7 & 6 and so on
        oddNum = oddNum - 1
        evenNum = evenNum - 1
    
    #test
    #print ("after most outter loop")
    #print (oddNum)
    #print (evenNum)

    #change array into string
    maxNumStr = aryToStr(usrInpt)

    print (maxNumStr)


###############################################################################################################################################
###############################################################################################################################################
###############################################################################################################################################

#break user input into digits in array & turn type into integer
def mkary(usrAns):
    
    usrInpt = []

    for i in usrAns:
        usrInpt.append(int(i))
    
    #test
    #print (usrInpt)

    return usrInpt
        


#find from 9 & 8 to 3 & 2 and swap with a smaller number at an earlier index in the array if it exists - skip 1 & 0 for already smallest
def biggestDigit(usrInpt, oddNum, evenNum):

    #position counter for the current number being looked for
    i = 0
    
    #test
    #print ("in biggestDigit")
    
    #iterate to look for current oddNum and evenNum
    while i < len(usrInpt):
    
        #test
        #print (i)
        #print (len(usrInpt))
        #oddTF = (usrInpt[i] == oddNum)
        #evenTF = (usrInpt[i] == evenNum)
        #print (oddTF)
        #print (evenTF)

        #if found current oddNum or evenNum
        if usrInpt[i] == oddNum or usrInpt[i] == evenNum:    
            
            #position counter for numbers to swap with oddNum or evenNum
            ii = 0
            
            #test
            #print (usrInpt)
            
            #iterate before position i
            while ii < i:
                
                #test
                #print (usrInpt[ii] < usrInpt[i]) 
                #print (usrInpt[ii] % 2 == usrInpt[i] % 2)

                #find 1st smaller digit with same parity
                if  usrInpt[ii] < usrInpt[i] and usrInpt[ii] % 2 == usrInpt[i] % 2:
                    #swap the numbers' position
                    tempNum = usrInpt[ii]
                    usrInpt[ii] = usrInpt[i]
                    usrInpt[i] = tempNum
                    
                    #test
                    #print ("break")
                    
                    break
                
                ii = ii + 1
                
                #test
                #print ("ii")
                #print (ii)

        i = i + 1
        
        #test
        #print ("i")
        #print (i)

    #return biggest digit value and position
    return usrInpt

#change array to string
def aryToStr(usrInpt):
    
    maxNumStr = ""
    
    for i in usrInpt:
        maxNumStr = maxNumStr + str(i)

    return maxNumStr


###############################################################################################################################################
###############################################################################################################################################
###############################################################################################################################################



#test if any number before the biggest digit in user input has the same parity with the biggest number
#def numPar(usrInpt, bgstDgt, bgstPos):
#    parity = False
#    i = 0
#
#    while i < bgstPos:
#        if int(usrInpt[i]) % 2 == bgstDgt % 2:
#            parity = True
#            break
#
#        i = i + 1
#    
#    return (parity, i)

        
#swap the biggest digit with a digit that comes before it in the user input
#def numSwap(usrInpt, bgstPos, swapPos):
    



#replace biggest digit with 0 in user input and 
#def writeNum(usrInpt, bgstNum):
    
