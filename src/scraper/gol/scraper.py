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
        "Authorization": "Bearer eyJhbGciOiJSUzI1NiIsImtpZCI6IjkyM0NFMDYyQkI0M0QzRTNFNEEzQUM2MkFENTMwNUMzRDEyNEM3MzIiLCJ4NXQiOiJranpnWXJ0RDAtUGtvNnhpclZNRnc5RWt4ekkiLCJ0eXAiOiJKV1QifQ.eyJkY3QiOiJWREZTVEVGUlNXNVVWRU5qU210RmJXeFpOMjA0YlZaUFZVTndUVWMwZWtsNFVESXJjM2RNVWtONlV6VkVRbUp3WjNoQlRTOW1ObkJtYVhneFMyOVFOa2haZWsxMmMxUTNRVUZFVVhVMVVrbEhaVVU1WTBoNVIyaGhZa3hrUkd0T09YRk1ZblExVm01SFVVRmxaV3c1VG5OSGVVZHlhV0o2U1VkblpHeFFZbHBvVm0xeFpsRlhSWEZCYmpSTVlrMXlhVEpLYTI5eFJrWTViME5VUVhOME1IZDRhRkZLWTJWalExRmFPR1p4ZW1sd05WZHVXVkZ1YVhvdlEzaHdhbmhhVUUxRVoxUm1lRUV4VkdWNVMyRkpjVEJuUjFWQmVVODFSbEJTVDJ4SmJtTnVUa1o2ZGtWM04ySk9Rak5FVXpKWVJGUlNTVkJQUjBsNVoyRkJjV0U0YzJ4Rk1XVlpWMnBKV1hoNkwwZDNUbkZQU214YVdVbHlZVmxFWXl0TFNXUlFSMDlGVTJRNFNUbGxhbXBZY2xjNE1WWXhTSGg0ZVRObGFUVlRkMmRQVjFKR05XbzBaMDlKYVZVeFpHUlFZMWhFYW01aGRFUTFaVGgwWnl0TVlrNU9lSHBuS2lvPSIsIm5iZiI6MTY2MDY4Mzg1MSwiZXhwIjoxNjYxMTE1ODUyLCJpYXQiOjE2NjA2ODM4NTIsImlzcyI6Imh0dHBzOi8vYXV0aC1hcGkudm9lZ29sLmNsb3VkIiwiYXVkIjoiYjJjLnZvZWdvbC5jb20uYnIvUFJPRCJ9.fYZsKnyyEo00Qi0BDnG0VUklvpmF52ad88UvhZiyPl66Al417_Zc3bsWay9HIedRWqqXzgKOyHx5nLbZwcSvbV7TpEjGSYJQIAI8PtYt1lPHKFjuyR_SU1KASIFM1Ml8Lt44bneGWGgaPBw7nfWjdzPCCAtLHR9eXiAed4RP8W7dV1brqFDigB1lZxvfN5aCU7W_-wUoONXAh9Ssi26pE32GSaZyyG2qqCykq081W2wP73G8ubW1gHDzzYgTopQhzjJ88H6Mwc6CgaBRDUkXvYVyu7DrSzTbu8MPkREYvYkoadMhBoSKl5D7oAtX9ZiiUEFdXJCBCkOOF8zYsLKFxg",
    }

    response = requests.request(
        "POST", url, data=payload, headers=headers, params=querystring
    )
    # print(type(response.json()))
    # return json.loads(response.text)
    return response.json()
