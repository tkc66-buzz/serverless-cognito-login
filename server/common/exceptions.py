class DataNotFound(Exception):
    """
    Exception for when the requested data is not in the dynamodb.
    """

    def __init__(self, data_type, pk_dict):
        """
        Initialization
        """
        self.message = f'{data_type} is not found. Key: ' + ', '.join(
            [f'{k}={v}' for k, v in pk_dict.items()])


class LoginFailureException(Exception):
    """
    Exception for when the login returns empty.
    """

    def __init__(self, message):
        """
        Initialization
        """
        self.message = message
