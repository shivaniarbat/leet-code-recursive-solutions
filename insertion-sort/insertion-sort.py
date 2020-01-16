# Insertion sort - Recursively
def insert(A,k):
    if(k==0):
        return A
    elif(k>0):
        if(A[k-1]>A[k]):
            temp = A[k]
            A[k] = A[k-1]
            A[k-1] = temp
            insert(A,k-1)
        return A

def rec_insertion_sort(A,n):
    if(n == 0):
        return A
    elif(n > 0):
        rec_insertion_sort(A,n-1)
        insert(A,n)
        return A

rec_insertion_sort([4,5,3,1,4],4)
