#######################################
# 내장함수 중 이해하기 어려운 스타일
# filter, lambda, map
#######################################
# 아래 데이터중에 구성원값이 0보다 큰 값만 모아서 
# 리스트로 반환하시오
tmp = [ 1, -2, 0, 4, 6, -3 ]
dump = list()
for t in tmp:
    if t>0:
        print( t )
        dump.append(t)
print( dump )
#######################################
# filter() 제공 : 걸러낸다
# check : 실제 필터링 작업을 수행하는 콜백함수
# => 대상이되면 True, 대상이 아니면 False 반환
# => 대상 => 데이터 하나 하나
def check(x):
    return x>0
print( list( filter( check, tmp )))
#######################################
# map() : 대상 데이터를 전체적으로 작업할때
# 데이터를 일괄적으로 2배 증가시켜라
def scale(x):
    return 2*x

print( list( map( scale,tmp ) ) )
#######################################
#데이터중에 음수는 다 0으로 보정 처리
def scale2(x):
    if x<0:
        return 0
    return x

print( list( map( scale2,tmp ) ) )
# lambda => 함수를 좀 더 간결하게 표현이 가능하고
# 메모리적으로 함수보다는 월등하게 효과적이다
# 코드가 끝나면 소멸된다
print( list( map( lambda x: 2*x, tmp ) ) )





