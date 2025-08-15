from typing import List, Tuple

DISCOUNTS = [10, 20, 30, 40]

def solution(users: List[Tuple[int, int]], emoticons: List[int]) -> List[int]:
    """
    users: [ [비율, 가격], ... ]
    emoticons: [정가, ...]
    return: [최대_가입자수, 최대_매출]
    """
    best_subs, best_revenue = 0, 0
    m = len(emoticons)
    assigned = [0] * m  # 각 이모티콘에 부여된 할인율

    def evaluate() -> Tuple[int, int]:
        subs, revenue = 0, 0
        # 미리 할인된 가격 캐싱
        discounted_prices = [emoticons[i] * (100 - assigned[i]) // 100 for i in range(m)]
        for ratio, limit in users:
            spend = 0
            # 기준 이상 할인된 이모티콘만 구매
            for i in range(m):
                if assigned[i] >= ratio:
                    spend += discounted_prices[i]
            # 한도(가격 기준) 이상이면 구독 전환
            if spend >= limit:
                subs += 1
            else:
                revenue += spend
        return subs, revenue

    def dfs(idx: int):
        nonlocal best_subs, best_revenue
        if idx == m:
            subs, rev = evaluate()
            # 1순위: 가입자, 2순위: 매출
            if subs > best_subs or (subs == best_subs and rev > best_revenue):
                best_subs, best_revenue = subs, rev
            return
        for d in DISCOUNTS:
            assigned[idx] = d
            dfs(idx + 1)

    dfs(0)
    return [best_subs, best_revenue]
