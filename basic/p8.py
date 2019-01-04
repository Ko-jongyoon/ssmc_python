'''
2. 여러개 데이터 (연속 데이터, 시퀀스 데이터)
 - 집합     :     값의 중복 제거시 사용,
                  주로 리스트 구성원의 중복 제거 시 사용

 '''

a = 'helloworld'
# 중복 제거, 순서는 정렬되지 않는다
b = set(a)
# {'w', 'o', 'h', 'l', 'd', 'e', 'r'}
print(b)
c = list(b)
print(c)
c.sort()
print(c)
####################################################
a = set( [1,3,5,7,9,2,6,5,5] )
b = set( [2,4,6,8,1,5,4,4] )
print( a,b )
# 합집합
print( a.union(b) )
print( a.intersection(b) )
# 차집합 (방향)
print( a.difference(b) )
print( b.difference(a) )

