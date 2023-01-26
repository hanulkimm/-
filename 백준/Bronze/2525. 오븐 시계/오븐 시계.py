time = [input() for _ in range(2)]
hour , min = map(int, time[0].split())
more_min = time[1]

if min + int(more_min) % 60 == 60:
    if hour + int(more_min) // 60 + 1 >= 24:
        print((hour + int(more_min) // 60 + 1) -24 , 0) 
    else: 
        print(hour + int(more_min) // 60 + 1  , 0)
    
elif min + int(more_min) % 60 > 60:
    if  hour + int(more_min) // 60 + 1 >= 24:
        print(hour + int(more_min) // 60 + 1 -24 , (min + int(more_min) % 60)-60 )
    else:
        print(hour + int(more_min) // 60 + 1  , (min + int(more_min) % 60)-60 )
else:
    if hour + int(more_min) // 60 >=24:
        print(hour + int(more_min) // 60 -24 , min + int(more_min) % 60) 
    else:
        print(hour + int(more_min) // 60  , min + int(more_min) % 60) 