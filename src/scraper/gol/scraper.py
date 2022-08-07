import json

import requests


def get_flight_list(date, airport):
    url = "https://b2c-api.voegol.com.br/api/sabre-default/flights"

    querystring = {"context": "b2c", "flow": "Issue"}

    payload = (
        "{promocodebanner:false,destinationCountryToUSA:false,airSearch:{cabinClass:null,currency:null,pointOfSale:'BR',awardBooking:false,searchType:'BRANDED',promoCodes:[],originalItineraryParts:[{from:{code:'"
        + airport
        + "',useNearbyLocations:false},to:{code:'IGU',useNearbyLocations:false},when:{date:'"
        + date.isoformat()
        + ":00:00'},selectedOfferRef:null,plusMinusDays:null}],itineraryParts:[{from:{code:'"
        + airport
        + "',useNearbyLocations:false},to:{code:'IGU',useNearbyLocations:false},when:{date:'"
        + date.isoformat()
        + "T00:00:00'},selectedOfferRef:null,plusMinusDays:null}],passengers:{ADT:1,CHD:0,INF:0},trendIndicator:null,preferredOperatingCarrier:null}}"
    )
    headers = {
        "cookie": "visid_incap_2618276=n%2Bl3UUJLTkyntyqnYSq6KMDDvGIAAAAAQUIPAAAAAAC82GODHJj585ua8bCcnjet; nlbi_2618276=FuD8R6uTXgoMz46mjGAFLwAAAAAYyUu3Djv6zmJqbGJoE%2BZH; incap_ses_980_2618276=t6xLRN8%2B9DnUbV1q4aiZDU7o0mIAAAAAhpIXQB4U1C3Gaxmb6SX2SA%3D%3D; visid_incap_2631856=WK6kW%2FmMTGizw61yp%2F6MM3Lp0mIAAAAAQUIPAAAAAABFZxINOVzaj0m%2FQP6fToj3; incap_ses_788_2631856=lAX5YMJH2ni7vkPcc4rvCnLp0mIAAAAAi9HZf4d%2BGV19B1pLW98%2BWA%3D%3D; incap_ses_1471_2618276=fKi0eLp6bFYT5qhb%2BApqFMTk1mIAAAAAMmKKC5hlNHQlPeJy5c7rQA%3D%3D",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:102.0) Gecko/20100101 Firefox/102.0",
        "Content-Type": "application/json",
        "Authorization": "Bearer eyJhbGciOiJSUzI1NiIsImtpZCI6IjkyM0NFMDYyQkI0M0QzRTNFNEEzQUM2MkFENTMwNUMzRDEyNEM3MzIiLCJ4NXQiOiJranpnWXJ0RDAtUGtvNnhpclZNRnc5RWt4ekkiLCJ0eXAiOiJKV1QifQ.eyJkY3QiOiJWREZTVEVGUlNqTlBaWFZoVUVSdmJqVjFheTkwZW5SbGNsVTJjM0Z4V1haVWMzbHhLMWgwVlZsUFZuZDJWM1l5VjBKQll6SmxORnBYTUU1TmN6QnBabk5JT0ZOb2MwMTZRVUZFVVVWbU1EVk5LMmM1Um5WWk9FTTJRVloyYUVKbGJVbExUMFo2YlZaSFdVbFVhbU5OVVdGWVdsbERaM0JEUXpJemFIZEROV3BMTmxaRVdIQkROMEpMUlVoMVpHaFZNM1ZXZDBoT2NqSmpOMUpDWjJKa09GaFNiMGQ1YzIxaFRWUkhhSGxoWlZkaVkwSkxhbnA1V1VNM2VXZEVTMXB0UWs5c1ZFTklNM2RsZFZGTWFrNUZjMkZVVFdKU2QwOHlkVElyY2l0RFFVRmpZekpFY3l0dFJuaGlaVTloY2xaT05XSnlSakJRZUhJeFpuaEVNbVZxV25wRFdsaEpOVmx6U21oNGRTOW9hR0pZUkM4dlR6ZHdkMmRDTWxORVJubzRORXRWVVVjclNHTXlURFl3VkVZeVNIRlFOQ3RLWm5ob2NtRm1MM1pQVWswMmMxQTNOVVJoTkhKVVRrcE5kVkprV1Zab1NqTk5VR3RTVEU1SlQzUXlUa2xSS2lvPSIsIm5iZiI6MTY1OTU3MTczNSwiZXhwIjoxNjYwMDAzNzM2LCJpYXQiOjE2NTk1NzE3MzYsImlzcyI6Imh0dHBzOi8vYXV0aC1hcGkudm9lZ29sLmNsb3VkIiwiYXVkIjoiYjJjLnZvZWdvbC5jb20uYnIvUFJPRCJ9.bseBFfG1ERrs9KKOYVTfCgc5UBajeCtBV9OgsBwJejeJrSVsfb_0QJTp2tjqzlWfMwsXbuaYQvCbo9k9m1CrTm9Ul7dlGI5Uam93P4AZbN4SI3ySHyNi95joFjXAu51byM8UTsJ3epiDjRoRa7e01lGJDo5FznEcgoWWd1bhXY0ZB1Xkw7UymZWVtCc6HDMVzrf_Y6D6RyyjSB0ywGHxXrJy2Ba_LyivDKoudbvwNbnjfMPz7AtibVXoolFGelG_9fO04Uu9YiRnWipcQNQB9P0ZEQJKjFXtco2gTrIqCTq38rkz5MToWXenodo5UPusDzkFXYlioLmfhCq9h1Hfbw",
    }

    response = requests.request(
        "POST", url, data=payload, headers=headers, params=querystring
    )
    # print(type(response.json()))
    # return json.loads(response.text)
    return response.json()
