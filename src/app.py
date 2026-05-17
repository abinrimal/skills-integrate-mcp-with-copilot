"""
High School Management System API

A super simple FastAPI application that allows students to view and sign up
for extracurricular activities at Mergington High School.
"""

from fastapi import FastAPI, HTTPException
from fastapi.staticfiles import StaticFiles
from fastapi.responses import RedirectResponse
import os
from pathlib import Path
import json
from typing import Optional
from pydantic import BaseModel

app = FastAPI(title="Mergington High School API",
              description="API for viewing and signing up for extracurricular activities")

# Session storage (in-memory for now)
sessions = {}  # Format: {session_id: {"username": str}}

# Load teachers from JSON file
def load_teachers():
    """Load teacher credentials from teachers.json"""
    teachers_path = Path(__file__).parent / "teachers.json"
    if teachers_path.exists():
        with open(teachers_path, 'r') as f:
            data = json.load(f)
            return {t['username']: t['password'] for t in data.get('teachers', [])}
    return {}

teachers = load_teachers()

# Pydantic models
class LoginRequest(BaseModel):
    username: str
    password: str

class AuthResponse(BaseModel):
    authenticated: bool
    username: Optional[str] = None

# Mount the static files directory
current_dir = Path(__file__).parent
app.mount("/static", StaticFiles(directory=os.path.join(Path(__file__).parent,
          "static")), name="static")

# In-memory activity database
activities = {
    "Chess Club": {
        "description": "Learn strategies and compete in chess tournaments",
        "schedule": "Fridays, 3:30 PM - 5:00 PM",
        "max_participants": 12,
        "participants": ["michael@mergington.edu", "daniel@mergington.edu"]
    },
    "Programming Class": {
        "description": "Learn programming fundamentals and build software projects",
        "schedule": "Tuesdays and Thursdays, 3:30 PM - 4:30 PM",
        "max_participants": 20,
        "participants": ["emma@mergington.edu", "sophia@mergington.edu"]
    },
    "Gym Class": {
        "description": "Physical education and sports activities",
        "schedule": "Mondays, Wednesdays, Fridays, 2:00 PM - 3:00 PM",
        "max_participants": 30,
        "participants": ["john@mergington.edu", "olivia@mergington.edu"]
    },
    "Soccer Team": {
        "description": "Join the school soccer team and compete in matches",
        "schedule": "Tuesdays and Thursdays, 4:00 PM - 5:30 PM",
        "max_participants": 22,
        "participants": ["liam@mergington.edu", "noah@mergington.edu"]
    },
    "Basketball Team": {
        "description": "Practice and play basketball with the school team",
        "schedule": "Wednesdays and Fridays, 3:30 PM - 5:00 PM",
        "max_participants": 15,
        "participants": ["ava@mergington.edu", "mia@mergington.edu"]
    },
    "Art Club": {
        "description": "Explore your creativity through painting and drawing",
        "schedule": "Thursdays, 3:30 PM - 5:00 PM",
        "max_participants": 15,
        "participants": ["amelia@mergington.edu", "harper@mergington.edu"]
    },
    "Drama Club": {
        "description": "Act, direct, and produce plays and performances",
        "schedule": "Mondays and Wednesdays, 4:00 PM - 5:30 PM",
        "max_participants": 20,
        "participants": ["ella@mergington.edu", "scarlett@mergington.edu"]
    },
    "Math Club": {
        "description": "Solve challenging problems and participate in math competitions",
        "schedule": "Tuesdays, 3:30 PM - 4:30 PM",
        "max_participants": 10,
        "participants": ["james@mergington.edu", "benjamin@mergington.edu"]
    },
    "Debate Team": {
        "description": "Develop public speaking and argumentation skills",
        "schedule": "Fridays, 4:00 PM - 5:30 PM",
        "max_participants": 12,
        "participants": ["charlotte@mergington.edu", "henry@mergington.edu"]
    }
}


@app.get("/")
def root():
    return RedirectResponse(url="/static/index.html")


@app.post("/login")
def login(request: LoginRequest):
    """Teacher login endpoint"""
    if request.username in teachers and teachers[request.username] == request.password:
        # Create a session token (simplified: use username as token)
        session_id = request.username + "_" + str(len(sessions))
        sessions[session_id] = {"username": request.username}
        return {"session_id": session_id, "username": request.username, "message": "Login successful"}
    else:
        raise HTTPException(status_code=401, detail="Invalid username or password")


@app.post("/logout")
def logout(session_id: str):
    """Teacher logout endpoint"""
    if session_id in sessions:
        del sessions[session_id]
        return {"message": "Logout successful"}
    else:
        raise HTTPException(status_code=400, detail="Invalid session")


@app.get("/auth/check")
def check_auth(session_id: str = None):
    """Check if user is authenticated"""
    if session_id and session_id in sessions:
        return AuthResponse(authenticated=True, username=sessions[session_id]["username"])
    return AuthResponse(authenticated=False)


@app.get("/activities")
def get_activities():
    return activities


@app.post("/activities/{activity_name}/signup")
def signup_for_activity(activity_name: str, email: str, session_id: str = None):
    """Sign up a student for an activity (teacher only)"""
    # Check if teacher is authenticated
    if not session_id or session_id not in sessions:
        raise HTTPException(
            status_code=401,
            detail="Authentication required. Only teachers can register students."
        )
    
    # Validate activity exists
    if activity_name not in activities:
        raise HTTPException(status_code=404, detail="Activity not found")

    # Get the specific activity
    activity = activities[activity_name]

    # Validate student is not already signed up
    if email in activity["participants"]:
        raise HTTPException(
            status_code=400,
            detail="Student is already signed up"
        )

    # Add student
    activity["participants"].append(email)
    teacher = sessions[session_id]["username"]
    return {"message": f"Teacher {teacher} registered {email} for {activity_name}"}


@app.delete("/activities/{activity_name}/unregister")
def unregister_from_activity(activity_name: str, email: str, session_id: str = None):
    """Unregister a student from an activity (teacher only)"""
    # Check if teacher is authenticated
    if not session_id or session_id not in sessions:
        raise HTTPException(
            status_code=401,
            detail="Authentication required. Only teachers can unregister students."
        )
    
    # Validate activity exists
    if activity_name not in activities:
        raise HTTPException(status_code=404, detail="Activity not found")

    # Get the specific activity
    activity = activities[activity_name]

    # Validate student is signed up
    if email not in activity["participants"]:
        raise HTTPException(
            status_code=400,
            detail="Student is not signed up for this activity"
        )

    # Remove student
    activity["participants"].remove(email)
    teacher = sessions[session_id]["username"]
    return {"message": f"Teacher {teacher} unregistered {email} from {activity_name}"}
