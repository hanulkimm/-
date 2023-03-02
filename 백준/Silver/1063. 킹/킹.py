dct = {'R': (0,1), 'L': (0, -1), 'B':(1,0), 'T':(-1,0), 'RT':(-1,1), 'LT':(-1, -1), 'RB':(1, 1), 'LB':(1, -1)}

king, rock, n = input().split()
n = int(n)
sk, ek  = 8 - int(king[1]), ord(king[0])-65  # 행, 열 idx로 변환
sr, er = 8 - int(rock[1]), ord(rock[0])-65

for _ in range(n):
    ch = input()
    di, dj = dct[ch]
    ni_k,nj_k = sk + di, ek + dj

    if 0<=ni_k<8 and 0<=nj_k<8:
        if (ni_k,nj_k)!=(sr,er):
            sk,ek = ni_k, nj_k
        else:
            ni_r, nj_r = sr + di, er + dj
            if 0<=ni_r<8 and 0<=nj_r<8:
                sr, er = ni_r,nj_r
                sk, ek = ni_k, nj_k


ans_king = [chr(ek+65), 8-sk]
print(*ans_king,sep='')
ans_rock = [chr(er+65), 8-sr]
print(*ans_rock, sep='')