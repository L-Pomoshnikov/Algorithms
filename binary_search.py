from random import randint as rnd

a = 1
b = 100
c = rnd(a, b)
print(c)
print('------')

def guess(lbound, ubound, x, i=1):
    y = (lbound + ubound) // 2
    if y == x:
        return i
    elif y < x:
        lbound = y + 1
        return i + guess(lbound, ubound, x)
    elif y > x:
        ubound = y - 1
        return i + guess(lbound, ubound, x)

print('угадано с', guess(a,b,c),'попытки')