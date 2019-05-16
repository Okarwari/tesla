#
# def f(a, b=[]):
#     print(b)
#     a.append(2)
#     b.append(2)
#     print('inter', a)
#     print('inter', b)
#
# a = [1]
# b = [1]
# f(a)
# print(a)
# f(a)
# print(a)
#
# f(a, b)
#
# f(a)
# print(a)
#
# print(a)




def func(a, b, c, d, e):
    print(a, b, c, d, e)
func(1, *[1,2], **{"d":1, 'e': 2})