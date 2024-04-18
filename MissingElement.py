
def solution(K):
    ar1 = []
    A = sorted(K)
    if not A:
        return 1
    max_num = max(A)
    if max_num <= 0:
        return 1
    for i in range(1,max_num+1):
        ar1.append(i)
    if(ar1 != A):
        F = set(ar1).difference(set(A))
        return F.pop()
    else:
        return max_num+1

# Example usage:
B = [1,2,3,4,5,6,7]
print(solution(B))  # Output: 5



