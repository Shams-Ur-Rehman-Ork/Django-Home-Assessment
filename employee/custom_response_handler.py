from rest_framework import status
from rest_framework.status import is_server_error
from rest_framework.views import APIView
from rest_framework.response import Response

from django.conf import settings


class BaseAPIView(APIView):
    """Base class for API views."""

    @staticmethod
    def make_response_body(success=True,
                           payload=None,
                           message="",
                           ):

        """Make standard response body
        :param success
        :param payload
        :param message
        :return : dictionary including all above params
        """
        return {
            "success": success,
            "payload": {} if payload is None else payload,
            "message": message,
        }

    def send_response(
            self,
            success=True,
            status_code=status.HTTP_200_OK,
            payload=None,
            message="",
            **kwargs,
    ):
        """
        Generates response.
        :param success: bool tells if call is successful or not.
        :param status_code: int HTTP status code.
        :param payload:dict  data generated for respective API call.
        :param message: str message.
        :rtype: dict.
        """
        if not success and is_server_error(status_code):
            if settings.DEBUG:
                message = f"error message: {message}"
            else:
                message = "Internal server error."
        return Response(data=self.make_response_body(success, payload, message),
                        status=status_code,
                        **kwargs
                        )

    def send_success_response(self, message, payload=None, **kwargs):
        """compose success response"""
        return self.send_response(
            status_code=status.HTTP_200_OK,
            payload=payload,
            message=message,
            **kwargs,
        )

    def send_created_response(self, message, payload=None, **kwargs):
        """compose response for new object creation."""
        return self.send_response(
            status_code=status.HTTP_201_CREATED,
            payload=payload,
            message=message,
            **kwargs,
        )

    def send_bad_request_response(self, message):
        """compose response for bad request"""
        return self.send_response(
            success=False,
            status_code=status.HTTP_400_BAD_REQUEST,
            message=message,
        )

    def send_not_found_response(self, message="Not found."):
        """compose response for not found request"""
        return self.send_response(
            success=False,
            status_code=status.HTTP_404_NOT_FOUND,
            message=message,
        )
