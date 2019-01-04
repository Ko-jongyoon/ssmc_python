# 주소가 추가되면 6~8라인의 코드가 반복되서 해당
# 주소가 요청이오면 처리할 함수를 구성
# 요청 문법
# 브라우저 주소창
# http(프로토콜명) + :// + IP + : + 포트 + / + 세부주소
from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return 'hello world3'

# 라우트 => 세부 페이지를 누가 처리 할 것인지 함수와 매칭시키는
# 역활을 담당, 요청을 분석하여 세부페이지 값을 획득하는 행위
# /users/login 구성하시오
# 회원에 관련된 모든 페이지는 /users 밑으로 두겠다 의미내포
# 이렇게 하나의 (웹/미드웨어) 서비스에서 기능별로 URL을 묶고
# 업무 분담도 가능하게 하는 방식 => blueprint라 한다(고급)
@app.route('/users/login')
def login():
    return 'login page'

if __name__ == '__main__':# 이코드를 메인으로 구동시 서버가동
    app.run(debug=True)
    