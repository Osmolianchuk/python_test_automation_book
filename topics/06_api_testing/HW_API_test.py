import pytest
import requests
from unittest.mock import patch

# Define schema as a dictionary.
post_schema = {
    "required": ["userId", "id", "title", "body"]
}
# Fixture for headers with authentication token
@pytest.fixture(scope="module")
def headers():
    return {
        "Content-Type": "application/json",
        "Authorization": "Bearer fake_token_1234"
    }
# Fixture for API base URL

@pytest.fixture(scope="module")
def base_url():
    return "https://jsonplaceholder.typicode.com"

# Fetching a Post
def test_fetch_post(base_url, headers):
    post_id = 1
    with patch('requests.get') as mock_get:
        mock_get.return_value.json.return_value = {"userId": 1, "id": post_id, "title": "Title", "body": "Body"}
        mock_get.return_value.status_code = 200

        response = requests.get(f"{base_url}/posts/{post_id}", headers=headers)
        assert response.status_code == 200
        assert "id" in response.json()
# Creating a New Post
def test_create_post(base_url, headers):
    post_data = {"title": "New Post", "body": "Content of the post", "userId": 1}
    with patch('requests.post') as mock_post:
        mock_post.return_value.json.return_value = post_data
        mock_post.return_value.status_code = 201

        response = requests.post(f"{base_url}/posts", headers=headers, json=post_data)
        assert response.status_code == 201
        assert response.json() == post_data
# Updating
def test_update_post(base_url, headers):
    post_id = 1
    updated_data = {"title": "Updated Title", "body": "Updated content", "userId": 1}
    with patch('requests.put') as mock_put:
        mock_put.return_value.json.return_value = updated_data
        mock_put.return_value.status_code = 200

        response = requests.put(f"{base_url}/posts/{post_id}", headers=headers, json=updated_data)
        assert response.status_code == 200
        assert response.json() == updated_data
# Delete
def test_delete_post(base_url, headers):
    post_id = 1
    with patch('requests.delete') as mock_delete:
        mock_delete.return_value.status_code = 204

        response = requests.delete(f"{base_url}/posts/{post_id}", headers=headers)
        assert response.status_code == 204

# Parametrized test
@pytest.mark.parametrize("post_id", [1, 2, 3, 4, 5])  # Testing with 5 different post IDs
def test_fetch_post(base_url, headers, post_id):
    with patch('requests.get') as mock_get:
        mock_data = {
            "userId": 1, "id": post_id, "title": f"Test Title for post {post_id}", "body": "Test Content"
        }

        mock_get.return_value.json.return_value = mock_data
        mock_get.return_value.status_code = 200

        response = requests.get(f"{base_url}/posts/{post_id}", headers=headers)
        assert response.status_code == 200
        # Verify if response data contains all the necessary keys based on the schema
        expected_keys = {"userId", "id", "title", "body"}
        assert expected_keys.issubset(response.json().keys()), "Response missing one or more expected keys"
        # Check the correctness of 'id' field in the response
        assert response.json()["id"] == post_id, f"Expected post ID was {post_id}, but got {response.json()['id']}"
# Press the green button in the gutter to run the script.
def test_fetch_comments(base_url):
    with patch('requests.get') as mock_get:
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = [
            {"id": 1, "name": "Commenter", "email": "test@example.com", "body": "A comment body"}]
        # GET request
        response = requests.get(f"{base_url}/comments")
        assert response.status_code == 200
        assert isinstance(response.json(), list)
        assert "email" in response.json()[0]






