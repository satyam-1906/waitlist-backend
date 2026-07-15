from database import formData

def user_exists(email, number, db) -> bool:
    user = db.query(formData).filter_by(email=email).first()
    if user is not None and user.number == number:
        return False
    return True