from turtle import *

t = 22  # angle  of branches
d = 16  # length of branches
n = 4  # max depth of recursion

X = "F-[[X]+X]+F[+FX]-X"  # Linden mayer System
F = "F"

stack = []


def x(n):
    if n > 0:
        lin(X, n)
    else:
        dot(16, 'green')


def f(n):
    if n > 0:
        lin(F, n)


def lin(s, n):
    pensize(n*2)
    for c in s:
        if c == "-":
            lt(t)
        elif c == "+":
            rt(t)
        elif c == "X":
            x(n-1)
        elif c == "F":
            f(n-1)
            fd(d)
        elif c == "[":
            stack.append((pos(), heading(), n))
        elif c == "]":
            ((i, j), h, p) = stack.pop()
            penup()
            goto(i, j)
            seth(h)
            pensize(p)
            pendown()
penup()
goto(0, -200)
pendown()
seth(90)
color('brown', 'green')
x(n)
