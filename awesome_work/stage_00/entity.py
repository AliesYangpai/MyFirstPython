class HttpResponse:
    def __init__(self, success: bool = False, data: dict = None, msg:str = None):
        self.success = success
        self.data = data
        self.msg = msg