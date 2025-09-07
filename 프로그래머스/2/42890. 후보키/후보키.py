from itertools import combinations

def solution(relation):
    n_rows = len(relation)
    n_cols = len(relation[0])
    candidates = []

    # 모든 컬럼 조합 생성
    for size in range(1, n_cols+1):
        for comb in combinations(range(n_cols), size):
            # 유일성 검사
            tmp = [tuple(item[c] for c in comb) for item in relation]
            if len(set(tmp)) == n_rows:
                # 최소성 검사
                if not any(set(c).issubset(comb) for c in candidates):
                    candidates.append(comb)

    return len(candidates)
