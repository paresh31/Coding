def rotate(A,D,N):
    l = A[D:]
    m = A[:D]
    l.extend(m)
    return(l)

A = [2,4,6,8,10,12,14,16,18,20]
D = 3
N = 10
res = rotate(A,D,N)
print(res)
