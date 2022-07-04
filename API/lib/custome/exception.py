class AbstractError(RuntimeError):
    def __init__(self, msg) -> None:
        self.msg = msg


    def pesan_error(self):
        raise (f'Error : {self.msg}')