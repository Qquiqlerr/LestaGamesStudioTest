def isEven(value):
    #Использование побитогого "И" 
    #1000 & 1 -> 0(not 0 вернет True)
    #111 & 1 -> 1(not 1 вернет False)
    return not value&1

#True
print(isEven(16))

#False
print(isEven(11))