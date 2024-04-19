# def solution(A):
#     # Implement your solution here
#     sums = []
#     poped = []
#     for i in range(1,len(A)):
#         poped.append(A.pop())
#         print(poped)
#         D = abs(sum(poped)-sum(A))
#         sums.append(D)
#     if(len(sums)>0):
#         return min(sums)
#     else:
#         return 0

def solution(A):
    total_sum = sum(A)
    min_difference = float('inf')
    left_sum = 0
    for i in range(len(A) - 1, 0, -1):
        left_sum += A[i]
        right_sum = total_sum - left_sum
        difference = abs(left_sum - right_sum)
        min_difference = min(min_difference, difference)
    return min_difference

# Test the function
# print(solution([3, 1, 2, 4, 3]))  # Output should be 1
A =  [3, 1, 2, 4, 3]
print(solution(A))