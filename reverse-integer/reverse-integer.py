# Reverse the integer recursively
def reverse(x,k,ret) -> int:
    if(k==0): return ret
    else:
        ret = ret * 10 + (x % 10)
        x //= 10
        return reverse(x,k-1,ret)
        
def rec_reverse_integer(x,n) -> list:
    if(n==0): return x
    else:
        rec_reverse_integer(x,n-1)
        val = reverse(x,n,0)
        return val

rec_reverse_integer(128319,6)
