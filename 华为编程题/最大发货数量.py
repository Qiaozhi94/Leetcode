# 最大发货数量
# 2022-07-18
# 假设有 numPacks 个货车和 numGoods 件货物，每个货车的容量为 packs[i]，每件货物的体积为 goods[j]，只有 packs[i] >=goods[j]的货车才可以装下对应货物.
# 给定一组货车和货物，计算这些货车能够运输货物的最大体积和，并返回该最大值。
# 输入
# 首行一个整数 numPacks，表示货车的数量
# 第二行是 numPacks 个整数，表示货车容量的数组 packs
# 第三行一个整效numGoods， 表示待运输货物的件数
# 第四行是 numGoods 个垫数，表示货物体积的数组 goods
# 1 <= numPacks, numGoods <= 1000
# 1 <= packs[i], goods[j] <= [1, 10000]
# 输出
# 一个整数，表示可以运输货物的体积之和的最大值


num_packs = 4
packs = [3,4,7,9]
num_goods = 2
goods = [1,2]

packs.sort()
goods.sort()
max_goods = 0
num = 0
for i in range(1, num_packs+1):
  for j in range(1+num, num_goods+1):
    if packs[-i] >= goods[-j]:
      max_goods = max_goods + goods[-j]
      num = num + 1
      break
    if packs[-i] < goods[-j]:
      continue

print(max_goods)
