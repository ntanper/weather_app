
class Location:
    """
    A class containing location data for our weather forecast
    """
    def __init__(self, zip_code):
        self.zip_code = zip_code

    def __call__(self, *args, **kwargs):
        print(f'ZIP CODE : {self.zip_code}')

    def __str__(self):
        return f'ZIP CODE : {self.zip_code}'
