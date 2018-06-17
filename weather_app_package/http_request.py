class http_req:
    def __init__(self, zipcode):
        self.host = 'https://www.wunderground.com/'
        self.url = self.host + 'weather_forecast/' + str(zipcode)

    def __call__(self, *args, **kwargs):
        print('URL : %s' %self.url)