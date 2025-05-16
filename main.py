from fastapi import FastAPI
from fetch import FetchFromMongo

app = FastAPI()
url = 'https://leetcode.com/problemset/'
mongo = FetchFromMongo(url)
mongo.fetch_data_and_insert_in_mongo()


@app.get('/analyze/leetcode/problemset/')
def extract():
    data = mongo.get_all_data()
    return data
