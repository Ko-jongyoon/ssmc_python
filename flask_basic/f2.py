from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return 'hello world3'
if __name__ == '__main__':# 이코드를 메인으로 구동시 서버가동
    app.run(debug=True)
    