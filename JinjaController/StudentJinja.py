from fastapi import APIRouter, Depends, HTTPException, Request, Form
from Models.StudentModels import StudentRequest, StudentResponse, StudentUpdate, StudentContact, StudentClass, StudentForm
from DataDependencyConfig.StudentDataDependencyConfig import get_student_dal
from Dal.StudentDal import StudentDal
from CommonModel import ResponseTo
from starlette import status
from schema import Student
import uuid
from typing import List, Optional
from sqlmodel import Session, select
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse

apirouter = APIRouter(tags=["Student-Jinja"])

templates = Jinja2Templates(directory="StudentTemplates")

@apirouter.get("/", response_class=HTMLResponse)
def home(request:Request):
    return templates.TemplateResponse("home.html",{"request":request})

@apirouter.get("/Studentform", name="student_form", response_class=HTMLResponse)
def get_student_form(request:Request):
    return templates.TemplateResponse("studentform.html",{"request":request})

@apirouter.post("/submit", response_model=ResponseTo[StudentResponse])
def create_Student_form(request:Request, form_data:StudentForm = Form(), dal: StudentDal = Depends(get_student_dal)):
    data= Student(**form_data.model_dump())
    result= dal.create(data)
    value = StudentResponse(**result.model_dump())
    return templates.TemplateResponse("submitform.html",{"request":request, "submit": value})

