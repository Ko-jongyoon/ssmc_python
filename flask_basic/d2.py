# 쿼리수행
import pymysql as sql


connection = sql.connect(host='localhost',        #디비 주소
                             user='root',         #디비 접속 계정
                             password='12341234', #디비 접속 비번
                             db='python_db',      #데이터베이스 이름
                             port=3306,           #포트
                             charset='utf8',)
print("디비 오픈")

# 2.쿼리수행 
# 2-1 커서 획득
cursor = connection.cursor()
# 2-2 sql 준비
sql = "select * from users where uid='m' and upw='1';"
# 2-3 쿼리 수행
cursor.execute ( sql )
# 2-4 결과 획득: rows 획득 : 결과집합 획득
row = cursor.fetchone()
print( row )
# 이름을 획득해서 "~님 반갑습니다."출력
# 순서를 기반으로 데이터를 획득하면 구조 변경시 자동 대응이 안됞다
# -> 데이터가 딕셔너리로 오게 처리해야 근본 문제해결
print("%s님 반갑습니다." %row[3])
# 2-5 닫아라
cursor.close()


connection.close()
print('디비 닫기')