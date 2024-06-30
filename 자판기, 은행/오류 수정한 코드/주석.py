def 은행():
    print("어서오세요 태호 은행입니다.")
    print("-------------------------------------")
    print("고객님의 계좌 번호는 : 1111-1111-1111 입니다.")
    card = 0  # 초기 잔액 설정
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

def 자판기(card):
    print("어서오세요 김태호 자판기입니다")
    print("-----------------------------")
    menu_list = ["콜  라", "사이다", "포카리", "핫식스", "알로에"]
    menu_price = [2000, 2000, 2500, 2300, 1700]

    print("    김태호 자판기의 메뉴")
    print("-----------------------------")
    print("            메  뉴   가격")
    for i in range(len(menu_list)):
        print(f"{i+1}번 메뉴 :  {menu_list[i]}   {menu_price[i]}")
    print("-----------------------------")
    print(f"현재 고객님의 카드 잔액은 {card}원 입니다.")
    print("구매가 가능하신 메뉴")
    print("-----------------------------")

    for i in range(len(menu_price)):
        if card >= menu_price[i]:
            print(f"{i+1}번 메뉴 :  {menu_list[i]}   {menu_price[i]}")
        else:
            print(f"\033[31m{i+1}번 메뉴 :  {menu_list[i]}   {menu_price[i]}\033[0m")
    print("-----------------------------")

    while True:
        menu_no = int(input("구매하려는 메뉴 번호를 입력하세요 > "))
        if menu_no < 1 or menu_no > len(menu_list):
            print("입력하신 메뉴 번호는 없는 번호입니다.")
            continue
        else:
            if card >= menu_price[menu_no - 1]:
                print(f"구매하신 메뉴 : {menu_list[menu_no - 1]}")
                card -= menu_price[menu_no - 1]
                break
            else:
                print("잔액이 부족합니다.")
                continue
    
    print(f"현재 잔액은 {card}원 입니다.")
    return card

card = 은행()  # 초기 은행 계좌 잔액 설정

while True:
    print("-------------------------------------")
    number = int(input("(1) 은행, (2) 자판기, (3) 종료 선택하여 주세요. > "))
    if number == 1:
        card = 은행()
    elif number == 2:
        card = 자판기(card)
    elif number == 3:
        print("프로그램을 종료합니다.")
        break
    else:
        print("잘못된 선택입니다. 다시 선택해주세요.")
        continue
