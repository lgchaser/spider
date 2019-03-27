# coding:utf8
def hano(n, a, b, c):
    """
    汉诺塔递归实现
    :param n: 有几个盘子
    :param a: 开始的塔
    :param b: 过渡的塔
    :param c: 目标塔
    :return: none
    要点在于，首先要从开始的塔通过目标塔把n-1的盘子移动到过渡塔上，把最后一个最大的盘子移动到目标塔上
        hano(n-1, a, c, b)
        print(a, "to", c)
    然后再由过渡塔通过开始的塔把盘子移动到目标塔上
        hano(n-1, b, a, c)
    """
    if n == 1:
        print(a, "to", c)
        return None

    hano(n-1, a, c, b)
    print(a, "to", c)
    hano(n-1, b, a, c)


a = "A"
b = "B"
c = "C"
hano(3, a, b, c)

a = [1, 3, 5, 6, 3, 3]
print(len(a))

a = [["one", 1], ["two", 2], ["three", 3]]
for k, v in a:
    print(k, "-->", v)

a = [1, 4, 5, 2, 5]
b = [m for m in a]
print(b)