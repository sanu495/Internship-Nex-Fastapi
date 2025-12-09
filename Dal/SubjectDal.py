from GenericDal import GenericDal
from sqlmodel import Session
from schema import Subject

class SubjectDal(GenericDal[Subject]):
    def __init__(self, db: Session):
        super().__init__(Subject, db)