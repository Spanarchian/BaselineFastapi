from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_get_events():
    response = client.get("/events")
    assert response.status_code == 200
    assert response.json() == [{"eventTitle": "PyConUK"}, {"eventTitle": "DataScienceFestival"}]



def test_get_event_by_name_valid():
    response = client.get("/events/PyConUK")
    assert response.status_code == 200
    assert response.json() == {"Event": "PyConUK"}


def test_get_events_valid():
    response = client.get("/events/PyConUS")
    assert response.status_code == 404
    assert response.json() == {"detail": "Event with eventTitle PyConUS not found"}