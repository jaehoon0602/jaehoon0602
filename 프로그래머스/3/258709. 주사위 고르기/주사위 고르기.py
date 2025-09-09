from itertools import combinations, product
from bisect import bisect_left, bisect_right

def solution(dice):
    n = len(dice)
    pick_count = n // 2
    dice_idx = list(range(n))
    
    best_win = -1
    best_choice = []
    
    # A가 가져갈 주사위 조합 (nC(n/2))
    for comb in combinations(dice_idx, pick_count):
        A_idx = set(comb)
        B_idx = set(dice_idx) - A_idx
        
        # A의 합의 모든 경우의 수
        A_sums = [sum(x) for x in product(*[dice[i] for i in A_idx])]
        B_sums = [sum(x) for x in product(*[dice[i] for i in B_idx])]
        
        A_sums.sort()
        B_sums.sort()
        
        # 승리 횟수 계산
        win, draw, lose = 0, 0, 0
        for a in A_sums:
            # B의 점수 중 a보다 작은 개수
            win += bisect_left(B_sums, a)
            # B의 점수 중 a와 같은 개수
            draw += bisect_right(B_sums, a) - bisect_left(B_sums, a)
            # 나머지는 패배
            lose += len(B_sums) - bisect_right(B_sums, a)
        
        if win > best_win:
            best_win = win
            best_choice = sorted(i+1 for i in A_idx)  # 문제에서 주사위 번호는 1부터 시작
    
    return best_choice
