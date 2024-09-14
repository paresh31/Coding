def rotate(A,D,N):
    l = A[D:]
    m = A[:D]
    k = []
    k = l + m
    return(k)

# def rotate(A,D,N):
#     for i in range(N):
        
    
    
A = [1, 2, 3, 4, 5]
D = 2
N = 5
res = rotate(A,D,N)
print(res)
