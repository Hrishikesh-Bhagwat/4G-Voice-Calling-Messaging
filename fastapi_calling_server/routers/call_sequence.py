from fastapi import APIRouter

router = APIRouter()

@router.post("/")
def start_call_sequence():
    pass