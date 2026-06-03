from fastapi import APIRouter

router = APIRouter(prefix="/items", tags=["items"])


@router.get("{item_id}")
def get_all(item_id):
    return {"Message": {item_id}}


@router.get("")
def get_all():
    return {"Message": "momo"}