#__new__ 魔术方法
# 实例对象的时候触发,负责对象的创建与否
class Human:
    def __new__(cls,limit):
        if isinstance(limit,int):
            return super().__new__(cls)
    def __init__(self,limit):
        print("哈哈哈哈")
a = Human('he')
print(a)
