from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_get_philosophers():
    response = client.get("/philosophers")
    assert response.status_code == 200
    assert response.json() == [
                                {
                                    "name": "Su, Lao",
                                    "time": "6th BC",
                                    "nationality": "Chinese"
                                },
                                {
                                    "name": "Epititus",
                                    "time": "3rd BC",
                                    "nationality": "Greek"
                                },
                                {
                                    "name": "Watts, Alan",
                                    "time": "20th",
                                    "nationality": "English"
                                }
                            ]


def test_get_philosophers_id_0():
    response = client.get("/philosophers/0")
    assert response.status_code == 200
    assert response.json() == {
                                    "name": "Su, Lao",
                                    "time": "6th BC",
                                    "nationality": "Chinese"
                                }

def test_get_philosophers_id_2():
    response = client.get("/philosophers/2")
    assert response.status_code == 200
    assert response.json() == {
                                    "name": "Watts, Alan",
                                    "time": "20th",
                                    "nationality": "English"
                                }

def test_get_philosophers_id_not_found():
    response = client.get("/philosophers/999")
    assert response.status_code == 404
    assert response.json() == { "detail": "Philosopher 999 Not Found" }