# 中间件:接口. 对外提供数据,定制一个标准.
# 鸭子类型
# 鸭子测试:当一只鸟,叫起来像鸭子,走起来像鸭子,游起来像鸭子,那么这只鸟就可以称之为鸭子.
# 只要有对象符合这个标准,就可以调用该接口.
# 多态性.多态:一类事物有多种形态.依赖:继承  多态性:向不同对象发送同一条消息,不同对象会给不同的回应.依赖:接口
# class Duck:
#     def quack(self):
#         print("鸭子嘎嘎嘎")
#     def walk(self):
#         print("鸭子摇摇摆摆")
#     def swim(self):
#         print("鸭子游泳")
# class Bird:
#     def quack(self):
#         print("鸟嘎嘎嘎")
#     def walk(self):
#         print("鸟蹦蹦跳跳")
#     def swim(self):
#         print("鸟游泳")
# class Human:
#     def quack(self):
#         print("人嘎嘎嘎")
#     def walk(self):
#         print("人蹦蹦跳跳")
#     def swim(self):
#         print("人游泳")
# def api(duck): # 接口:接受quack,swim,walk三个方法的对象
#     duck.quack()
#     duck.swim()
#     duck.walk()
# api(Duck())
# api(Bird())
# api(Human())
name = "hehe"