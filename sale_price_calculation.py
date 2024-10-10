def salePrice(line):
    line = line[:-1]
    list1 = line.split(",")
    cost = int(list1[1])/100*20
    tax = int(list1[1])/100*18
    profit = int(list1[1])/100*25
    final_price = int(list1[1]) + cost + tax + profit
    return "Product: " + list1[0] + " || " + "Price: " + str(final_price) + "$" + "\n"

with open("costs.txt","r+",encoding="utf-8") as file:
    for i in file:
        products = []
        products.append(salePrice(i))

        with open("salePrices.txt","a",encoding="utf-8") as sale:
            sale.writelines(products)