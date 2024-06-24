def price():    #가격
    plus = 0
    for f in range(0,len(a_list)):
        x=a_list[f]
        plus = plus+(dic[x]*b_list[f])
    return plus
