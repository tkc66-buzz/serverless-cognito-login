import boto3
import os

from server.common.exceptions import LoginFailureException


class Authenticator:
    """
    Class to authenticate the received user.
    """
    def __init__(self, email, password):
        self.__email = email
        self.__password = password

    def get_token(self):
        """
        Get login token related to the inputted email and password.

        :return: token
        """
        client = boto3.session.Session().client('cognito-idp')
        auth_response = client.admin_initiate_auth(
            UserPoolId=os.environ['USER_POOL_ID'],
            ClientId=os.environ['COGNITO_CLIENT_ID'],
            AuthFlow='ADMIN_NO_SRP_AUTH',
            AuthParameters={
                'USERNAME': self.__email,
                'PASSWORD': self.__password
            }
        )

        id_token = auth_response.get(
            'AuthenticationResult', {}).get('IdToken')
        if id_token:
            return id_token
        else:
            raise LoginFailureException('Login failed')
