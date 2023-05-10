n = int(input())
arr = [list(input().split()) for _ in range(n)]
arr.sort(key=lambda x:x[0]) # 이름 오름차순
arr.sort(key=lambda x:int(x[3]), reverse=True) # 수학 내림차순
arr.sort(key=lambda x:int(x[2])) # 영어 점수 오름차순
arr.sort(key=lambda x:int(x[1]), reverse=True) # 국어 내림차순

for lst in arr:
    print(lst[0])