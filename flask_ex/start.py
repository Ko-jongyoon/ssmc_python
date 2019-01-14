from service import create_app

# create_app()가 Flask 객체를 리턴한다
app = create_app()

# 서버가동
if __name__=='__main__':
    host = None
    port = None
    if app.config.get('SERVER_RUN_MODE_IS_REAL'): # 리얼 환경
        host = app.config.get('REAL_URL')
        port = app.config.get('REAL_POST')
    else: # 테스트 환경
        host = app.config.get('TEST_URL')
        port = app.config.get('TEST_PORT')
    app.run(
        host = host,
        port = port,
        debug= app.config.get('SERVER_RUN_MODE_IS_DEBUG'))