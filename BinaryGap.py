from collections import Counter
def solution(N):
    size = []
    binary = bin(N).split('0b')[1]
    new_b = Counter(binary)
    if ((new_b['1'] == 1) or (new_b['1'] >=1 and new_b['0'] == 1 and new_b[1]==1)) :
        return 0
    else:
        split_bin = []
        current_seq = ""
        for digit in binary:
            if digit == '1':
                split_bin.append(current_seq)
                current_seq = ''
            else:
                current_seq += digit
        for i in split_bin:
            size.append(len(i))
        return max(size)