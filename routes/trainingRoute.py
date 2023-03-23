from fastapi import FastAPI,APIRouter
from models.trainingModel import training
from controllers.trainingController import get_all_training,get_a_training,create_training,update_training,delete_training


app=FastAPI()
router=APIRouter()


@router.get("/vr-wedding/training", tags=["Training"],summary="get all training ",description="Get the list of all the trainings")
async def root():
    response=get_all_training()
    return {"Response":response}

@router.get("/vr-wedding/training/{id}", tags=["Training"],summary="get a training ",description="Get the detail of single training")
async def root(id):
    response=get_a_training(id)
    return {"Response":response}

@router.post("/vr-wedding/training/create", tags=["Training"],summary="Create a new training ",description="Create a new training")
async def root(data:training):
    response=create_training(data)
    return {"Response":response}

@router.patch("/vr-wedding/training/{id}", tags=["Training"],summary="update a training ",description="update a training")
async def root(id,data):
    response=update_training(id,data)
    return {"Response":response}

@router.delete("/vr-wedding/training/{id}", tags=["Training"],summary="delete a training ",description="delete a training")
async def root(id):
    response=delete_training(id)
    return {"Response":response}

