# 내 코드
lst = ['c=','c-','dz=','d-','lj','nj','s=','z=']
croatia = input()


# def a(croatia):
#     word = []

#     def new(croatia):
#         while len(croatia) >= 1:
#             if croatia[0:2] in lst :
#                 word.append(1)
#                 new(croatia.replace(croatia[0:2],'',1))
#             elif croatia[0:3] in lst:
#                 word.append(1)
#                 new(croatia.replace(croatia[0:3],'',1))
#             else:
#                 word.append(1)
#                 new(croatia.replace(croatia[0],'',1))
#             break
            
#     new(croatia)
#     return sum(word)

#print(a(croatia))

# 더 쉬운 접근
for i in lst:
    croatia = croatia.replace(i,'*')
print(len(croatia))

