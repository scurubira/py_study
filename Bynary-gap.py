import unittest

def solution(N):
    max_gap = 0
    current_gap = 0
    # Skip the tailing zero(s)
    while N > 0 and N%2 == 0:
        N //= 2
    while N > 0:
        remainder = N%2
        if remainder == 0:
            # Inside a gap
            current_gap += 1
        else:
            # Gap ends
            if current_gap != 0:
                max_gap = max(current_gap, max_gap)
                current_gap = 0
        N //= 2
    return max_gap

if __name__ == '__main__':
    # 1041 - 5
    # 32 - 0
    assert solution(32) == 0
    print('32 - OK')
    assert solution(1041) == 5
    print('1041 - OK')
