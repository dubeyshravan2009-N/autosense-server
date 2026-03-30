from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from datetime import datetime

app = FastAPI()

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Temporary storage
road_reports = []

# Data model
class RoadDamage(BaseModel):
    latitude: float
    longitude: float
    damage_level: str

@app.get("/")
def home():
    return {"message": "Autosense Server Running"}

# Add report with ID + timestamp
@app.post("/report")
def report_damage(data: RoadDamage):
    report = {
        "id": len(road_reports) + 1,
        "latitude": data.latitude,
        "longitude": data.longitude,
        "damage_level": data.damage_level,
        "timestamp": datetime.now().isoformat()
    }
    road_reports.append(report)
    return {"message": "Damage recorded", "data": report}

@app.get("/reports")
def get_reports():
    return road_reports
