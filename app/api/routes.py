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
	    "X-RapidAPI-Key": "07c65bd2ddmsh378abedbb7aca68p159664jsn95efed7aa6dc",
	    "X-RapidAPI-Host": "tripadvisor16.p.rapidapi.com"
    }
    response = requests.get(url, headers=headers, params=querystring)
    locationId = response.json()['data'][0]['locationId']

    url2 = "https://tripadvisor16.p.rapidapi.com/api/v1/hotels/searchHotels"

    checkin = request.json.get('checkin')
    checkout = request.json.get('checkout')
    querystring2 = {"geoId":locationId,"checkIn":"2023-05-01","checkOut":"2023-05-02","currencyCode":"USD"}

    headers2 = {
	    "content-type": "application/octet-stream",
	    "X-RapidAPI-Key": "07c65bd2ddmsh378abedbb7aca68p159664jsn95efed7aa6dc",
	    "X-RapidAPI-Host": "tripadvisor16.p.rapidapi.com"
    }

    response2 = requests.get(url2, headers=headers2, params=querystring2)
    
    return locationId
@api.route('/api/restaurants')
def restaurants():
    url = "https://tripadvisor16.p.rapidapi.com/api/v1/restaurant/searchRestaurants"

    querystring = {"locationId":"187497"}

    headers = {
	    "content-type": "application/octet-stream",
	    "X-RapidAPI-Key": "07c65bd2ddmsh378abedbb7aca68p159664jsn95efed7aa6dc",
	    "X-RapidAPI-Host": "tripadvisor16.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers, params=querystring)

    print(response.json())
    return response.json()

@api.route('/api/hotels')
def hotels():
    url = "https://tripadvisor16.p.rapidapi.com/api/v1/hotels/searchHotels"

    querystring = {"geoId":"187497","checkIn":"2023-05-01","checkOut":"2023-05-02","pageNumber":"1","currencyCode":"USD"}

    headers = {
	    "content-type": "application/octet-stream",
	    "X-RapidAPI-Key": "07c65bd2ddmsh378abedbb7aca68p159664jsn95efed7aa6dc",
	    "X-RapidAPI-Host": "tripadvisor16.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers, params=querystring)
    return response.json()