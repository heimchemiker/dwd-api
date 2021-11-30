# flake8: noqa

"""
    Deutscher Wetterdienst: API

    Aktuelle Wetterdaten von allen Deutschen Wetterstationen  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Contact: kontakt@bund.dev
    Generated by: https://openapi-generator.tech
"""


__version__ = "1.0.1"

# import ApiClient
from deutschland.dwd.api_client import ApiClient

# import Configuration
from deutschland.dwd.configuration import Configuration

# import exceptions
from deutschland.dwd.exceptions import (
    ApiAttributeError,
    ApiException,
    ApiKeyError,
    ApiTypeError,
    ApiValueError,
    OpenApiException,
)