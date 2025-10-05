import httpx

login_payload = {
  "email": "user@example.com",
  "password": "string"
}

login_response = httpx.post("http://localhost:8000/api/v1/authentication/login", json=login_payload)
login_response_data = login_response.json()

headers = {
  "Authorization": f"Bearer {login_response_data['token']['accessToken']}"
}

user_response = httpx.get("http://localhost:8000/api/v1/users/me", headers=headers)
user_response_data = user_response.json()

print("User response: ", user_response_data)
print("Status code: ", user_response.status_code)

