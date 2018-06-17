from weather_app_package import print_class as pc
from weather_app_package import location as loc
from weather_app_package import http_request as req


def main():
    pr = pc.printing('weather app')
    pr.print_header()
    lc = loc.location(35100)
    lc()
    r = req.http_req(lc.zip_code)
    r()


if __name__ == '__main__':
    main()