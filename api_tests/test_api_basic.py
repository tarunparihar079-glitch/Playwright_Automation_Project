from playwright.sync_api import Playwright
import os
from dotenv import load_dotenv

load_dotenv()

def test_get_user_list(playwright: Playwright):
    print("\n---> Sending request to the server...")

    api_request_context = playwright.request.new_context()

    response = api_request_context.get(f"{os.getenv("API_URL")}?page=2")

    assert response.ok, f"API failed! Status code: {response.status}"
    assert response.status == 200
    print("---> The server returned a success (200) status.")

    response_data = response.json()
    print("\n---> This data has come from the serever.")
    print(response_data)

    assert response_data["page"] == 2
    assert "data" in response_data
    print("---> Test passed: The data is absolutely correct!")

    api_request_context.dispose()

def test_create_user(playwright: Playwright):
    print("\n---> Sending request for craete new user...")

    api_request_context = playwright.request.new_context()

    payload = {
        "name" : "morpheus",
        "job" : "leader"
    }

    response = api_request_context.post(os.getenv("API_URL"),data = payload)

    assert response.ok
    assert response.status == 201,f"New user not created! Status: {response.status}"
    print("---> The server returned a success(201 Created) status.")

    response_data = response.json()
    print("\n---> Server sent this response after saved:")
    print(response_data)

    assert response_data["name"]  == "morpheus"
    assert response_data["job"] == "leader"

    api_request_context.dispose()

def test_update_user(playwright: Playwright):
    print("---> Request for update user data...")
    api_request_context = playwright.request.new_context()

    payload = {
        "name" : "morpheus",
        "job" : "senior leader"
    }

    response = api_request_context.put(f"{os.getenv("API_URL")}/2",data = payload)

    assert response.ok
    assert response.status == 200

    response_data = response.json()
    print("---> Server responsed after update:")
    print(response_data)

    assert response_data["job"] == "senior leader"

    api_request_context.dispose()

def test_delete_user(playwright: Playwright):
    print("---> Request for delete user on server...")
    api_request_context = playwright.request.new_context()

    response = api_request_context.delete(f"{os.getenv("API_URL")}/2")

    assert response.status == 204
    print("---> Server  returned success(204).")

    api_request_context.dispose()
