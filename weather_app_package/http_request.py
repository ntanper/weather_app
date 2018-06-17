class HttpReq:
    def __init__(self, zipcode):
        self.host = 'https://www.wunderground.com/'
        self.url = self.host + 'weather_forecast/' + str(zipcode)

    def __call__(self, *args, **kwargs):
        print(f'URL : {self.url}')

    def __str__(self):
        return f'URL : {self.url}'
