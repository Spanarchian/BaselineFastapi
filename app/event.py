from fastapi import APIRouter

router = APIRouter(
    prefix="/events",
    tags=["events"],
    # dependencies=[Depends(get_token_header)],
    responses={404: {"description": "Not found"}},
)


@router.get("/", tags=["events"])
async def read_event():
    return [{"eventTitle": "PyConUK"}, {"eventTitle": "DataScienceFestival"}]


@router.get("/{eventTitle}", tags=["events"])
async def read_user(eventTitle: str):
    return {"username": eventTitle}