lst = [input() for _ in range(2)]
x,y = map(int,lst)
if x>0 and y>0:
    print(1)
elif x>0 and y<0:
    print(4)
elif x<0 and y<0:
    print(3)
else:
    print(2)