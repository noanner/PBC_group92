# 經營背景
# [情境1, 情境2, 情境3, 情境4]
["您的餐廳開在著名的觀光景點附近，每天會有不同的大型旅行團造訪!",
    "您的餐廳舉辦了為期一周的活動，希望可以推廣並且慶祝各式各樣的節日!",
    "這一周的天氣變化很大，好在你可以先看天氣預報，再決定要備多少料!",
    "這是禍不單行，但也好事成雙的一周，您的餐廳遇到很多突發狀況，您要如何解決呢？"]


# 行事曆---------------------------------------------------------------------
# [第0天, 第1天, 第2天, 第3天, 第4天, 第5天, 第6天]
["固定需求", "印度教", "高中畢旅", "美國人", "健身俱樂部", "阿拉伯人", "佛教徒"]  # 情境1
["固定需求", "33五花肉日", "感恩節", "中秋節", "全球素食日", "兒童節", "情人節"]  # 情境2
["固定需求", "下豪大雨", "出炎熱的大太陽", "風和日麗", "寒流來襲", "颱風天", "無風無雨"]  # 情境3
["固定需求", "大樂透開獎", "店門口道路施工", "對面漢堡王休息一天", "新聞不實報導", "拿到安全衛生許可", "平凡的一天"]  # 情境4


# 小提示----------------------------------------------------------------------
# [第1天的提示, 第4天的提示]
# 情境1
["不吃牛肉豬肉，特愛雞肉，如果沒有咖哩的話，他們寧願少吃點", 
    "健身的巨巨們喜歡選用蛋白質較高的牛肉雞肉，若是有生同這樣碳水低的選擇，他們在愛也不過了，通常可以吃上兩份"]
# 情境2
["韓國人熱愛豬五花肉，甚至將3月3日正式訂為「五花肉日」", 
    "全球素食日是一個完全不能吃肉的節日，連製作的食材都不會有任何的肉"]
# 情境3
["因為午後的豪大雨，導致顧客出門意願降低，只想待在家叫Foodpanda或Ubereats，全品項銷量約減少25%", 
    "寒流來襲，大口大口咬下漢堡，身體有熱量去禦寒，大家喜歡到漢堡店坐在店裡享用，全品項銷售量約增加25%"]
# 情境4
["今日為大樂透開獎，得主就住在餐廳樓上，平常他最愛吃的就是牛肉漢堡，今天他決定拿獎金買下60個請台北車站的流浪漢吃", 
    "新聞報導指控您的餐廳餐點不衛生，漢堡都是用組合肉，生菜也不新鮮，麵包更是都發霉了，讓業績只剩4成"]


# 需求量-----------------------------------------------------------------------
# 情境1
# [牛,豬,雞,菜,酮]
[20,20,20,20,20]  # Day0需求
[3,5,52,62,2]     # Day1需求
[31,28,27,8,11]   # Day2需求
[30,25,28,5,15]   # Day3需求
[21,6,25,12,65]   # Day4需求
[25,3,30,28,18]   # Day5需求
[4,6,8,62,10]     # Day6需求
[[20,20,20,20,20], [3,5,52,62,2], [31,28,27,8,11], [30,25,28,5,15], [21,6,25,12,65], [25,3,30,28,18], [4,6,8,62,10]]


# 情境2
#[牛,豬,雞,菜,酮]
[20,20,20,20,20]  # Day0需求
[18,19,43,15,12]  # Day1需求
[21,18,31,17,19]  # Day2需求
[23,25,28,19,12]  # Day3需求
[0,0,0,110,0]     # Day4需求
[28,26,27,8,13]   # Day5需求
[22,23,21,19,18]  # Day6需求
[[20,20,20,20,20], [18,19,43,15,12], [21,18,31,17,19], [23,25,28,19,12], [0,0,0,110,0], [28,26,27,8,13], [22,23,21,19,18]]

# 情境3
#[牛,豬,雞,菜,酮]
[20,20,20,20,20]  # Day0需求
[16,16,17,15,15]  # Day1需求
[22,23,23,19,21]  # Day2需求
[26,28,27,23,24]  # Day3需求
[24,23,26,24,25]  # Day4需求
[15,14,16,13,16]  # Day5需求
[21,20,22,20,21]  # Day6需求
[[20,20,20,20,20], [16,16,17,15,15], [22,23,23,19,21], [26,28,27,23,24], [24,23,26,24,25], [15,14,16,13,16], [21,20,22,20,21]]

# 情境4
#[牛,豬,雞,菜,酮]
[20,20,20,20,20]  # Day0需求
[81,21,20,19,18]  # Day1需求
[16,13,15,15,16]  # Day2需求
[31,28,29,27,29]  # Day3需求
[8,7,7,8,6]       # Day4需求
[22,23,21,21,22]  # Day5需求
[21,21,21,21,21]  # Day6需求
[[20,20,20,20,20], [81,21,20,19,18], [16,13,15,15,16], [31,28,29,27,29], [8,7,7,8,6], [22,23,21,21,22], [21,21,21,21,21]]
