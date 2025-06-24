from fastapi import FastAPI

app = FastAPI()

@app.get('/') # /이하 경로 없음
def read_root(): # def는 함수
    print('출력')
    return {"Hello": "World"} # 들여쓰기 잘못하면 오류남