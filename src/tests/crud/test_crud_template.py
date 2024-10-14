# integration Scenario

# Create Token
# Create Booking id
# Update the booking (put) --> booking id, token
# Delete the booking (delete) ---> booking id, token

import pytest
import allure
from src.constants.api_constants import APIConstants
from src.helpers.api_requests_wrapper import post_request, patch_request, delete_request, put_request
from src.helpers.payload_manager import payload_create_booking, payload_create_token
from src.helpers.common_verification import *
from src.utils.utils import Utils
import logging


class TestCrudBooking(object):

    def test_update_booking_id_token(self):
        pass

    def test_delete_booking_id(self):
        pass
