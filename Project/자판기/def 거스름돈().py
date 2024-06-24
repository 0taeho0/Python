def 거스름돈(num):
    list=[]
    if(num > 0):
        for a in range(0,len(str(num))):
            list.append(int(str(num)[a]))
        print("\n거스름돈으로 50000원", list[0],"개", "10000원", list[1], "개, ", "5000원", list[2],"개, ", "1000원", list[3],"개, ", "500원", list[4],"개, ", "100원", list[5],"개, ", "50원", list[6],"개, ", "10원", list[7],"개를 드리겠습니다.")
        print("총 %d원입니다."% (num))
    elif (num==0):
        print("\n거스름돈이 없습니다.")
    else:
        print("\n잘못된 금액을 넣으셨습니다.")
