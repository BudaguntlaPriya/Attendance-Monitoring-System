from fastapi import FastAPI, HTTPException
from pymongo import MongoClient
from pydantic import BaseModel

app = FastAPI()

# MongoDB Connection
client = MongoClient("mongodb://localhost:27017/")
db = client["attendance_db"]
collection = db["students"]

class LoginModel(BaseModel):
    roll_no: str
    password: str

class AttendanceUpdate(BaseModel):
    attendance_count: int

@app.post("/login")
def login(user: LoginModel):
    student = collection.find_one({"roll_no": user.roll_no, "password": user.password})
    if student:
        return {"role": "student", "roll_no": user.roll_no, "name": student.get("name", "Student")}
    raise HTTPException(status_code=401, detail="Invalid Credentials")

@app.get("/get_attendance")
def get_all():
    return list(collection.find({}, {"_id": 0}))

# Subject wise update logic
@app.patch("/update_attendance/{roll_no}/{subject_name}")
def update_attendance(roll_no: str, subject_name: str, data: AttendanceUpdate):
    result = collection.update_one(
        {"roll_no": roll_no, "subject": subject_name}, 
        {"$set": {"attendance_count": data.attendance_count}}
    )
    if result.matched_count == 0:
        raise HTTPException(status_code=404, detail="Student or Subject not found")
    return {"message": "Updated successfully"}