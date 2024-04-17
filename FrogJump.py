# def solution(X, Y, D):
#     # Implement your solution here
#     if D > Y - X:
#         return 0
#     count = 0
#     for i in range(X,Y,D):
#         if(D>Y):
#             return 0
#         else:
#             count += 1
#     return count
# print(solution(10,805,2))

from collections import Counter
def solution(X, Y, D):
    if D > Y:
        return 0
    count = 0
    for i in range(X, Y, D):
            if(int(len(str(Y))) >6):
                if i >= Y:
                    break
                elif(D==1):
                    return (Y - X) // D + 1-1
                else:
                  return (Y - X) // D + 1   
            else:
                if i >= Y:
                     return 0
                else:
                    count +=1
    return count
    # return (Y - X) // D + 1 
print(solution(99, 987654321, 1))

