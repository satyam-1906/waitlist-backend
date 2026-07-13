from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session
from fastapi.middleware.cors import CORSMiddleware
from schemas import WaitlistSchema
from database import sessionLocal, formData

app = FastAPI()

origins = ['http://localhost:5503', 'http://127.0.0.1:5501', 'http://127.0.0.1:5502', 'http://127.0.0.1', '0.0.0.0']

app.add_middleware(CORSMiddleware,
                   allow_origins = ["*"],
                   allow_credentials = True,
                   allow_methods = ['*'],
                   allow_headers = ['*'])


def get_db():
    db=sessionLocal()
    try:
        yield db 
    finally:
        db.close()

@app.get("/")
def check():
    return {"status": "Running"}


@app.post('/add')
def add(payload: WaitlistSchema, db: Session=Depends(get_db)):
    new_record = formData(
        name = payload.name,
        email = payload.email,
        mobile_number = payload.mobile_number,
        location = payload.location,
        occupation = payload.occupation
    )
    db.add(new_record)
    try:
        db.commit()
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=f'Error: {str(e)}')
    db.refresh(new_record)
    return new_record
