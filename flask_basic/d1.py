# pymysql 모듈가져오기
import pymysql as sql

# 디비오픈
connection = sql.connect(host='localhost',        #디비 주소
                             user='root',         #디비 접속 계정
                             password='12341234', #디비 접속 비번
                             db='python_db',      #데이터베이스 이름
                             port=3306,           #포트
                             charset='utf8',)
print("디비 오픈")
# 쿼리수행

# 디비 닫기
connection.close()
print('디비 닫기')