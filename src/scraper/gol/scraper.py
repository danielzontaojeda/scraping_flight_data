import requests
import json
from datetime import datetime


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
        "Authorization": "Bearer eyJhbGciOiJSUzI1NiIsImtpZCI6IjkyM0NFMDYyQkI0M0QzRTNFNEEzQUM2MkFENTMwNUMzRDEyNEM3MzIiLCJ4NXQiOiJranpnWXJ0RDAtUGtvNnhpclZNRnc5RWt4ekkiLCJ0eXAiOiJKV1QifQ.eyJkY3QiOiJWREZTVEVGUlNqZHJMMFEwVFZadVJGRXpjSGh6ZDFGaVVHSlRVbTUyWVhoTFZFUkRhekkxYUVOQ1UzVkpMekZZZG1oQkwyOTJSMFp2UVdaT05HTTNSRFZUWlVRNFZrbHhRVUZFVVZoVlIwbHVhMHhRYTNsTFFVZEJNVmRNYkZGbU1VRmhhbk5aYlUwNFN6UTBhR3RrZUVkek9Xc3JNbG8xYVVodmFWVm5lVU5RY1ZCSFpVUXdNVEIwVlhVd1pFUnVOMEp2ZEc1YU1EaDVaV3hPYUdac1VsQnJUM1JEV214RFkyNTVMell6WkdkNGRqTkxhMVpwTmtjMU4wRkhPVVZxTjFsc1ZVSXhOa2ROTm14bGRFRnpiMk0zTDI5Ull6Vm5aekJNZWtsQk5HMUtOR3hZT0ZsclZ6bEVWMWQwYkUwNGFrVk1SVWhwUXpablR6RXdNSGN6TmpoUlkzQXdZalV2YjNwbWVGVnNlRXR4UTBKdkwzTnFLMDU1VDNKQ09YWmhSVkowVlZWUGFETlNRWEJoUjJod05GcFdVV0ZUYm1RM1VIcE5WelJvUkZOaWJuTk9PV1IxVFZGaVVsUTRWaloxV0VOdGJFTTNkRXhOU3paUlZVZGtaVTVSS2lvPSIsIm5iZiI6MTY1Nzk5NDAxMiwiZXhwIjoxNjU4NDI2MDEzLCJpYXQiOjE2NTc5OTQwMTMsImlzcyI6Imh0dHBzOi8vYXV0aC1hcGkudm9lZ29sLmNsb3VkIiwiYXVkIjoiYjJjLnZvZWdvbC5jb20uYnIvUFJPRCJ9.R4TaAMcysBJEdctYO70_WdPpEHdeHorEf3Ezly7doao0Z9zeJvBpxAe3m2TMkOWlntDm2HgTpxZtbKW4yIG2yJxr4xey1aNAb6mHmv72UKmqmDpOcxaY5G23S95-sbXa12LFt_WDhTnZVFfdRWgHYa0F_n8-W_uTFpjIzCqCib_Q5YFxQztopg3dDoiq9CThVBfvhYy7ezowajXtSyNvC0NBfL0nHHa7reqQQrk99z3YddqvzY2tgrU7AgcMTnMaUxdQg6P1eXeE86I_zDO7doFXisYGFNqLoiyY4tQcJGtU4ieuH_FReet6cloQ9p_SVrJfQShrP8Lavc2IcNwquQ",
    }

    response = requests.request(
        "POST", url, data=payload, headers=headers, params=querystring
    )

    return json.loads(response.text)
