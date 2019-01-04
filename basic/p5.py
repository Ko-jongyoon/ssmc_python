'''
2. 여러개 데이터 (연속 데이터, 시퀀스 데이터)
- 리스트   :
[],
순서가 존재,
인덱스 존재(0,1,2~..),
값의중복허용
 '''
# None : 값이 없다
nums = None
# 리스트 생성
nums = []
print( nums, type(nums), len(nums))
# 리스트 객체 생성
# 동적으로 생성되는방식이며, 반복작업시 안정적이다
nums =list()
print( nums, type(nums), len(nums))
# 10이하 양의 정수들의 리스트 생성
nums = [1,3,5,7,9]
print( nums, type(nums), len(nums))
anis=['dog','cat','bird']
print( anis, type(anis), len(anis) )
# 리스트 구성원들의 타입을 동일해야 하는가? (x)
ext=[1,2,4,'dog','cat']
print(ext,type(ext),len(ext))
# 차원이 달라지면
nums = [1,3,5,7,9,[1,2,3]]
print( nums, type(nums), len(nums))
############################################
# 인덱싱
# nums 리스트에 7값을 출력하시오
print (nums[3])
# nums 리스트에 2값을 출력하시오
print (nums[-1][1] )
print("_"*50)
print(nums)
print(nums[-1])
print(nums[-1][1])
###########################################

# 슬라이싱
nums= [1,3,5,7,9]
#3,5,7만 회득한 리스트를 출력
print( nums[1:-1] )
# 원본은 그대로 보존
print( nums )
# 복사
print( nums[:] )
# 구성원 1을 2로 변경하고 싶다 =>원본 수정
nums[0] = 2
print( nums )
# 범위 변경-> 범위개수가 값의 개수가 다른 경우
# 그 범위값은 대입하는 값을 치환 (개수가 줄어들 수 있다)
# 범위의 값 대입시 시퀀스 형식만 가능.
nums[1:-1]= 'A'
print (nums)
# 결과: [2,'A', 9]
########################################## 
# 삭제 
nums =[1,3,5,7,9]
# 0번 인덱스 삭제-> 인덱스의 변화를 일으킨다
del nums[0]
print(nums)
print(nums[0])
# 범위 삭제
del nums[:2]
print(nums)
# 값이 일치하면 삭제
nums.remove(7)
print(nums)
# 완전삭제
nums.clear()
print(nums)
###############################################
# 추가
nums.append(100)  
print(nums)
# 추가한 내요을 한 덩어리로 보고 덩어리체 구성원에 포함
nums.append([1,2])
print(nums)
# 구성원을 원 리스트에 멤버로 하나씩 입력
nums.extend([3,4])  
print(nums)
###############################################
# 정렬-> 원본 조작(왠만하면 사본에서 정렬하는게 유리함)
nums =[32,23,6,8,9,5,3,5,67,3,4,87,1,7]
nums.sort()
#오름
print(nums)
nums.sort( reverse=True )
#내림
print(nums)