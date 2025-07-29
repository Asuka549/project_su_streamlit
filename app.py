import streamlit as st
# 會旋轉的寫輪眼
# 寫輪眼模組
import streamlit as st
import turtle
from sharingan import draw_sharingan

def draw_sharingan(t1, x, y, a, b, m, p):
    # 眼球
    t1.penup()
    t1.goto(x, y-300)
    t1.pendown()
    t1.color(a)
    t1.begin_fill()
    t1.circle(300)
    t1.end_fill()

    # 瞳仁
    t1.penup()
    t1.goto(x, y-40)
    t1.pendown()
    t1.color(b)
    t1.begin_fill()
    t1.circle(40)
    t1.end_fill()

    # 勾玉
    for n in range(3):
        t1.penup()
        t1.goto(x, y-200/p)
        t1.seth(0)
        t1.circle(200/p, m)
        t1.pendown()

        t1.color(b)
        t1.circle(200/p, 60 + n * 120)

        t1.lt(195)

        t1.color(b)
        t1.begin_fill()
        t1.circle(40/p, 360 / 2)
        t1.end_fill()
        t1.lt(180)
        t1.color(a)
        t1.begin_fill()
        t1.circle(-20/p, 360 / 2)
        t1.end_fill()
        t1.color(b)
        t1.begin_fill()
        t1.circle(20/p, 360 / 2)
        t1.end_fill()

    # 內圈
    t1.penup()
    t1.goto(x, y-200/p)
    t1.seth(0)
    t1.pendown()
    t1.color(b)
    t1.circle(200/p)

    return None

# 頁面標題（可選）
st.set_page_config(page_title="Dockerized Streamlit")

# 顯示 JSON 格式的訊息
data = {"message": "Hello, Dockerized Flask!"}
st.json(data)

# 寫輪眼動畫
turtle.colormode(255)
t1 = turtle.Turtle()
t1.hideturtle()
t1.speed(0)
screen = turtle.Screen()
screen.bgcolor('black')
screen.tracer(0)

a = 'red'
b = 'black'
x = 0
y = 0
m = 0
dm = 10

while True:
    t1.clear()
    m += dm
    draw_sharingan(t1, x, y, a, b, m, p=None)
    screen.update()

turtle.mainloop()
