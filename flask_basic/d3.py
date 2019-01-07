# 데이터를 딕셔너리 구조로 받아오기 -> 최초접속시 처리
import pymysql as my


connection = my.connect(host='localhost',        #디비 주소
                             user='root',         #디비 접속 계정
                             password='12341234', #디비 접속 비번
                             db='python_db',      #데이터베이스 이름
                             port=3306,           #포트
                             charset='utf8'
                             ) # 커서타입지정
print("디비 오픈")
############################################################
# 커서의 종류를 my.cursors.DictCursor로 지정
cursor = connection.cursor(my.cursors.DictCursor)
sql = "select * from users where uid='m' and upw='1';"
cursor.execute ( sql )
row = cursor.fetchone()
# {'id': 1, 'uid': 'm', 'upw': '1', 'name': '멀티', 'regdate': datetime.datetime(2019, 1, 7, 14, 15, 41)}
print( row )
print ("%s님 반갑습니다." % row['name'] )
cursor.close()
############################################################

connection.close()
print('디비 닫기')