from fastapi import FastAPI
from fetch import fetch

app = FastAPI()

@app.get('/analyze/leetcode/problemset/')
def extract():
    url = 'https://leetcode.com/problemset/'
    data = fetch(url)
    # print(data)
    return data
