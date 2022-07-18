def countdown(x):
    print(x)
    if x == 0:
        return 
    else:
        countdown(x-1)

print(countdown(10))