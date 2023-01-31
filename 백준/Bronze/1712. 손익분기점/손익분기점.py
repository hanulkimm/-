fix_cost,flex_cost,nb_cost = map(int, input().split())


if nb_cost - flex_cost <= 0:
    print(-1)
else:
    print(int(fix_cost/(nb_cost - flex_cost)+1))