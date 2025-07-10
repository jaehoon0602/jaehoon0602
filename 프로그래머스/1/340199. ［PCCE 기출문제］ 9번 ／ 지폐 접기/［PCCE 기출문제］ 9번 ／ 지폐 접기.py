def solution(wallet, bill):
    from math import floor

    # 지갑의 가로세로 중 작은 값이 앞에 오도록 정렬
    wallet_w, wallet_h = sorted(wallet)
    # 지폐의 가로세로 중 작은 값이 앞에 오도록 정렬
    bill_w, bill_h = sorted(bill)

    answer = 0
    while bill_w > wallet_w or bill_h > wallet_h:
        # 긴 쪽을 반으로 접기
        if bill_w >= bill_h:
            bill_w = bill_w // 2
        else:
            bill_h = bill_h // 2
        answer += 1
        # 다시 정렬 (회전 가능성 고려)
        bill_w, bill_h = sorted([bill_w, bill_h])

    return answer
