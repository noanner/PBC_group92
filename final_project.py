name = input("您的餐廳名稱: ")
menu_list = ["beef", "pork", "chick", "vege", "keto"]
stock_order_list = [25, 25, 25, 25, 25]  # 預設購買存貨數量[牛肉, 豬肉, 雞肉, 生菜, 生酮]
price_list = [20, 18, 18, 12, 32]  # 產品價格
material_price = [10, 9, 9, 6, 16]  # 原料價格
demand_list = [20, 20, 20, 20, 20]  # 預設需求
stock_list = [0,0,0,0,0]  # 預設存貨
order_fixed_cost = 50  # 訂貨固定成本
stock_cost = 2  # 存貨變動成本
# demand_pattern = read.....
demand_pattern = [[20,20,20,20,20],[25,5,30,28,18],[30,25,28,5,15],[15,6,23,18,40],[3,15,46,38,2],[28,26,25,8,13],[9,7,12,62,8]]

price_dict = dict()
for i in range(len(menu_list)):
    price_dict[menu_list[i]] = price_list[i]
    
stock_dict = dict()
for i in range(len(menu_list)):
    stock_dict[menu_list[i]] = stock_list[i]

material_dict = dict()
for i in range(len(menu_list)):
    material_dict[menu_list[i]] = material_price[i]

# print(price_dict.items())
# print(stock_dict.items())
# print(material_dict.items())

def ordering(order):
    # 玩家訂單函數
    order_list = order.split(",")  # 輸入方法之後可改
    if len(order_list) != 5:
        result = "輸入錯誤"
    else:
        result = "輸入成功"
        for i in order_list:
            try:
                i = int(i)
            except ValueError:
                result = "輸入錯誤"
    print(result)
    return result, order_list

# order_list = ordering()  # 這個之後要設在迴圈內
# print(beef_order)
# print(order_list[0])

def day_result(demand=demand_list,stock_order=stock_order_list,stock=stock_list):
    # 當天最終結果綜合計算
    sold_list = []
    unmeet_list = []
    percent_list = []
    revenue_list = []
    total_revenue = 0
    for i in range(len(stock_list)):
        stock_list[i] += stock_order[i]
        sold = min(demand[i],stock_list[i])
        if sold < demand[i]:
            unmeet = demand[i] - sold
        else:
            unmeet = 0
        unmeet_list.append(unmeet)
        stock_list[i] -= sold
        sold_list.append(sold)
    for i in range(len(sold_list)):
        revenue = sold_list[i] * price_list[i]
        revenue_list.append(revenue)
        total_revenue += revenue
    for i in revenue_list:
        if total_revenue > 0:
            percentage = i / total_revenue
            percent_list.append("%.2f" % percentage)
        else:
            percent_list.append(0.00)
    return stock_list,sold_list,unmeet_list,percent_list,revenue_list,total_revenue

# stock_list, sold_list, unmeet_list, percent_list, revenue = day_result()  # 這個之後要設在迴圈內

def order_cost(order=stock_order_list,price=material_price, fixed_cost=order_fixed_cost):
    # 計算訂貨成本
    material_cost = 0
    total_fixed_cost = 0
    for i in range(len(order)):
        if order[i] != 0:
            material_cost += order[i] * price[i]
            total_fixed_cost += fixed_cost
        else:
            pass
    return material_cost, total_fixed_cost

# material_cost, fixed_cost = order_cost()  # 這個之後要設在迴圈內

def stock_cost(stock=stock_list, stock_cost=stock_cost):
    # 計算存貨總成本
    stock_total_cost = 0
    for i in range(len(stock)):
        stock_total_cost += stock[i] * stock_cost
    return stock_total_cost


import matplotlib.pyplot as plt
day = ["Day1","Day2","Day3","Day4","Day5","Day6","Day7"]
def plot_result(stock,acc_profit,profit,order_cost):
    # 折線圖函式
    plt.figure(figsize=(10,5),dpi=100,linewidth = 2)
    plt.plot(day,acc_profit,'s-',color = 'r', label="Accumulated Profit")
    plt.plot(day,stock,'o-',color = 'g', label="Stock Cost")
    plt.plot(day,profit,'s-',color = 'b', label="Day Profit")
    plt.plot(day,order_cost,'s-',color = 'y', label="Day Order Cost")
    plt.xticks(fontsize=12)
    plt.yticks(fontsize=12)
    plt.xlabel("Day", fontsize=20, labelpad = 10)
    plt.ylabel("$", fontsize=20, labelpad = 10)
    plt.legend(loc = "best", fontsize=10)
    plt.show()

