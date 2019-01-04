# 요구사항
# /login, /logout 이라는 페이지를 추가 주문
# 응답내용은 알아서
from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return 'home page'

@app.route('/login')
def login():
    return 'login page'

@app.route('/logout')    
def logout():
    return 'logout page'

if __name__ == '__main__':# 이코드를 메인으로 구동시 서버가동
    app.run(debug=True)







