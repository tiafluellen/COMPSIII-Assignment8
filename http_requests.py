# Write# http_requests.py
import requests  # Import requests library for HTTP requests

class JSONPlaceholder:
    """
    A class to interact with the JSONPlaceholder API using GET, POST, PUT, and DELETE.
    """

    def __init__(self, base_url):
        # Store the base URL (like "https://jsonplaceholder.typicode.com/posts")
        self.base_url = base_url

    def get_request(self):
        """Send a GET request to the base URL."""
        response = requests.get(self.base_url)
        return {
            "status_code": response.status_code,
            "headers": dict(response.headers),
            "content": response.text[:500]  # first 500 chars
        }

    def post_request(self, data):
        """Send a POST request with the given data dictionary."""
        response = requests.post(self.base_url, json=data)
        return {
            "status_code": response.status_code,
            "headers": dict(response.headers),
            "content": response.text[:500]
        }

    def update_user(self, userId, title, body):
        """Send a PUT request to update a user's post with new title and body."""
        url = f"{self.base_url}/{userId}"
        data = {"title": title, "body": body}
        response = requests.put(url, json=data)
        return {
            "status_code": response.status_code,
            "headers": dict(response.headers),
            "content": response.text[:500]
        }

    def delete_user(self, userId):
        """Send a DELETE request to remove a user's post."""
        url = f"{self.base_url}/{userId}"
        response = requests.delete(url)
        return {"status_code": response.status_code}
your code here
