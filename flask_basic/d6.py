# sql문에 아이디나 비번을 동적으로 세팅하기
# sql문에 파라미터 전달하기
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
    with connection.cursor() as cursor:
        # 파라미터 자리를 '' 포함해서 %s로 대체
        # 'm' => %s
        # 방법1
        sql = "select * from users where uid=%s and upw=%s;"
        cursor.execute ( sql, ('m', '1') )

        # 방법2 :적절히 섞어서 사용한다(적합한 타이밍이 나온다)
        # select * from users where uid=m and upw =1;
        #sql = "select * from users where uid='%s' and upw='%s';" %('m','1')
        #cursor.execute ( sql )
        
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