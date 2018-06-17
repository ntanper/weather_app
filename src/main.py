from weather_app_package import print_class as pc
from weather_app_package import location as loc
from weather_app_package import http_request as req


def main():
    pr = pc.Printing('weather app')
    pr.print_header()
    lc = loc.Location(35100)
    lc()
    print(lc)
    r = req.HttpReq(lc.zip_code)
    r()


if __name__ == '__main__':
    main()