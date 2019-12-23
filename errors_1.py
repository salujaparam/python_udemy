class RunTimeErrorWithCode(Exception):
    """
    Exception raised when a specific error code is needed
    """
    def __init__(self, message, code):
        super().__init__(f'Error code {code}: {message}')
        self.code = code

# raise RunTimeErrorWithCode('Ouch an error occured.', 500)

err = RunTimeErrorWithCode('An error happend', 500)
print(err.__doc__)