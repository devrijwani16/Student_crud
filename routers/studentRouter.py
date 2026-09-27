from fastapi import APIRouter, Response
from models.studentModel import student
from controllers.studentController import create_student_controller, get_student_controller, update_student_controller, delete_student_controller, get_students_id_controller

studentRouter = APIRouter(
    # means every route inside this router automatically starts with /students.
    prefix= '/students',
    tags= ['students']
    # This grps all api under group named students : Organized
)
# students = []
# id = 0

# Create student
@studentRouter.post('/poststudents')
def create_student(student: student, response: Response):
    return create_student_controller(student, response)

# Get students
@studentRouter.get('/getstudents')
def get_students(response: Response):
    return get_student_controller(response)

# Get student by ID
@studentRouter.get('/getstudent/{studentid}')
def get_students_id(studentid: int, response: Response):
    return get_students_id_controller(studentid, response)

# Delete student
@studentRouter.delete('/deletestudent/{studentid}')
def delete_student(studentid: int, response: Response):
    return delete_student_controller(studentid, response)

# Update student
@studentRouter.put('/updatestudent/{studentid}')
def update_student(studentid: int,updated_student: student, response: Response):
    return update_student_controller(studentid, updated_student, response)
#### All str for mongoDb id:int to id:str