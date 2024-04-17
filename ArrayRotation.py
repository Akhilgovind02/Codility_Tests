def solution(A,K):
    if(len(A) != 0):
        d = K % len(A)
        def loop(i):
            i = len(A)-1
            poped = A.pop(i)
            A.insert(0,poped)
        if d!=0:
            for i in range(d):
                loop(i)
        else:
            for i in range(K):
                loop(i)
        return A
    else:
        return []
A = [3, 8, 9, 7, 6]
K = 0
solution(A,K)
print(A)