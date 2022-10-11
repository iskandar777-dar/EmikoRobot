from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session
 
def start() -> scoped_session:
    engine = create_engine(postgres://wpdrdlyvlkqmeq:9193ba29692e1c8fe2f8558448453743804856bc5c6b89657f867c71fa113130@ec2-3-214-3-162.compute-1.amazonaws.com:5432/d64pmj2phrnhbd)
    BASE.metadata.bind = engine
    BASE.metadata.create_all(engine)
    return scoped_session(sessionmaker(bind=engine, autoflush=False))


BASE = declarative_base()
SESSION = start()
