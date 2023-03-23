from fastapi import FastAPI,APIRouter
from models.demoModel import demo
from controllers.demoController import get_all_demo,get_a_demo,create_demo,update_demo,delete_demo


app=FastAPI()
router=APIRouter()


@router.get("/vr-wedding/demo", tags=["Demo"],summary="get all demo ",description="Get the list of all the demos")
async def root():
    response=get_all_demo()
    return {"Response":response}

@router.get("/vr-wedding/demo/{id}", tags=["Demo"],summary="get a demo ",description="Get the detail of single demo")
async def root(id):
    response=get_a_demo(id)
    return {"Response":response}

@router.post("/vr-wedding/demo/create", tags=["Demo"],summary="Create a new demo ",description="Create a new demo")
async def root(data:demo):
    response=create_demo(data)
    return {"Response":response}

@router.patch("/vr-wedding/demo/{id}", tags=["Demo"],summary="update a demo ",description="update a demo")
async def root(id,data):
    response=update_demo(id,data)
    return {"Response":response}

@router.delete("/vr-wedding/demo/{id}", tags=["Demo"],summary="delete a demo ",description="delete a demo")
async def root(id):
    response=delete_demo(id)
    return {"Response":response}