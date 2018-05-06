from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Images(Base):

    __tablename__ = 'images'

    id = Column(Integer, primary_key=True)
    img_name = Column(String(80), nullable=False, unique=True)

    def __init__(self, img_name):
        self.img_name = img_name


if __name__ == "__main__":
    from sqlalchemy import create_engine
    from settings import DB_URI
    engine = create_engine(DB_URI)
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)