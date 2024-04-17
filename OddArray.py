from collections import Counter
def solution(A):
    # Implement your solution here
    c = Counter(A)
    count = 0
    for i in c:
        if(c[i] == 1):
            count = i
        elif(c[i] % 2 != 0):
            count = i
    return count

A = [9,3,9,3,9,9,3]
print("sol",solution(A))