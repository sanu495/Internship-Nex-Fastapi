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

# HOME PAGE 

@apirouter.get("/", response_class=HTMLResponse)
def home(request:Request):
    return templates.TemplateResponse("home.html",{"request":request})

@apirouter.get("/Student", name="student_home", response_class=HTMLResponse)
def get_student_home(request:Request):
    return templates.TemplateResponse("studenthome.html",{"request":request})

# STUDENT HOME PAGE (RESPONSE)

@apirouter.get("/Studentform", name="student_form", response_class=HTMLResponse)
def get_student_form(request:Request):
    return templates.TemplateResponse("studentform.html",{"request":request})

@apirouter.get("/Studentupdate", name="student_update", response_class=HTMLResponse)
def get_student_update(request:Request):
    return templates.TemplateResponse("Studentupdate.html",{"request":request})

@apirouter.get("/Studentclass", name="student_class", response_class=HTMLResponse)
def get_student_class(request:Request):
    return templates.TemplateResponse("StudentClass.html",{"request":request})

@apirouter.get("/Studentcontact", name="student_contact", response_class=HTMLResponse)
def get_student_contact(request:Request):
    return templates.TemplateResponse("StudentContact.html",{"request":request})

@apirouter.get("/Studentsearch", name="student_search", response_class=HTMLResponse)
def get_student_id(request:Request):
    return templates.TemplateResponse("search.html",{"request":request})

@apirouter.get("/error", name="student_error", response_class=HTMLResponse)
def error_message(request:Request):
    return templates.TemplateResponse("error.html",{"request":request})

@apirouter.get("/Studentdetails", name="student_details", response_model=ResponseTo[list[StudentResponse]])
def get_student_details(request:Request, dal: StudentDal = Depends(get_student_dal)):
    result = dal.get_all()
    student_list =[StudentResponse(**student.model_dump()) for student in result]
    return templates.TemplateResponse("studentsDetails.html",{"request":request,"data":student_list})

# STUDENT PAGE (REQUEST)

@apirouter.post("/submit", response_model=ResponseTo[StudentResponse])
def create_Student_form(request:Request, form_data:StudentForm = Form(), dal: StudentDal = Depends(get_student_dal)):
    data= Student(**form_data.model_dump())
    result= dal.create(data)
    value = StudentResponse(**result.model_dump())
    return templates.TemplateResponse("submitform.html",{"request":request, "submit": value})


