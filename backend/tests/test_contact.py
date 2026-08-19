import os, requests, pytest

BASE_URL = os.environ.get('REACT_APP_BACKEND_URL', '').rstrip('/')
if not BASE_URL:
    # Fallback to reading from frontend/.env
    with open('/app/frontend/.env') as f:
        for line in f:
            if line.startswith('REACT_APP_BACKEND_URL='):
                BASE_URL = line.split('=', 1)[1].strip().rstrip('/')


def test_contact_success():
    payload = {
        "name": "TEST_Jean Dupont",
        "phone": "0612345678",
        "city": "Paris 75011",
        "pest": "rats",
        "urgency": True,
        "message": "TEST message d'urgence pour rats dans la cave.",
    }
    r = requests.post(f"{BASE_URL}/api/contact", json=payload, timeout=30)
    assert r.status_code == 200, r.text
    data = r.json()
    assert data.get("status") == "success"
    assert "id" in data


def test_contact_missing_fields():
    r = requests.post(f"{BASE_URL}/api/contact", json={"name": "X"}, timeout=15)
    assert r.status_code in (400, 422)
