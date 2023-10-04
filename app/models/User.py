from app.db import Base
from sqlalchemy.orm import validates
import bcrypt
from sqlalchemy import Column, Integer, String

salt = bcrypt.gensalt()

class User(Base):
  __tablename__ = 'users'
  id = Column(Integer, primary_key=True)
  username = Column(String(50), nullable=False)
  email = Column(String(50), nullable=False, unique=True)
  password = Column(String(100), nullable=False)

  @validates('email')
  def validate_email(self, key, email):
    # make sure email address contains @ character
    assert '@' in email
    return email
  
  @validates('password')
  def validatE_password(self, key, password):
    # make sure password contains more than 4 characters
    assert len(password) > 4
    return bcrypt.hashpw(password.encode('utf-8'), salt)