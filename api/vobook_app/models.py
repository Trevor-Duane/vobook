from sqlalchemy import Boolean, Column, ForeignKey, DateTime, Integer, String, func, Text
from sqlalchemy.orm import relationship
from .database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    email = Column(String(255), unique=True, index=True)
    hashed_password = Column(String(255))
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime, nullable=False, server_default=func.now())

    #relationship reference
    books = relationship("Book", back_populates="user")

class Book(Base):
    __tablename__ = "books"

    id = Column(Integer, primary_key=True)
    title = Column(String(255), index=True)  # Renamed from 'book' to 'title' for clarity
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False) 
    uploaded_at = Column(DateTime, nullable=False, server_default=func.now())

    # relationship reference
    user = relationship("User", back_populates="books")
    pages = relationship("Page", back_populates="book")


class Page(Base):
    __tablename__ = "pages"

    id = Column(Integer, primary_key=True)
    book_id = Column(Integer, ForeignKey("books.id"), index=True)
    page_number = Column(Integer, index=True)
    page_text = Column(Text)
    audio_file = Column(String(255))

    # relationship reference
    book = relationship("Book", back_populates="pages")
