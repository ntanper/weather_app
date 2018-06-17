
class location:
    """
    A class containing location data for our weather forecast
    """
    def __init__(self, zip_code):
        self.zip_code = zip_code

    def __call__(self, *args, **kwargs):
        print("ZIP CODE : %s" %self.zip_code)