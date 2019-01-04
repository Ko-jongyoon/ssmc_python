# 가장 최소로 구성돈 웹서비스 구성
# 1. flask 모듈 가져오기
from flask import Flask
# 2. Flask 객체 생성
app = Flask(__name__)
# 3. 브라우저에서 사용자가 특정 페이지를 보기 위해서 
# 주소창에 주소 (규약에 맞게)를 치고 엔터를 치면 서버로
# 요청이 들어온다 => 요청을 분석해서 이 주소는 누가 처리해라
# 오더를 내린다 => 라우트 => 라우팅을 수행한다
# '/' => 홈페이지 => 기본 주소나 도메인만 작성한 형태
@app.route('/')
def home():
    return 'hello world3'

# 4. 서버 가동 => 프로그램 가동 =>
app.run(debug=True)









