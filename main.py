from fastapi import FastAPI
from database import engine
import models
import uvicorn
from routes import router

models.Base.metadata.create_all(bind=engine)

app = FastAPI(title='Backstract Generated APIs - custom-code-req-coll-ffd9856ca04d45dab0a6c54373ad3b26',debug=False,docs_url='/adoring-sneha-cc2ae504b30711efac320242ac12000338/docs',openapi_url='/adoring-sneha-cc2ae504b30711efac320242ac12000338/openapi.json')

app.include_router(router, prefix='/adoring-sneha-cc2ae504b30711efac320242ac12000338/api', tags=['APIs v1'])

def main():
    uvicorn.run('main:app', host='127.0.0.1', port=8008, reload=True)

if __name__ == '__main__':
    main()