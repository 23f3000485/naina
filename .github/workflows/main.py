pip install fastapi uvicorn
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional
import uvicorn

# Parcel Entity
class Parcel(BaseModel):
    tracking_id: str
    description: str

app = FastAPI()

# In-memory storage for parcels
parcels = []

# Get list of all parcels
@app.get("/parcels", response_model=List[Parcel])
def get_parcels():
    return parcels

# Get a parcel with given tracking ID
@app.get("/parcels/{tracking_id}", response_model=Parcel)
def get_parcel(tracking_id: str):
    for parcel in parcels:
        if parcel.tracking_id == tracking_id:
            return parcel
    raise HTTPException(status_code=404, detail="Parcel not found")

# Create a parcel and save it in memory
@app.post("/parcels", response_model=Parcel)
def create_parcel(parcel: Parcel):
    parcels.append(parcel)
    return parcel

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
