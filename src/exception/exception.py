class UnauthorizedException(Exception):
    def __init__(self, message='unauthorized'):
        self.message = message
        self.status = 500


class NotFoundException(Exception):
    def __init__(self, message='Not Found!'):
        self.message = message
        self.status = 404
