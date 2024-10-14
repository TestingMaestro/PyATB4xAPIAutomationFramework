# integration Scenario

# Create Token
# Create Booking id
# Update the booking (put) --> booking id, token
# Delete the booking (delete) ---> booking id, token

import pytest
import allure
from src.constants.api_constants import APIConstants
from src.helpers.api_requests_wrapper import post_request, patch_request, delete_request, put_request
from src.helpers.payload_manager import payload_create_booking, payload_create_token, payload_update_booking
from src.helpers.common_verification import *
from src.utils.utils import Utils
import logging


class TestCrudBooking(object):
    @pytest.mark.put
    @allure.title("Test CRUD operation Update(PUT).")
    @allure.description(
        "Verify that Full Update with the booking ID and Token is working.")
    def test_update_booking_id_token(self, create_token, get_booking_id):
        put_url = APIConstants().url_put_patch_delete(booking_id=get_booking_id)
        print(put_url)
        response = put_request(url=put_url,
                               headers=Utils().common_header_put_patch_delete_cookie(token=create_token),
                               payload=payload_update_booking(),
                               auth=None,
                               in_json=False)

        verify_http_status_code(response_data=response, expected_data=200)
        verify_response_key(response.json()["firstname"], "Amit")
        verify_response_key(response.json()["lastname"], "Brown")

    @pytest.mark.put
    @allure.title("Test CRUD operation Delete.")
    @allure.description(
        "Verify that delete with the booking ID and Token is working.")
    def test_delete_booking_id(self, create_token, get_booking_id):
        delete_url = APIConstants().url_put_patch_delete(booking_id=get_booking_id)
        print(delete_url)
        response = delete_request(url=delete_url,
                                  headers=Utils().common_header_put_patch_delete_cookie(token=create_token),
                                  in_json=False, auth=None)

        verify_http_status_code(response_data=response, expected_data=201)
        verify_response_delete(response=response.text)
