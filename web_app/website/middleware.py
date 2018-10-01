
def simple_middleware(get_response):
    """

    :param get_response:
    :return:
    """
    def middleware(request):
        response = get_response(request)
        return response
    return middleware

