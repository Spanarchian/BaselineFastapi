from fastapi import APIRouter

router = APIRouter(
    prefix="/users",
    tags=["users"],
    # dependencies=[Depends(get_token_header)],
    responses={404: {"description": "Not found"}},
)

users = {
    "u0001" : {"ref": "u0001", "uname": "Spanarchian", "email":"spanarchian@gmail.com", "loc":"Wales", "pword" : "Pas55word!"},
    "u0002" : {"ref": "u0002", "uname": "SouthCoastpy", "email":"southcoastpy@gmail.com", "loc":"England", "pword" : "Pas55word!"},
    "u0003" : {"ref": "u0003", "uname": "Itestedthis1", "email":"itestedthis1@gmail.com", "loc":"Scotland", "pword" : "Pas55word!"},
    "u0004" : {"ref": "u0004", "uname": "QuantumOfHope", "email":"aquantumofhope@gmail.com", "loc":"Ireland", "pword" : "Pas55word!"}
}


@router.get("/", tags=["users"])
async def read_users():
    return [{"username": "Rick"}, {"username": "Morty"}]


@router.get("/me", tags=["users"])
async def read_user_me():
    return users["u0001"]


@router.get("/ref/{ref}", tags=["users"])
async def read_user_by_ref(ref: str):
    return users[ref]