# Roman to Integers 
def get_val(S):
    if(S == 'I'): return 1
    elif(S == 'V'): return 5
    elif(S == 'X'): return 10
    elif(S == 'L'): return 50
    elif(S == 'C'): return 100
    elif(S == 'D'): return 500
    elif(S == 'M'): return 1000
    else: return 0

def convert(S,k,ret,last_roman):
    if(k==0):
        return ret
    elif(k>0):
        current_roman = get_val(S[k-1])
        # few conditions for substractions
        if(last_roman == 'I' and current_roman == 5): 
            current_roman = 4 - 1
            ret = ret + current_roman
            convert(S,k-2,ret,S[k-2])
        elif(last_roman == 'I' and current_roman == 10): 
            current_roman = 9 - 1
            ret = ret + current_roman
            convert(S,k-2,ret,S[k-2])
        elif(last_roman == 'X' and current_roman == 50):
            current_roman = 40 - 10
            ret = ret + current_roman
            convert(S,k-2,ret,S[k-2])
        elif(last_roman == 'X' and current_roman == 100): 
            current_roman = 90 - 10
            ret = ret + current_roman
            convert(S,k-2,ret,S[k-2])
        elif(last_roman == 'C' and current_roman == 500): 
            current_roman = 400 - 100
            ret = ret + current_roman
            convert(S,k-2,ret,S[k-2])
        elif(last_roman == 'C' and current_roman == 1000):
            current_roman = 900 - 100
            ret = ret + current_roman
            convert(S,k-2,ret,S[k-2])
        # conditions ends here
        else:
            ret = ret + current_roman
            convert(S,k-1,ret,S[k-2])
        return ret
    
def roman_to_integer(S,n):
#     print('S',S)
    if(n==0):
        return 0
    elif(n>0):
        ret = roman_to_integer(S,n-1)
        if((n-2) >= 0):
            last_roman = S[n-2]
        else:
            last_roman = 'NA'
        val = convert(S,n,ret,last_roman)
        
        return val
    
roman_to_integer("MCMXCIV",7)
