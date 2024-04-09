from fastapi.testclient import TestClient

from src.main import app, sort_data

client = TestClient(app)


def test_sort_data():
    data = {
        "fruits": ["orange", "apple", "banana"],
        "animals": ["rabbit", "dog", "cat"],
        "cars": ["toyota", "audi", "opel"]
    }

    sort_keys = ["fruits", "cars"]

    result = sort_data(data, sort_keys)

    assert result == {
        "fruits": ["apple", "banana", "orange"],
        "animals": ["rabbit", "dog", "cat"],
        "cars": ["audi", "opel", "toyota"]
    }


def test_sort_endpoint():
    response = client.post("/sort", json={
        "data": {
            "fruits": ["orange", "apple", "banana"],
            "animals": ["rabbit", "dog", "cat"],
            "cars": ["toyota", "audi", "opel"]
        },
        "sortKeys": {"keys": ["fruits", "cars"]}
    })

    assert response.status_code == 200

    expected_result = {
        "fruits": ["apple", "banana", "orange"],
        "animals": ["rabbit", "dog", "cat"],
        "cars": ["audi", "opel", "toyota"]
    }

    assert response.json() == expected_result
