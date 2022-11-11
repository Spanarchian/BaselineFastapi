from fastapi import APIRouter
# from ..schemas.schema_video import Video

router = APIRouter(
    prefix="/video",
    tags=["video"],
    # dependencies=[Depends(get_token_header)],
    responses={404: {"description": "Video Not Found"}},
)

vlogs=[
        {'ref' : '48A4C8C5-DD82-4478-9FFB-2D53E9B8AEC4', 'title' : 'southcoastpy', 'creator' : 'southcoastpy@gmail.com', 'type' : 'creator', 'desc' : 'Pontypridd', 'duration' : '1hr', 'level (All / Sub)' : 'all', 'till' : '-'},
        {'ref' : '8BA356B3-828B-42EE-A613-3D60D12CE701', 'title' : 'itestedthis1', 'creator' : 'itestedthis1@gmail.com', 'type' : 'mediator', 'desc' : 'Cardiff', 'duration' : '1hr', 'level (All / Sub)' : 'sub', 'till' : 'End Oct'},
        {'ref' : '426826D6-EC4E-4D61-A6BA-26E284C4C1E3', 'title' : 'quantumofhope', 'creator' : 'aquantumofhope@gmail.com', 'type' : 'admin', 'desc' : 'Treforest', 'duration' : '1hr', 'level (All / Sub)' : 'all', 'till' : '-'},
        {'ref' : '71D543B5-6884-4FE4-AEF8-AD98D35A6B83', 'title' : 'spanarchian', 'creator' : 'spanarchian@gmail.com', 'type' : 'reader', 'desc' : 'Rydr', 'duration' : '1hr', 'level (All / Sub)' : 'sub', 'till' : 'End Nov'},
        {'ref' : '6F2B2369-6392-4B31-A238-EA65EDE57C65', 'title' : 'colin', 'creator' : 'colin.moore.hill@gmail.com', 'type' : 'subscriber', 'desc' : 'Vancouver', 'duration' : '1hr', 'level (All / Sub)' : 'all', 'till' : '-'}
]


@router.get("/", status_code=200, tags=["video"])
async def read_media():
    return vlogs