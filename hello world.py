# coding:utf8
year = 0
p = 1000
while p < 2000:
    p = p*(1+0.0387)
    year += 1
    print("第{0}年拿到了{1}元".format(year,p))

for _ in range(1,11):
    print(_)

for _ in ["lihaobin","wangzhiling"]:
    print("i am {0}".format(_))

for row in range(1, 10):
    for col in range(1, row+1):
        print(row*col, end=" ")
    print(" ")
    print("-------------------------")