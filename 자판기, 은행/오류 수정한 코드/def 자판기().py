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

card = 은행()  # 초기 잔액 설정

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
