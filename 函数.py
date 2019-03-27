# coding:utf8
#默认函数


def chengfabiao(row):
    for col in range(1, row+1):
        print(row*col, end=" ")
    print("")


for row in range(1, 10):
    chengfabiao(row)


def reg(name, age, gendle="male"):
    if gendle == "male":
        print("{0} is{1},and he is a good student".format(name, age))
    else:
        print("{0} is{1},she is a good student".format(name, age))


reg("li hao bin", 23)


# 关键字函数

def role(name=" ", age="", address=" "):
    print("i am {0}, {1}years old, live in {2}".format(name, age, address))


role(name="li hao bin", age=23, address="bai yun qu")


# 收集参数  *
def coll(*args):
    print(type(args))
    for item in args:
        print(item)


coll("li hao bin", "watch book", "play game")

# 关键字收集参数


def coll(**infor): #kwargs
    print(type(infor))
    for k, v in infor.items():
        print(k, "*"*5, v)


coll(name="li hao bin", hobby="play games", age=23)

#混合使用  优先普通参数跟关键字参数