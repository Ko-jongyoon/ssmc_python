# with문을 사용하여 close 처리및 기타 닫는 보정
# 비정상 종료를 없애고 -> try~
# 정상적인 처리 부분의 틀을 완성했다
import pymysql as my

connection = None
try:
    connection = my.connect(host='localhost',        #디비 주소
                             user='root',         #디비 접속 계정
                             password='12341234', #디비 접속 비번
                             db='python_db',      #데이터베이스 이름
                             #port=3306,           #포트
                             charset='utf8',
                             cursorclass = my.cursors.DictCursor) # 커서타입지정

    if connection:
        print("디비 오픈")
    ############################################################
    # 커서의 종류를 my.cursors.DictCursor로 지정
    with connection.cursor() as cursor:
        sql = "select * from users where uid='m' and upw='1';"
        cursor.execute ( sql )
        row = cursor.fetchone()
        # {'id': 1, 'uid': 'm', 'upw': '1', 'name': '멀티', 'regdate': datetime.datetime(2019, 1, 7, 14, 15, 41)}
        print( row )
        print ("%s님 반갑습니다." % row['name'] )
        #cursor.close()
    ############################################################
    
except Exception as e:
    print('->', e)
finally:
    if connection:
      connection.close()
      print('디비 닫기')