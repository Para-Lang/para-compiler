# coding=utf-8
"""
Test for the project configuration class
"""
from parac.proj_conf import ParacProjectConfig
from . import BASE_TEST_PATH


class TestProjectConfiguration:
    """ Test for the Project Configuration class """

    def test_simple_init(self):
        """ Simple initialisation of the class """
        p = BASE_TEST_PATH / "test_config" / "parac-config-1.json"
        config = ParacProjectConfig(p)
