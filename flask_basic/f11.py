# 주소 뒤에 / 를 붙이는 여부
# ~/pro
# ~/pro/
# 이 2개의 주소를 같은것으로 볼 것인가?
from flask import Flask

app = Flask(__name__)

# ~/pro/ => 404 not found : 존재하지 않는 페이지
@app.route('/pro')
def home():
    return 'hello world3'
    
#~/pro2/, ~/pro2 허용 하겠다면
@app.route('/pro2/')
def pro2():
    return 'hello world123'

if __name__ == '__main__':# 이코드를 메인으로 구동시 서버가동
    app.run(debug=True)
    