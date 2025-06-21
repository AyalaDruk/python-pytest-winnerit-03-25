import requests
import pytest
from assertpy import assert_that
from dotenv import load_dotenv
import os

load_dotenv()

headers = {"x-api-key": os.getenv("X_API_KEY")}
base_url_api ="https://reqres.in/api"

@pytest.mark.api
def test_get_single_user_not_found():
  response = requests.get(f"{base_url_api}/users/23",headers=headers)
  assert response.status_code==404
  assert  response.reason == "Not Found"

@pytest.mark.api
def test_post_login_successful():
    payload ={
        "email": "eve.holt@reqres.in",
        "password": "cityslicka"
    }
    response = requests.post(f"{base_url_api}/login",json=payload,headers=headers)
    assert_that(response.status_code).is_equal_to(200)
    response_body=response.json()
    assert_that(response_body).contains("token")

@pytest.mark.api
def test_post_register_unsuccessful():
    payload =  {
    "email": "sydney@fife"
      }
    response = requests.post(f"{base_url_api}/register", json=payload, headers=headers)
    assert_that(response.status_code).is_equal_to(400)
    response_body = response.json()
    assert_that(response_body).contains_key("error")
    assert response_body["error"]=="Missing password"






