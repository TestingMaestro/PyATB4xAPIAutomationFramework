import pytest
import allure


@allure.title("Sample Test case1")
def test_sample_tc():
    assert True == True


@allure.title("Sample Test case2")
def test_sample_t2():
    assert True == True
