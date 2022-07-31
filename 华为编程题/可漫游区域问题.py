# 可漫游区域问题
# 2022-07-18
# 输入
# 首行输入两个整数 m n，取值范围为[1,1000].
# 随后 m 行是用户签约的漫游限制区城的前缀范围，每行格式为 start end，start和end是长度相同的数字字符串，长度范围为[1,6]，且 start <= end.
# 按下来n行是服务区列表，每行一个数字字行串表示一个服务区，长度范国为(6,151.
# 输出
# 亨典宇群序排列的可漫游服务区列表，或字符串 empty
# 样例1
# 输入
# 2 4
# 755 769
# 398 399
# 3970001
# 756000000000002
# 600032
# 755100
# 输出
# 600032
# 3970001

# def get_roaming_area(self, restricts: List[List[str]], areas: List[str]) -> List[str]:
restricts = [['755','769'],['398','399']]
restricts_num = 2
areas_num = 4
areas = ['3970001','756000000000002','600032','755100']



roaming_list_int = []
for i in range(areas_num):
        for j in range(restricts_num):
            if restricts[j][0] <= areas[i][0:len(areas[i])] <= restricts[j][1]:
              break
            else:
              if int(areas[i]) in roaming_list_int:
                continue
              else:
                roaming_list_int.append(int(areas[i]))
roaming_list.sort()
for n in range(len(roaming_list_int)):


print(roaming_list)