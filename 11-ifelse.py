# Python 3

# # 彩票号码
# no = "123456"
#
# # 接收输入的彩票信息
# myno = input("请输入你的彩票号码：")
#
# if no == myno:
#     print("恭喜中奖")
# else:
#     print("遗憾！")


import time
now_time = time.localtime()
mday = now_time.tm_mday # 当月天数
wday = now_time.tm_wday # 星期天数,0是星期一,6是星期天
print("今天是："+str(mday)+"号")
if mday <= 15:
    print("上旬")
else:
    print("下旬")

print("今天是星期"+str(wday+1))