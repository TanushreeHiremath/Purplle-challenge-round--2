# PROMPT:
# Generate tests for FastAPI retail analytics endpoints.

# CHANGES MADE:
# - Added ST1008 store ID
# - Added funnel response validation


import requests


def test_funnel_api():

    response = requests.get(
        "http://localhost:8000/stores/ST1008/funnel"
    )

    assert response.status_code == 200

    data = response.json()

    assert "entered" in data

    assert "purchased" in data