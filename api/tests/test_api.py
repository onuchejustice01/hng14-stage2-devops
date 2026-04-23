from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_health():
    res = client.get("/health")
    assert res.status_code == 200

def test_create_job():
    res = client.post("/jobs")
    data = res.json()
    assert "job_id" in data

def test_get_job():
    res = client.post("/jobs")
    job_id = res.json()["job_id"]

    res2 = client.get(f"/jobs/{job_id}")
    assert res2.status_code == 200