from flask import Blueprint, request
import requests

api = Blueprint('api', __name__)

@api.post('/api/location')
def location():
    location= request.json.get('location')
    url = "https://tripadvisor16.p.rapidapi.com/api/v1/restaurant/searchLocation"
    querystring = {
        "query":location
    }
    headers = {
	    "content-type": "application/octet-stream",
	    "X-RapidAPI-Key": "07c65bd2ddmsh378abedbb7aca68p159664jsn95******",
	    "X-RapidAPI-Host": "tripadvisor16.p.rapidapi.com"
    }
    response = requests.get(url, headers=headers, params=querystring)
    locationId = response.json()['data'][0]['locationId']

    url2 = "https://tripadvisor16.p.rapidapi.com/api/v1/hotels/searchHotels"

    checkin = request.json.get('checkin')
    checkout = request.json.get('checkout')
    querystring2 = {"geoId":locationId,"checkIn": checkin,"checkOut":checkout,"currencyCode":"USD"}

    headers2 = {
	    "content-type": "application/octet-stream",
	    "X-RapidAPI-Key": "07c65bd2ddmsh378abedbb7aca68p159664jsn95******",
	    "X-RapidAPI-Host": "tripadvisor16.p.rapidapi.com"
    }

    response2 = requests.get(url2, headers=headers2, params=querystring2)
    print(response2.json())
    return response2.json()
@api.route('/api/restaurants')
def restaurants():
    url = "https://tripadvisor16.p.rapidapi.com/api/v1/restaurant/searchRestaurants"

    querystring = {"locationId":"187497"}

    headers = {
	    "content-type": "application/octet-stream",
	    "X-RapidAPI-Key": "07c65bd2ddmsh378abedbb7aca68p159664jsn9****",
	    "X-RapidAPI-Host": "tripadvisor16.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers, params=querystring)

    print(response.json())
    return response.json()

