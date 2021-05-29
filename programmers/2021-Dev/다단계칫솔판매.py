def solution(enroll, referral, seller, amount):
    enroll_referrals = list(zip(enroll, referral))
    graph = {}
    money_i_earn = {}

    for enroll_referral in enroll_referrals:
        money_i_earn[enroll_referral[0]] = []
        if enroll_referral[0] not in graph:
            graph[enroll_referral[0]] = []
        graph[enroll_referral[0]].append(enroll_referral[1])

    amount = [i*100 for i in amount]
    seller_amounts = list(zip(seller, amount))
    for seller_amount in seller_amounts:
        flag = True
        seller = seller_amount[0]
        amount = seller_amount[1]
        # print("처음판매자", seller, "처음번금액", amount)
        while flag:
            try:
                if seller in graph and amount/10 >= 1:
                    # print(f"날 가입시켜줬으니 {graph[seller]} 에게 {amount}의 십프로만큼나눠줘야함")
                    own_money = amount - (amount//10)
                    money_i_earn[seller].append(own_money)
                    # print(f"내가 받았으니{own_money}는 내꺼{seller}")
                    # print(money_i_earn[seller], seller)
                    amount = amount - own_money
                    # graph[seller].append(amount)
                    seller = graph[seller][0]
                    # print("새로운 셀러", seller, "남은돈", amount)
                else:
                    # print(f"샐러는{seller}인데 돈 남은게 {amount}")
                    money_i_earn[seller].append(amount)
                    flag = False
            except:
                flag = False
    answers = [sum(money_i_earn[seller]) for seller in enroll]
    return answers


print(solution(["john", "mary", "edward", "sam", "emily", "jaimie", "tod", "young"],
               ["-", "-", "mary", "edward", "mary", "mary", "jaimie", "edward"],
               ["young", "john", "tod", "emily", "mary"],
               [12, 4, 2, 5, 10]))
