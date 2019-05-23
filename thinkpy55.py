from __future__ import print_function, division
import turtle

bob = turtle.Turtle()


def koch(t, n):
    """Draws a koch curve with length n."""
    if n < 10:
        t.fd(n)
        return
    m = n/3
    koch(t, m)
    t.lt(60)
    koch(t, m)
    t.rt(120)
    koch(t, m)
    t.lt(60)
    koch(t, m)


def snowflake(t, n):
    for i in range(3):
        koch(t, n)
        t.rt(120)


snowflake(bob, 100)

turtle.mainloop()
