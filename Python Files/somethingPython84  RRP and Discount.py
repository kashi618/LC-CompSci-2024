def salePrice():
    rrp = []
    discount = []
    for i in range(6):
        rrp.append(float(input("Input RRP amount: ")))
        discount.append(float(input("Input discount (percentage): ")))
        print(float(rrp[0+i])*(float(discount[0+i])/100))


print(salePrice())


