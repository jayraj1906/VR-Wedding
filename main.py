from fastapi import FastAPI
from routes import demoRoutes,refferalRoute,trainingRoute

description = """
This is your asset management api

You can create, delete and update your asset

"""

tags_metadata = [
    {
        "name": "Demo",
        "description": "People who wants to see the demo",
    },
    {
        "name":"Refferal",
        "description":"People refferals"
    },
    {
        "name":"Training",
        "description":"People can enroll themselves for training"
    }
]
app=FastAPI(title="Vr-Wedding",description=description,openapi_tags=tags_metadata)

@app.get("/")
async def root():
    return {"Response":"Welcome to vr-wedding"}

app.include_router(demoRoutes.router)
app.include_router(refferalRoute.router)
app.include_router(trainingRoute.router)