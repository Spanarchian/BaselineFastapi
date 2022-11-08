from fastapi import APIRouter

router = APIRouter(
    prefix="/media",
    tags=["media"],
    # dependencies=[Depends(get_token_header)],
    responses={404: {"description": "Not found"}},
)

vlogs={
        "southcoastpy":{'ref' : '48A4C8C5-DD82-4478-9FFB-2D53E9B8AEC4', 'title' : 'southcoastpy', 'creator' : 'southcoastpy@gmail.com', 'type' : 'creator', 'desc' : 'Pontypridd', 'duration' : '1hr', 'level (All / Sub)' : 'all', 'till' : '-'},
        "itestedthis1":{'ref' : '8BA356B3-828B-42EE-A613-3D60D12CE701', 'title' : 'itestedthis1', 'creator' : 'itestedthis1@gmail.com', 'type' : 'mediator', 'desc' : 'Cardiff', 'duration' : '1hr', 'level (All / Sub)' : 'sub', 'till' : 'End Oct'},
        "quantumofhope":{'ref' : '426826D6-EC4E-4D61-A6BA-26E284C4C1E3', 'title' : 'quantumofhope', 'creator' : 'aquantumofhope@gmail.com', 'type' : 'admin', 'desc' : 'Treforest', 'duration' : '1hr', 'level (All / Sub)' : 'all', 'till' : '-'},
        "spanarchian":{'ref' : '71D543B5-6884-4FE4-AEF8-AD98D35A6B83', 'title' : 'spanarchian', 'creator' : 'spanarchian@gmail.com', 'type' : 'reader', 'desc' : 'Rydr', 'duration' : '1hr', 'level (All / Sub)' : 'sub', 'till' : 'End Nov'},
        "colin":{'ref' : '6F2B2369-6392-4B31-A238-EA65EDE57C65', 'title' : 'colin', 'creator' : 'colin.moore.hill@gmail.com', 'type' : 'subscriber', 'desc' : 'Vancouver', 'duration' : '1hr', 'level (All / Sub)' : 'all', 'till' : '-'}
    }

blogs={
        "southcoastpy":{'ref' : '48A4C8C5-DD82-4478-9FFB-2D53E9B8AEC4', 'title' : 'southcoastpy', 'creator' : 'southcoastpy@gmail.com', 'type' : 'creator', 'desc' : 'Pontypridd', 'duration' : '1hr', 'level (All / Sub)' : 'all', 'till' : '-'},
        "itestedthis1":{'ref' : '8BA356B3-828B-42EE-A613-3D60D12CE701', 'title' : 'itestedthis1', 'creator' : 'itestedthis1@gmail.com', 'type' : 'mediator', 'desc' : 'Cardiff', 'duration' : '1hr', 'level (All / Sub)' : 'sub', 'till' : 'End Oct'},
        "quantumofhope":{'ref' : '426826D6-EC4E-4D61-A6BA-26E284C4C1E3', 'title' : 'quantumofhope', 'creator' : 'aquantumofhope@gmail.com', 'type' : 'admin', 'desc' : 'Treforest', 'duration' : '1hr', 'level (All / Sub)' : 'all', 'till' : '-'},
        "spanarchian":{'ref' : '71D543B5-6884-4FE4-AEF8-AD98D35A6B83', 'title' : 'spanarchian', 'creator' : 'spanarchian@gmail.com', 'type' : 'reader', 'desc' : 'Rydr', 'duration' : '1hr', 'level (All / Sub)' : 'sub', 'till' : 'End Nov'},
        "colin":{'ref' : '6F2B2369-6392-4B31-A238-EA65EDE57C65', 'title' : 'colin', 'creator' : 'colin.moore.hill@gmail.com', 'type' : 'subscriber', 'desc' : 'Vancouver', 'duration' : '1hr', 'level (All / Sub)' : 'all', 'till' : '-'}
    }

@router.get("/", status_code=201, tags=["media"])
async def read_media():
    return [{"mediaType": "Video"}, {"mediaType": "blog"}]

# @router.get("/{mediaType}", tags=["media"])
# async def read_user(mediaType: str):
#     return {"username": mediaType}

@router.get("/vlogs", status_code=201, tags=["media", "vlog"])
async def list_vlog():
    return vlogs

@router.get("/blogs", status_code=201, tags=["media", "blogs"])
async def list_blogs():
    return blogs