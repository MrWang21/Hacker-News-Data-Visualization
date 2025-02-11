import requests
import pytest

def test_status_code():
    """Test if HackerNews API responds with status code 200."""

    url = "https://hacker-news.firebaseio.com/v0/topstories.json"
    r = requests.get(url)
    assert r.status_code==200, f"Expected status code 200, but got {r.status_code}"

def test_data_format():
    """Test if the top stories API returns a list of story IDs."""

    url = "https://hacker-news.firebaseio.com/v0/topstories.json"
    response = requests.get(url)
    data = response.json()
    
    assert isinstance(data, list), "Expected a list of story IDs."

@pytest.fixture
def submission_ids():
    url = "https://hacker-news.firebaseio.com/v0/topstories.json"
    r = requests.get(url)
    submission_ids = r.json()
    return submission_ids
    

def test_submission_status(submission_ids):
    """Test if a first 5 submission exists and returns valid data."""

    for submission_id in submission_ids[:5]:
        url =  f"https://hacker-news.firebaseio.com/v0/item/{submission_id}.json"
        r = requests.get(url)

        assert r.status_code==200, f"Expected status code 200, but got ID:{submission_id} got: {r.status_code}"

        response_dict = r.json()
        assert isinstance(response_dict, dict), "Expected a dict of submission ids data."
        assert 'title' in response_dict, "Expected 'title' field in submission data"
        assert 'descendants' in response_dict, "Expected 'descendants' field (comments count) in submission data"