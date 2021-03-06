
ques_list1 = [[2,"First in, First out (FIFO)是指先進的貨品先出貨，Last in, First out (LIFO)是讓後進的貨品先出貨。如果你\
               賣的是市場價格呈上升趨勢的商品如貴金屬，或是沒有特定保存期限的商品如煉油業，適合使用哪種存貨\管理方法?",
                "FIFO","LIFO"],
              [3,"安全庫存：安全庫存又稱保險庫存，是指為了防止不確定性因素的保險庫存量。小明開了一間\
               漢堡店，平常總是備100個漢堡的庫存供日常販售，另外在地下室裡另外放了25個漢堡的庫存以備不時之需\
               。請問小明經營的漢堡店安全庫存數量為？",
               "100","25"],
              [3,"訂購週期：訂購週期為連續訂購之間的時間間隔。小明開了一間漢堡店，漢堡需要用到麵包、生菜及肉\
               排。麵包每3天需要訂貨一次，生菜與肉排則是每2天訂貨一次。請問生菜的訂購週期為？",
               "3天","2天"],
              [3,"訂購點：當商品庫存低至特定水位時，再次訂購商品的時間點。小明開了一間漢堡店，漢堡需要用到麵包\
               、生菜及肉排。每天開店前都要準備300個麵包，只要麵包庫存少於50個，小明就會擔心缺貨。請問麵包的訂\
               購點為？",
               "300個","50個"],
              [2,"最大存貨量：所能存放的最大物品數量。小明開了一間漢堡店，漢堡店的食物儲藏室最多可以裝500個漢堡的\
               材料，但是小明希望留一條走道方便拿東西，所以規定最多只能放450份漢堡食材。請問漢堡食材的最大庫存量為？",
               "450個","500個"],
              [2,"最小訂購量：每筆訂單的最低起訂量。小明開了一間漢堡店，每天開店時會準備5公斤的生菜，\
               但賣生菜的老闆說每次只送5公斤連付油錢都不夠，要買8公斤以上才送貨。請問生菜的最小訂購量為？",
               "4公斤","8公斤"]]

ques_dict1 = dict()
for i in range(len(ques_list1)):
    ques_dict1[i+1] = ques_list1[i]

ques_list2 = [[3,"期末庫存：期末庫存=期初庫存+期間進貨-期間需求。小明開了一間漢堡店，開店前倉庫裡有12公斤麵包、10公斤\
               生菜、8公斤肉排。今天總共進貨6公斤麵包、7公斤生菜、4公斤肉排，消耗4公斤麵包、6公斤生菜、5公斤肉排。請問今天結束營業後\
               肉排的期末庫存為？",
               "5公斤","7公斤"],
              [2,"訂單達成率：給定時間內實際完成訂單的百分比。小明開了一間漢堡店，今天午餐時段售出100個漢堡、晚\
               餐時段售出300個漢堡，但實際上因為缺貨還有100個訂單沒有被滿足。請問漢堡店今天的訂單達成率為？",
               "80%","90%"],
              [3,"前置時間：指從買方開始下單訂購到賣方交貨所間隔的時間。小明開了一間漢堡店，顧客下單後需要經過以下程序：\
               服務生與廚房確認訂單(10秒)→廚房製作漢堡(320秒)→服務生出餐(30秒)。請問顧客訂購一個漢堡的前置時間為？",
               "3分鐘","6分鐘"],
              [2,"毛利率：毛利率計算的是產品的成本以及收入的關係，毛利率計算公式＝(銷售收入－銷售成本) / 銷售收入 x 100%。\
               小明開了一間漢堡店，一個漢堡售價60元，已知漢堡的材料麵包、生菜、肉排成本分別是10元、15元、20元。請問一個漢堡的毛利\
               率為？",
               "75%","85%"],
              [3,"營收：又稱為營業額，是指企業在某段時間內，經由商業行為取得的收入。小明開了一間漢堡店，總共販售三種品項包括雞塊\
               、沙拉與漢堡，售價分別為40元、30元、60元。已知今日雞塊、沙拉與漢堡分別售出10份、20份、15份。請問漢堡店今天的營收為？",
               "1,500元","1,900元"],
              [2,"固定成本：不會隨著營業收入變動而變動的成本，包括店面租金、機械設備租金、人事費等等。小明開了一間漢堡店，店裡\
               聘僱了一位正職員工月薪20,00元，機器租金每年120,00元、店面租金每月50,00元。請問漢堡店每個月的固定成本為？",
               "8,000元","19,000元"]]
ques_dict2 = dict()
for i in range(len(ques_list1)):
    ques_dict2[i+1] = ques_list1[i]