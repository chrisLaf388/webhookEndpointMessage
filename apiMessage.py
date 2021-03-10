import sys
import datetime

# for creating the mapper code
from sqlalchemy import Column, ForeignKey, Integer, String

# for configuration and class code
from sqlalchemy.ext.declarative import declarative_base

# for creating foreign key relationship between the tables
from sqlalchemy.orm import relationship

# for configuration
from sqlalchemy import create_engine

# create declarative_base instance
Base = declarative_base()


# We will add classes here
class SMSFromDiabolo(Base):
    __tablename__ = 'SMSFromDiabolo'

    id = Column(Integer, primary_key=True)
    #dateHeure = Column(datetime, nullable=False)
    ffrom = Column(String(10), nullable=False)
    to = Column(String(10), nullable=False)
    genre = Column(String(500), nullable=False)

    @property
    def serialize(self):
        return {
            'id':self.id,
            #'dateHeure': self.dateHeure,
            'From': self.ffrom,
            'To': self.to,
            'Content': self.genre,
        }


# creates a create_engine instance at the bottom of the file
engine = create_engine('sqlite:///sms-collection.db')
Base.metadata.create_all(engine)