def 은행():
    print("어서오세요 태호 은행입니다.")
    print("-------------------------------------")
    print("고객님의 계좌 번호는 : 1111-1111-1111 입니다.")
    card = 0  # 초기 잔액
    while True:
        money_no = int(input("고객이 사용하실 계좌 비밀번호를 입력해주세요 > "))
        if len(str(money_no)) != 6:
            print("6자리 비밀번호를 입력해주세요")
            continue
        else:
            money_no2 = int(input("재확인 > "))
            if money_no == money_no2:
                print("일치합니다")
                break
            else:
                print("일치하지 않습니다")
                continue
    print("-------------------------------------")
    money = int(input("입금하실 금액을 선택하세요 > "))
    card += money

    while True:
        number = int(input("어떤걸 하시겠습니까? (1) 출금, (2) 입금, (3) 종료 > "))
        print("-------------------------------------")
        if number == 1:
            print("출금 페이지입니다.")
            while True:
                num1 = int(input("계좌번호를 입력하세요 (-)제외 > "))
                num2 = int(input("비밀번호를 입력하세요 > "))
                print("-------------------------------------")
                if num1 != 111111111111:
                    print("계좌번호가 일치하지 않습니다.")
                    continue
                elif num2 != money_no:
                    print("계좌 비밀번호가 일치하지 않습니다.")
                    continue
                else:
                    subtraction = int(input("출금 하실 금액을 입력하세요 > "))
                    print("-------------------------------------")
                    if subtraction > card:
                        print("잔액부족.")
                        continue
                    else:
                        card -= subtraction
                        print(f"출금 완료! 현재 잔액은 {card}원 입니다.")
                        break
        elif number == 2:
            print("입금을 선택하셨습니다.")
            money_plus = int(input("입금하실 금액을 선택하세요 > "))
            card += money_plus
            print(f"현재 카드 잔액 {card}원 입니다.")
            print("-------------------------------------")
        elif number == 3:
            print("종료")
            break
        else:
            print("잘못된 선택입니다. 다시 선택해주세요.")
            continue
    
    return card
