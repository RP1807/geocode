""""
Author: Rushikesh Pendse
Usage: This module is used to get latitude and longitude of the given city using Google Maps GeoCoding API
"""
import httplib2
import json
import argparse
import sys

GOOGLE_API_KEY = "PASTE_YOUR_API_KEY"


def get_geocode_location(name_of_city):
    url = "https://maps.googleapis.com/maps/api/geocode/json?address=%s&key=%s" % (name_of_city, GOOGLE_API_KEY)
    result = None
    try:
        http_obj = httplib2.Http()
        res, content = http_obj.request(uri=url, method="GET")
        if int(res["status"]) == 200:
            result = json.loads(content)
    except Exception as ex:
        print ex.message
    return result


def get_latitude_longitude(result):
    latitude = None
    longitude = None
    try:
        latitude = result["results"][0]["geometry"]["location"]["lat"]
        longitude = result["results"][0]["geometry"]["location"]["lng"]
    except Exception as ex:
        print ex.message
    return latitude, longitude


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    required_parameter = parser.add_argument_group("Required Named Arguments")
    required_parameter.add_argument("--city", help="Enter name of the city", required=True)
    args = parser.parse_args()
    city = args.city
    print "Getting Latitude and Longitude cordinates for city: %s" % city
    try:
        result = get_geocode_location(name_of_city=city)
        latitude, longitude = get_latitude_longitude(result=result)
        print "Latitude: %s \n" % str(latitude)
        print "Longitude: %s \n" % str(longitude)
    except Exception as ex:
        print ex.message
        sys.exit(1)
