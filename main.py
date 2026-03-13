from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Allow requests from anywhere (for prototype)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

road_reports = []

class RoadDamage(BaseModel):
    latitude: float
    longitude: float
    damage_level: str

@app.get("/")
def home():
    return {"message": "Autosense Server Running"}

@app.post("/report")
def report_damage(data: RoadDamage):
    road_reports.append(data)
    return {"message": "Damage recorded", "data": data}

@app.get("/reports")
def get_reports():
    return road_reports