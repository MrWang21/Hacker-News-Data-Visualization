import requests

def test_status_code():
    """Test if HackerNews API responds with status code 200."""

    url = "https://hacker-news.firebaseio.com/v0/topstories.json"
    r = requests.get(url)
    assert r.status_code==200, f"Expected status code 200, but got {r.status_code}"