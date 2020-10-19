# def feibo(num):
#     n,a,b = 0,0,1
#     while n < num:
#         a,b = b,a+b
#         yield a
#         n += 1
# for i in feibo(12):
#     print(i)

# def func1():
#     print("呵呵哒")
#     yield func2
#     print("嘻嘻嘻")
#     yield
# def func2():
#     print("哈哈哈")
#
# a = func1()
# n = next(a)
# n()
# next(a)

async def func1():
    print("1 start")
    await func2()
    print("1 end")
async def func2():
    print("2 start")
a = func1()
try:
    a.send(None)
except:
    pass