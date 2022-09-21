import requests
from config import AIRPORT_ORIGIN
from retry import retry
from scraping_flight_data.src.util import util_get_logger

LOGGER = util_get_logger.get_logger(__name__)


@retry(delay=10, logger=LOGGER)
def get_flight_list(date, airport: str, token) -> dict:
    url = "https://b2c-api.voegol.com.br/api/sabre-default/flights"

    querystring = {"context": "b2c", "flow": "Issue"}

    payload = (
        "{promocodebanner:false,destinationCountryToUSA:false,airSearch:{cabinClass:null,currency:null,pointOfSale:'BR',awardBooking:false,searchType:'BRANDED',promoCodes:[],originalItineraryParts:[{from:{code:'"
        + airport
        + "',useNearbyLocations:false},to:{code:'"
        + AIRPORT_ORIGIN
        + "',useNearbyLocations:false},when:{date:'"
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
        "Authorization": f"Bearer {token}",
    }

    response = requests.request(
        "POST", url, data=payload, headers=headers, params=querystring
    )
    return response.json()
