import requests
import pytest
from assertpy import assert_that
from dotenv import load_dotenv
import os

load_dotenv()

headers = {"x-api-key": os.getenv("X_API_KEY")}


def test_get_single_user_not_found():
  response = requests.get("https://reqres.in/api/users/23")
  assert response.status_code==404
  assert  response.reason == "Not Found"

def test_post_login_successful():
    payload ={
        "email": "eve.holt@reqres.in",
        "password": "cityslicka"
    }
    response = requests.post("https://reqres.in/api/login",json=payload,headers=headers)
    assert_that(response.status_code).is_equal_to(200)
    response_body=response.json()
    assert_that(response_body).contains("token")


def test_post_register_unsuccessful():
    payload =  {
    "email": "sydney@fife"
      }
    response = requests.post("https://reqres.in/api/register", json=payload, headers=headers)
    assert_that(response.status_code).is_equal_to(400)
    response_body = response.json()
    assert_that(response_body).contains_key("error")
    assert response_body["error"]=="Missing password"






