from fastapi import APIRouter

router = APIRouter(
    prefix="/auth",
    tags=["auth"],
    # dependencies=[Depends(get_token_header)],
    responses={404: {"description": "Not found"}},
)

signedIn={}
activeToken=[1,2,3,4,5,6,7]

@router.get("/signin", tags=["event"])
async def read_event():
    return [{"eventTitle": "PyConUK"}, {"eventTitle": "DataScienceFestival"}]

@router.get("/verify", tags=["event"])
async def read_event():
    return [{"eventTitle": "PyConUK"}, {"eventTitle": "DataScienceFestival"}]
