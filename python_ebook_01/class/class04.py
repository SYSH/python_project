#! usr/bin/env python
# -*- coding: utf-8 -*-

# 演示内部类的使用方法

class Car:
    class Door:                   # 内部类
        def open(self):
            print "open door"

    class Wheel:                  # 内部类
        def run(self):
            print "car run"


if __name__ == "__main__":        # 两种调用方法：
    car = Car()                   # out_name = outclass_name()
    backDoor = Car.Door()         # in_name = out_name.inclass_name()
    frontDoor = car.Door()        # in_name.method()
    backDoor.open()
    frontDoor.open()
    wheel = Car.Wheel()           # 方式二： object_name = outclass_name.inclass_name()
    wheel.run()                   #        object_name.method()
