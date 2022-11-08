from fastapi import APIRouter, HTTPException,Request

router = APIRouter(
    prefix="/events",
    tags=["events"],
    # dependencies=[Depends(get_token_header)],
    responses={404: {"description": "Not found"}},
)

eventlist = [{"eventTitle": "PyConUK"}, {"eventTitle": "DataScienceFestival"}]



@router.get("/", status_code=200, tags=["events"])
async def read_event():
    return eventlist


@router.get("/{eventTitle}", status_code=200,  tags=["events"])
async def read_user(eventTitle: str):
    for event in eventlist:
        if event["eventTitle"] == eventTitle:
            return {"Event": eventTitle}
    raise HTTPException(
            status_code=404, detail=f"Event with eventTitle {eventTitle} not found"
        )


@router.post("/create", status_code=201,  tags=["events"])
async def root(request: Request):
    print(f"type:eventlist = {type(eventlist)}")
    resp = await request.json()
    print(f"resp = {resp}")
    print(f"type:resp = {type(resp)}")
    response = eventlist +[{ "eventTitle": "DSF-Online" }]
    print(f"response = {response}")
    print(f"type:response = {type(response)}")
    return {"received_request_body": response}