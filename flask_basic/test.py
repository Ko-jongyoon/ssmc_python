#데이터가 덩어리채 온다  ( 구분자(sep..)를 통해서 )
datas = '1000/4/5/3/5/6/3/2'.split('/')
print( datas )
# 합산
# 하나씩 구성원을 뽑는다
addSum = 0
for n in datas:
     addSum += int(n)
     print(addSum)