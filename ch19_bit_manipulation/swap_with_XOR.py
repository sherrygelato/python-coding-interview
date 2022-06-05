from tkinter import Y


x, y = 9, 4

x = x + y
y = x - y
x = x - y
x, y # (4, 9)

x, y = 9, 4 # 1001, 0100
x = x^y     # 1001^0100 = 1101(13)
y = x^y     # 1101^0100 = 1001(9)
x = x^y     # 1101^1001 = 0100(4)
x, y # (4, 9)

x, y = 10, 40
x, y = (x^y)^x, (x^y)^y
x, y # 40, 10