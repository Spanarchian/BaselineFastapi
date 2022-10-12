from fastapi import APIRouter

router = APIRouter(
    prefix="/media",
    tags=["media"],
    # dependencies=[Depends(get_token_header)],
    responses={404: {"description": "Not found"}},
)


@router.get("/", tags=["media"])
async def read_media():
    return [{"mediaType": "Video"}, {"mediaType": "blog"}]


@router.get("/{mediaType}", tags=["media"])
async def read_user(mediaType: str):
    return {"username": mediaType}