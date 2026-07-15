from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session
from fastapi.middleware.cors import CORSMiddleware
from schemas import WaitlistSchema
from database import sessionLocal, formData
import keepalive
import validation

app = FastAPI()

origins = ['https://www.vyomplus.in']

app.add_middleware(CORSMiddleware,
                   allow_origins = ["*"],
                   allow_credentials = True,
                   allow_methods = ['*'],
                   allow_headers = ['*'])

keepalive.ping()


def get_db():
    db=sessionLocal()
    try:
        yield db 
    finally:
        db.close()

@app.head("/")
@app.get("/")
def check():
    return {"status": "Running"}

@app.post('/add')
def add(payload: WaitlistSchema, db: Session=Depends(get_db)):
    if validation.user_exists(payload.email, payload.mobile_number, db):
        new_record = formData(
            name = payload.name,
            email = payload.email,
            mobile_number = payload.mobile_number,
            location = payload.location,
            occupation = payload.occupation,
            details = payload.details
        )
        db.add(new_record)
        try:
            db.commit()
        except Exception as e:
            db.rollback()
            raise HTTPException(status_code=500, detail=f'Error: {str(e)}')
        db.refresh(new_record)
        return {"status": "success", "detail": "User added"}
    else:
        return {"status": "failed", "detail": "User already exists"}