# print(stock_list)
# print(sold_list)
# print(unmeet_list)
# print(stock_cost())

stock_cost_list = []
accumulated_profit_list = []
profit_list = []
order_cost_list = []
accumulated_profit = 0
for i in range(7):  # print 出的方式可以再改
    if i == 0:  # 初始頁面
        print("Day "+str(i+1))
        print(menu_list)
        stock_list, sold_list, unmeet_list, percent_list, revenue_list,revenue = day_result(demand_pattern[i],stock_order_list,stock_list)
        material_cost, total_fixed_cost = 0, 0   
    else:  # day 1 ~ day 6之後的頁面
        print("有要訂貨嗎?")
        print("庫存: "+str(stock_list))
        print("進貨成本: "+str(material_price))
        a, order_a = ordering(input("請輸入訂貨量: "))
        while a == "輸入錯誤":
            a, order_a = ordering(input("請輸入訂貨量: "))
        order_list = []
        for sub_order in order_a:
            order_list.append(int(sub_order))
        after_order = []
        for j in range(len(order_list)):
            after_order_a = order_list[j] + stock_list[j]
            after_order.append(after_order_a)
        print("訂後庫存: ",end="")
        print(after_order)
        stock_list, sold_list, unmeet_list, percent_list, revenue_list,revenue = day_result(demand_pattern[i],order_list,stock_list)
        material_cost, total_fixed_cost = order_cost(order_list)
        print("訂貨固定費用: " + str(total_fixed_cost))
        print("材料費用: " + str(material_cost))
        print("總價: ",end="")
        print(material_cost + total_fixed_cost)
        print("Day " + str(i+1))
        print(menu_list)
    stock_total_cost = stock_cost(stock_list)
    stock_cost_list.append(stock_total_cost)
    profit = revenue - material_cost - stock_total_cost - total_fixed_cost
    accumulated_profit += profit
    accumulated_profit_list.append(accumulated_profit)
    profit_list.append(profit)
    order_cost_list.append(material_cost+total_fixed_cost)
    print("這是你今天營運結果")
    print("需求量: " + str(demand_pattern[i]))
    print("庫存量: ",end="")
    if i == 0:
        print(stock_list)
    else:
        print(after_order)
    print("賣出數量: " + str(sold_list))
    print("營業額: " + str(revenue_list))
    print("營業佔比: " + str(percent_list))
    print("今日收益: " + str(revenue))
    print("進貨成本: " + str(material_cost + total_fixed_cost))
    print("存貨成本: " + str(stock_total_cost))
    print("本日利潤: " + str(profit))
    print("累積利潤: " + str(accumulated_profit))

print("最終結果: " + str(accumulated_profit))
# print(accumulated_profit_list)
# print(stock_cost_list)
plot_result(stock_cost_list,accumulated_profit_list,profit_list,order_cost_list)

if accumulated_profit >= 3000:
    print("恭喜您的餐廳榮獲",end="")
    if accumulated_profit > 10000:
        print("米其林三星殊榮")
    elif accumulated_profit <= 10000 and accumulated_profit > 7000:
        print("必比登必吃百大美食")
    elif accumulated_profit <= 7000 and accumulated_profit > 5000:
        print("「我就讚」美食獎")
    else:
        print("街訪第一名")
elif accumulated_profit < 3000 and accumulated_profit >=0:
    print("「今晚我想來點 " + name +" 的漢堡全餐」",end="；")
    print("「客人請您明天再來喔」")
    print("因為沒控制好存貨，",end="")
    if accumulated_profit > 2000:
        print("漢堡稍微會缺貨")
    elif accumulated_profit <= 2000 and accumulated_profit > 500:
        print("漢堡偶爾缺貨")
    else:
        print("客人每次來都抓狂")
else:
    print("加盟大老闆:「朽木不可雕也，你重練吧」")