from fastapi import FastAPI,APIRouter
from models.refferalModel import refferal
from controllers.refferalController import get_all_refferal,get_a_refferal,create_refferal,update_refferal,delete_refferal


app=FastAPI()
router=APIRouter()


@router.get("/vr-wedding/refferal", tags=["Refferal"],summary="get all refferal ",description="Get the list of all the refferals")
async def root():
    response=get_all_refferal()
    return {"Response":response}

@router.get("/vr-wedding/refferal/{id}", tags=["Refferal"],summary="get a refferal ",description="Get the detail of single refferal")
async def root(id):
    response=get_a_refferal(id)
    return {"Response":response}

@router.post("/vr-wedding/refferal/create", tags=["Refferal"],summary="Create a new refferal ",description="Create a new refferal")
async def root(data:refferal):
    response=create_refferal(data)
    return {"Response":response}

@router.patch("/vr-wedding/refferal/{id}", tags=["Refferal"],summary="update a refferal ",description="update a refferal")
async def root(id,profession,name,city):
    response=update_refferal(id,profession,name,city)
    return {"Response":response}

@router.delete("/vr-wedding/refferal/{id}", tags=["Refferal"],summary="delete a refferal ",description="delete a refferal")
async def root(id):
    response=delete_refferal(id)
    return {"Response":response}