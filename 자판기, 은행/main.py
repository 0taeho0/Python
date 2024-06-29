while(True):
    은행()
    
    number = int(input("(1) 은행, (2) 자판기, (3) 종료 선택하여 주세요. >"))
    if(number == 1) :
        은행()
        continue
    elif(number == 2) :
        자판기()
        continue
    else :
        break
