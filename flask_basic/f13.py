# 템플릿 엔진에서 값 찍기
# 전달 : render_template('xx.html', 키 =값, 키 =값, 키 =값 ..)
# 받는쪽(html) : 값출력 => { { 키 } }
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    data=[
        {'rank':1, 'national':'한국'},
        {'rank':2, 'national':'미국'},
        {'rank':3, 'national':'일본'}
    ]
    return render_template('index.html', items=data)
    
if __name__ == '__main__':# 이코드를 메인으로 구동시 서버가동
    app.run(debug=True)
    