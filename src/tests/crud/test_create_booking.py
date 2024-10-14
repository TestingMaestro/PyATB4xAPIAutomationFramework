import pytest
import allure
from src.constants.api_constants import APIConstants
from src.helpers.api_requests_wrapper import post_request
from src.helpers.payload_manager import payload_create_booking
from src.helpers.common_verification import *
from src.utils.utils import Utils
import logging

# setting up the logging
logging.basicConfig(level=logging.INFO)


class TestCreateBooking:
    @pytest.mark.positive
    @allure.title("Verify that Create Booking Status and Booking ID shouldn't be null")
    @allure.description(
        "Creating a Booking from the payload and verify that booking id should not be null" +
        "and status code should be 200 for the correct payload")
    def test_create_booking_positive(self):
        logging.info("Starting Test Case #1 - Create Booking")
        response = post_request(
            url=APIConstants().url_create_booking(),
            auth=None,
            headers=Utils().common_headers_json(),
            payload=payload_create_booking(),
            in_json=False
        )
        # Attach the response to Allure
        allure.attach(str(response.text), name="API Response", attachment_type=allure.attachment_type.TEXT)

        # Attach the logs (you can customize this part based on what logs you want to attach)
        logging.info(f"Response Status Code: {response.status_code}")
        logging.info(f"Response Content: {response.text}")

        verify_http_status_code(response_data=response, expected_data=200)
        verify_json_key_for_not_null(response.json()["bookingid"])
        logging.info(response.json()["bookingid"])
        logging.info("End of the TC #1")

    @pytest.mark.negative
    @allure.title("Verify that booking id doesn't work without payload")
    @allure.description("Create booking without payload and verify booking id")
    def test_create_booking_negative(self):
        logging.info("Starting Test Case #2")
        response = post_request(
            url=APIConstants().url_create_booking(),
            auth=None,
            headers=Utils().common_headers_json(),
            payload={},
            in_json=False
        )
        verify_http_status_code(response_data=response, expected_data=500)
        logging.info("End of the TC #2")
