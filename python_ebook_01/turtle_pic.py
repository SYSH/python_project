#! usr/bin/env python
# -*- coding: utf-8 -*-

import turtle,time

turtle.color("purple")    # 线条的颜色
turtle.pensize(2)            # 线条的宽度
turtle.speed(1)          # 画线条的速度
turtle.goto(0,0)          # 以0,0为起点

# 绘制正方形
for i in range(4):
    turtle.forward(100)
    turtle.right(90)

# 绘制五角星
turtle.up()
turtle.goto(0,100)

turtle.down()
turtle.color("blue")
turtle.pensize(2)

for i in range(5):
    turtle.forward(100)
    turtle.right(144)
    
# 画笔移动到点(-150,-120)时不绘图
turtle.up()
turtle.goto(-150,-120)
# 再次定义画笔颜色
turtle.color("red")
# 在(-150,-120)点上打印"Done"
turtle.write("Done")
time.sleep(3)
