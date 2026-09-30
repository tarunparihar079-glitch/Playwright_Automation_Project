from playwright.sync_api import Playwright
import os
from dotenv import load_dotenv

load_dotenv()

def test_user_lifecycle_chaining(playwright:Playwright):
    api_request_context = playwright.request.new_context()

    print("\n---> 1.Creating new user...")
    create_payload = {
        "name":"neo",
        "job":"the one"
    }

    post_response = api_request_context.post(os.getenv("API_URL"),data = create_payload)
    assert post_response.status == 201
    
    post_data = post_response.json()

    new_user_id = post_data["id"]
    print(f"---> Success! New user created.Server give ID: {new_user_id}")

    print(f"---> 2.Now updating the job of new ID {new_user_id}...")
    update_payload = {
        "name":"neo",
        "job":"matrix hacker"
    }

    dynamic_url = f"{os.getenv("API_URL")}/{new_user_id}"

    put_response = api_request_context.put(dynamic_url,data=update_payload)
    assert put_response.status == 200

    put_data = put_response.json()
    assert put_data["job"] == "matrix hacker"
    print(f"---> Success! Updated job of ID {new_user_id}")

    print(f"---> 3.Now deleting this ID ({new_user_id})...")

    delete_response = api_request_context.delete(dynamic_url)
    assert delete_response.status == 204
    print(f"---> Success! ID {new_user_id} deleted.")

    api_request_context.dispose()