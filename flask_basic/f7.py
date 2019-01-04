# 유저(클라이언트)들이 웹페이지를 요청할때 데이터를 보내고 싶다
# Method 방식 = GET : 데이터를 헤더에 싣고 전송
#              POST : 데이터는 바디에 싣고 전송
# 요청(패킷)= 헤더 + 바디로 구성된다
# 데이터 추출은 request 객체를 통해서 진행한다
###########################################################
'''
GET의 예시 = 주소 + ? + 데이터(키=값&키=값&...)
주소
https://news.naver.com/main/hotissue/read.nhn
물음표
?
데이터
mid=hot&sid1=101&cid=957181&iid=3665469&oid=277&aid=0004388232&ptype=052
'''
from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def home():
    return 'hello world3'

# ~/test?name=multi
# 이렇게 요청하면 데이터를 받아서 출력하는 라우트 처리
# 함수를 구성하시오
@app.route('/test')
def test():
    # get방식으로 데이터 획득하는 방법
    # request.args.get('키')
    name = request.args.get('name')
    print( name )
    return name
# 요청 주소
# http://127.0.0.1:5000/login?uid=가나다&upw=1234
# 화면에 아이디와 비번을 출력하는 해당 페이지를 구성하시오1
@app.route('/login')
def login():
    uid =request.args.get('uid')
    upw =request.args.get('upw') 
    print(uid, upw)
    return uid + upw



if __name__ == '__main__':# 이코드를 메인으로 구동시 서버가동
    app.run(debug=True)
    