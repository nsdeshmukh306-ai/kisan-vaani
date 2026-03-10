from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def root():
    return {'status': 'Kisan Vaani online', 'modules': ['pest', 'seed', 'entitlement']}

