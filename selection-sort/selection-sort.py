# Selection Sort Recursively
def max_index(A,k):
    if(k==0): return 0
    elif(k > 0):
        # return max 
        # search linear in the list
        max_ind = max_index(A,k-1)
        if(A[k] > A[max_ind]):
            return k # return greater 
        else:
            return max_ind
        

def rec_selection_sort(A,n):
    if(n==0): return A
    elif(n > 0):
        k = max_index(A,n)
        temp = A[n]
        A[n] = A[k]
        A[k] = temp
        rec_selection_sort(A,n-1)
        return A

rec_selection_sort([5,5,4,3,2,1,5],6)   
