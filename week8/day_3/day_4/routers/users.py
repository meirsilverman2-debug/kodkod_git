from fastapi import APIRouter

router = APIRouter(prefix="/users", tags=["users"])

@router.get("")
def get_all():
    return {"Message": "momo"}
