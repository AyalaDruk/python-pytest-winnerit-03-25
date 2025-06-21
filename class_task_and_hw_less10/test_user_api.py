import requests
import pytest
from assertpy import assert_that

base_api_url="https://jsonplaceholder.typicode.com/users"

@pytest.mark.api
def test_get_all_user():
 response=requests.get(base_api_url)
 assert response.status_code ==200
 response_body= response.json()
 assert_that(len(response_body)).is_equal_to(10)

@pytest.mark.api
def test_get_user_1():
 response=requests.get(f"{base_api_url}/1")
 assert response.status_code ==200
 response_body = response.json()
 assert_that(response_body["name"]).is_equal_to("Leanne Graham")
 assert_that(response_body["email"]).is_equal_to("Sincere@april.biz")

@pytest.mark.api
def test_get_user_not_exist():
 response = requests.get(f"{base_api_url}/999")
 assert response.status_code == 404
@pytest.mark.api
def test_get_user_3():
  response = requests.get(f"{base_api_url}/3")
  response_body = response.json()
  assert_that(response_body).contains_key("id")
  assert_that(response_body).contains_key("username")
  assert_that(response_body).contains_key("address")
  assert_that(response_body).contains_key("company")

test_data=[
           (1,"Leanne Graham"),
           (2,"Ervin Howell"),
           (3,"Clementine Bauch"),
           (4,"Patricia Lebsack"),
           (5,"Chelsey Dietrich")
           ]
@pytest.mark.api
@pytest.mark.parametrize("id, result", test_data)
def test_get_name_with_param(id,result):
 response = requests.get(base_api_url)
 response_body =response.json()
 assert_that(response_body[id-1]["name"]).is_equal_to(result)


