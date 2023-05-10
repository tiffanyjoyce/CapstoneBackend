from flask import Blueprint, request
import requests
from ..models import Locations

api = Blueprint('api', __name__)

@api.post('/api/location')
def location():
    location= request.json.get('location')
    name=Locations.query.filter_by(city=location.upper()).first()
    if name:
        locationId = name.lid
        url2 = "https://tripadvisor16.p.rapidapi.com/api/v1/hotels/searchHotels"

        checkin = request.json.get('checkin')
        checkout = request.json.get('checkout')
        querystring2 = {"geoId":locationId,"checkIn": checkin,"checkOut":checkout,"currencyCode":"USD"}

        headers2 = {
	        "content-type": "application/octet-stream",
	        "X-RapidAPI-Key": "07c65bd2ddmsh378abedbb7aca68p159664jsn95efed7aa6dc",
	        "X-RapidAPI-Host": "tripadvisor16.p.rapidapi.com"
        }

        response2 = requests.get(url2, headers=headers2, params=querystring2)
        print(response2.json())
        return response2.json()
    else: 
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
        print(response.json())
        l = Locations(lid=locationId, city = location.upper())
        l.saveLocation()

        url2 = "https://tripadvisor16.p.rapidapi.com/api/v1/hotels/searchHotels"

        checkin = request.json.get('checkin')
        checkout = request.json.get('checkout')
        querystring2 = {"geoId":locationId,"checkIn": checkin,"checkOut":checkout,"currencyCode":"USD"}

        headers2 = {
	        "content-type": "application/octet-stream",
	        "X-RapidAPI-Key": "07c65bd2ddmsh378abedbb7aca68p159664jsn95efed7aa6dc",
	        "X-RapidAPI-Host": "tripadvisor16.p.rapidapi.com"
        }

        response2 = requests.get(url2, headers=headers2, params=querystring2)
        print(response2.json())
        return response2.json()
@api.post('/api/restaurants')
def restaurants():
    location= request.json.get('location')
    name=Locations.query.filter_by(city=location.upper()).first()
    if name:
        locationId = name.lid
        url = "https://tripadvisor16.p.rapidapi.com/api/v1/restaurant/searchRestaurants"

        querystring = {"locationId":locationId}

        headers = {
	        "content-type": "application/octet-stream",
	        "X-RapidAPI-Key": "07c65bd2ddmsh378abedbb7aca68p159664jsn95efed7aa6dc",
	        "X-RapidAPI-Host": "tripadvisor16.p.rapidapi.com"
            }

        response = requests.get(url, headers=headers, params=querystring)

        print(response.json())
        return response.json()
    else:
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
        print(response.json())
        l = Locations(lid=locationId, city = location.upper())
        l.saveLocation()
        url2 = "https://tripadvisor16.p.rapidapi.com/api/v1/restaurant/searchRestaurants"

        querystring2 = {"locationId":locationId}

        headers2 = {
	        "content-type": "application/octet-stream",
	        "X-RapidAPI-Key": "07c65bd2ddmsh378abedbb7aca68p159664jsn95efed7aa6dc",
	        "X-RapidAPI-Host": "tripadvisor16.p.rapidapi.com"
            }

        response2 = requests.get(url2, headers=headers2, params=querystring2)

        print(response2.json())
        return response2.json()
    
@api.post("/api/rentals")
def rentals():
    location = request.json.get('location')
    name = Locations.query.filter_by(city=location.upper()).first()
    checkin = request.json.get('checkin')
    checkout = request.json.get('checkout')

    if name:
        locationId = name.lid

        url = "https://tripadvisor16.p.rapidapi.com/api/v1/rentals/rentalSearch"

        querystring = {"geoId":locationId,"arrival":checkin,"departure":checkout,"sortOrder":"POPULARITY","currencyCode":"USD"}

        headers = {
	        "X-RapidAPI-Key": "07c65bd2ddmsh378abedbb7aca68p159664jsn95efed7aa6dc",
	        "X-RapidAPI-Host": "tripadvisor16.p.rapidapi.com"
        }

        response = requests.get(url, headers=headers, params=querystring)

        print(response.json())  
        return response.json()
    else:
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
        print(response.json())
        l = Locations(lid=locationId, city = location.upper())
        l.saveLocation()

        url2 = "https://tripadvisor16.p.rapidapi.com/api/v1/rentals/rentalSearch"

        querystring2 = {"geoId":locationId,"arrival":checkin,"departure":checkout,"sortOrder":"POPULARITY","currencyCode":"USD"}

        headers2 = {
	        "X-RapidAPI-Key": "07c65bd2ddmsh378abedbb7aca68p159664jsn95efed7aa6dc",
	        "X-RapidAPI-Host": "tripadvisor16.p.rapidapi.com"
        }

        response2 = requests.get(url2, headers=headers2, params=querystring2)

        print(response2.json())  
        return response2.json()


