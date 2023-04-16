from fastapi import FastAPI
import redis

app = FastAPI()

r = redis.Redis(host='redis', port=6379)

@app.get("/")
async def root():
    return {"message": "Hello World234"}

@app.get("/hits")
def read_root():
    r.incr("hits")
    return {"number of hits": r.get("hits")}