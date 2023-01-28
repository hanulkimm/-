n= int(input())

for _ in range(n):
    case = list(map(int,input().split()))

    mean_grade = sum(case[1:])/case[0]

    student = 0
    for i in case[1:]:
        if i > mean_grade:
            student += 1
    a = student/case[0]*100
    print(f'{a:.3f}%')