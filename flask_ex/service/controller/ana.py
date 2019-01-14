# 주소 : ~/analysis/..
# ~/analysis/init, ~/analysis/proc, ~/analysis/sum
# app라는 실체가 바뀌면(블루프린트로) 주소의 시작방식이 변경이된다
from service.controller import bp_analysis as app

# ~/analysis/init
@app.route('/init')
def init():
    return "analysis init"

# ~/analysis/proc
@app.route('/proc')
def proc():
    return "analysis proc"

# ~/analysis/sum
@app.route('/sum')
def sum():
    return "analysis sum"