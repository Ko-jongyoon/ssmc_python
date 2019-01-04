################################################
# 레퍼런스 카운트
# referece count
################################################
# 파이썬은 모든것이 객체다
a = 1
# 1이라는 객체는 나는 만든적이 없다
# 이미 만들어져 있다
# 1이란 객체를 a처럼 가르키고 있는 변수들이 몇개인지
# -> 몇개가 참조하고 있는지 => 래퍼런스 카운트가 몇개인지
import sys
print ( a, type(a), sys.getrefcount(1))
b = 1
print ( b, type(b), sys.getrefcount(1))
# 참조해제
del(b)
print( sys.getrefcount(1) )
del a
print( sys.getrefcount(1) )
# a라는 존재가 완전히 소멸되어서 더이상 사용이 불가하다
# print ( a )