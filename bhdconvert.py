"""
    Hexadecimal <-> Decimal <-> Binary conversions
    
    @author: Jesse Vazquez
    Github: github.com/javproj
    
    Usage:
        > python convert.py [type1] [type2] [value]
        > e.g.: python convert.py h b F1
        > ----> converts hex value F1 to binary "11110001"

"""
import sys

#Grab arguments
type1 = sys.argv[1]
type2 = sys.argv[2]
value = sys.argv[3]

#Just in case, switch all alphas to lower
value = value.lower()

#-----INIT VARS###
hexAlphas = {
    "a" : 10,
    "b" : 11,
    "c" : 12,
    "d" : 13,
    "e" : 14,
    "f" : 15
}

hexVals = {
    10 : "a",
    11 : "b",
    12 : "c",
    13 : "d",
    14 : "e",
    15 : "f"
}

#array holding letters to check against
alpha = ["a", "b", "c", "d", "e", "f", "A", "B", "C", "D", "E", "F"]

#counter
cnt = 0

#length of input string
length = len(value)

#-----Functions####
def d2b(decimalIn):
    """ Decimal to Binary function"""    
    #initialize remainder
    rem = 0

    dec = int(decimalIn)
    

    #string to store binary value
    binval = ""

    while dec > 0:
        rem = dec % 2 #remainder
        dec = dec / 2
    
        binval += str(rem)

    #Need length of binval for appropriate output 
    binLength = len(binval) - 1

    #Depending on size of binval, pad with zeros for multiple of 4 bit output
    if binLength < 4 and dec < 16:
        padamt = 4 - len(binval)    
        binval += "0"*padamt

    elif binLength < 8 and dec < 128:
        padamt = 8 - len(binval)    
        binval += "0"*padamt   

    elif binLength < 12 and dec < 256:
        padamt = 12 - len(binval)    
        binval += "0"*padamt
    
    elif binLength < 16 and dec < 512:
        padamt = 16 - len(binval)    
        binval += "0"*padamt  

    #Reverse binary string for appropriate value
    binval = binval[::-1]

    return binval

def h2b(hexIn):
    """Hexadecimal to Binary"""
    cnt = 0     #Reset counter just in case
    
    hbOut = ""  #initialize return value
    
    while cnt < len(hexIn):
        if hexIn[cnt] in hexAlphas:    
            hbOut += d2b(hexAlphas[hexIn[cnt].lower()])
    
        else:
            hbOut += d2b(hexIn[cnt])
        cnt += 1            

    return hbOut

def b2d(binIn):
    """Binary to Decimal"""
    
    cnt = 0     #init counter    

    decVal = 0  #init return decimal value
    
    revbin = binIn[::-1] #Need to reverse input binary for fn

    while cnt < len(binIn):
        if int(revbin[cnt]) is 1:
            decVal += 2**cnt
    
        cnt += 1  #increment x

    return decVal

def d2h(dhIn):
    """Decimal to Hex"""
    #Convert to int
    dec = int(dhIn)

    #initialize remainder
    rem = 0

    #string to store hex value
    hexval = ""

    while dec > 0:
        rem = dec % 16
        dec = dec / 16
    
        if rem in hexVals:
            hexval += str(hexVals[rem])
        else:
            hexval += str(rem)

    #Reverse hexval to get appropriate value
    hexval = hexval[::-1]

    return hexval

def b2h(bhIn):
    """Binary to Hex"""
    
    hexOut = "" #init return string
    
    #first pad with zero's if input not multiple of 4 for clarity
    if (len(bhIn) % 4) != 0:
        cnt = 0                 #init cnt        
        t = bhIn[::-1]          #temp for padding
        t += "0"*(len(bhIn)%4)  #pad
        bhIn = t[::-1]          #reverse t for padded bhIn

    #Use b2d fn to get decimal value
    deciVal = b2d(bhIn)   

    #Now return hex using d2h
    return d2h(deciVal)

#-----/FUNCTIONS###
 
###Start
if type1 is 'b' and type2 is 'd':   
    print b2d(value)
if type1 is 'd' and type2 is 'h':
    print d2h(value)
if type1 is 'd' and type2 is 'b':
    print d2b(value)
if type1 is 'h' and type2 is 'b':
    print h2b(value)
if type1 is 'b' and type2 is 'h':
    print b2h(value)
