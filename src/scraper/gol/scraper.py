import requests
import json
from datetime import datetime

def get_flight_list(date, airport):
    session = requests.Session()
    s = session.get('https://www.voegol.com.br/')

    url = "https://b2c-api.voegol.com.br/api/sabre-default/flights"

    querystring = {"context":"b2c","flow":"Issue"}

    payload = "{promocodebanner:false," \
              "destinationCountryToUSA:false," \
              "airSearch:{cabinClass:null," \
              "currency:null," \
              "pointOfSale:'BR'," \
              "awardBooking:false," \
              "searchType:'BRANDED'," \
              "promoCodes:[]," \
              "originalItineraryParts:[{from:{" \
              f"code:'{airport}'," \
              "useNearbyLocations:false}," \
              "to:{code:'IGU'," \
              "useNearbyLocations:false}," \
              "when:{" \
              f"date:'{date.isoformat()}'," \
              "selectedOfferRef:null," \
              "plusMinusDays:null}}]," \
              "itineraryParts:[{from:{" \
              f"code:'{airport}'," \
              "useNearbyLocations:false}," \
              "to:{code:'IGU'," \
              "useNearbyLocations:false}," \
              "when:{" \
              f"date:'{date.isoformat()}'," \
              "selectedOfferRef:null," \
              "plusMinusDays:null}}]," \
              "passengers:{ADT:1," \
              "CHD:0," \
              "INF:0}," \
              "trendIndicator:null," \
              "preferredOperatingCarrier:null}}," \
              "destinationCountry:'BR'}"
    headers = {
        "cookie": "visid_incap_2618276=n%2Bl3UUJLTkyntyqnYSq6KMDDvGIAAAAAQUIPAAAAAAC82GODHJj585ua8bCcnjet; nlbi_2618276=FuD8R6uTXgoMz46mjGAFLwAAAAAYyUu3Djv6zmJqbGJoE%2BZH; incap_ses_980_2618276=t6xLRN8%2B9DnUbV1q4aiZDU7o0mIAAAAAhpIXQB4U1C3Gaxmb6SX2SA%3D%3D; visid_incap_2631856=WK6kW%2FmMTGizw61yp%2F6MM3Lp0mIAAAAAQUIPAAAAAABFZxINOVzaj0m%2FQP6fToj3; incap_ses_788_2631856=lAX5YMJH2ni7vkPcc4rvCnLp0mIAAAAAi9HZf4d%2BGV19B1pLW98%2BWA%3D%3D",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:102.0) Gecko/20100101 Firefox/102.0",
        "Accept": "application/json",
        "Accept-Language": "pt-BR,pt;q=0.8,en-US;q=0.5,en;q=0.3",
        "Accept-Encoding": "gzip, deflate, br",
        "Content-Type": "application/json",
        "Referer": "https://b2c.voegol.com.br/",
        "x-sabre-cookie-encoded": "H4sIAAAAAAAEA+2WSW+bQBzFvwrytcHMDLstDsCAjY038JqqioCMbYxZzBKDq3z3OqmqRs2hraKoqtoRh4ELv3nv/57m4+fWkDStTsslJa2naRSS1k1r6R0rcv2orlzV1uY9RQxmrCmGD2s5JQaOWQGKgmcPzREU9VksOWS6wKFUR8xiaabRnL/km97J9JP1zJMb1cMIOIOtFcmHAq71yV6tG+bY5/vJ3LQ2Pcd7SHIdjkpe3dYP9kkeHPYRso2L7zqzIuibzXnXuOtL79YGlcpbulh+wMtmv2BOxYdI21msOTudSDaSN0C3z+4hN+6HkdKljDoLc1IorlfeUIilBtWRQgAhCgodTu5AgeqN5l1q6pV7hWk93vySFvrEcf8FPbqU68XEDUuijNOE/Jo8yqWOK3Oj1hOcbcUTYbXzejlILo0wz46Hs7bnL3vN4Zy1E7M9e6YPY/1sPKgHaFlb9cA0mrc8pbE4vj3gFSKjTepkfoblgNsx9e1lyuzhqFnFYysK7YMrR9zC2UgVQoER+Qz3LoY/2/0Xneo3bRu4hutak7GFFQ0LBtaxJhkmL0pQ1mVeNwRDwEAzIeJBlxp5Na3uiHLdfovWfF/dUADSAy+hoSwCCoDO9YHgZbRcd4UABMyVjQRVTrpUvyyzSXJs3pP2a6zf/M+VPdUnk6FlKGFGQ0BDxNIST0vtqqDPpChp1A7SOKtK0g6TkuSJd4RvluoPU4sIvPD4uT6hQF/rk/5an9Lr+nwzMda/j6LEIR+xIKAFHt3TnL/d0r7IEhoGEpKBDADLvdD4+v59IF/Dih3A/dD1r2F/Vm9/lu7K+ztd/D/UP7Pzf6hf5+Q9Qh0mgZfdFaS4g5wo3yGWE4EgKAk3mvrbqbNKIlzu8rnIej1TvRQgttSnpQF9XizKAV7ie0u0U27Sr8uzcr3SZc93tS6F09gLE6Wd5el9u/D8nDy1cOvx0xfAXLEU0QoAAA==",
        "x-jsessionid": "BD6EDCDB8EF57819C95CE6E6D0BF1250",
        "Origin": "https://b2c.voegol.com.br",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-site",
        "Authorization": "Bearer eyJhbGciOiJSUzI1NiIsImtpZCI6IjkyM0NFMDYyQkI0M0QzRTNFNEEzQUM2MkFENTMwNUMzRDEyNEM3MzIiLCJ4NXQiOiJranpnWXJ0RDAtUGtvNnhpclZNRnc5RWt4ekkiLCJ0eXAiOiJKV1QifQ.eyJkY3QiOiJWREZTVEVGUlNXeDZMemRMVEM5QlVHdFhVRE5HVlVkdlMycGpOVFJ1UVdKRFV6UkhSRGxZVUVsQ2VWZEVkR3AxVTBKQmNqRm5Na0oxY3pWUmN6RnNTMjh6WlZWRVJISXdRVUZFVVhwbGJIQXJiakJ0VGxwRmJuVkVUVFJpTDNVelZtSk9OMWRwZDJ0Rk0yMVRaRmN4UkRaeFpFVmtlbU0xVHpsa05HUjBUVmQxV1RScmJqVTNiR0V4ZVhWRFEweFVkbFZLYVVrMmVWazRNM0UxVERSWFdrdEthR05JZG1GU1YzSkJhbkJ6U1VkMldXUktUMU5PU0dOUlpucDNjMnRCYkRoRlJ5czFlbmhDUzNkNE1FSTBOMmQ2Ym1GeVdtVlJNbkpIY0ZGTk9IQTVNWGRPYVhVMmFGZDFibk13WlhnM05VNVlhMnRKWVRReFdFbFVlRFJ5YkRoc2NtVm1ORkpDWWs5WlEwWXpPRk5pVm10RVFqQmlXbVpLVDFacVZuZDVTMWxNYW14RVFXSTBhRGgxTlN0bFZWVkNUVTFZUVZObGMxTmlORWRZYUhOb2F6ZDFha2htUjI1NldUTlJZMnA2VG1SVVMzcE5NamwwVTNZd2RtbzVaa1ZSS2lvPSIsIm5iZiI6MTY1NzU3MTA5MywiZXhwIjoxNjU4MDAzMDk0LCJpYXQiOjE2NTc1NzEwOTQsImlzcyI6Imh0dHBzOi8vYXV0aC1hcGkudm9lZ29sLmNsb3VkIiwiYXVkIjoiYjJjLnZvZWdvbC5jb20uYnIvUFJPRCJ9.gjxnXkqMkMW42DIel-STcVWjEEdcJWzkVRgAKpZGTXzW_ugQVKa7NZhEKwFIO_kKeNl_2w6h4VBEYI3jtNFii9TZ6YmmmWilFhgsHPiTPW9LKZISJYnir674BWTwbOXJ7X1wgpkIq1R4S9Uxp7RbT1Zr6WAzLakoYDG2aBVY2xzhzAiX_bojO1klU9QSsg6oWbjy-FDqqtjcBfy5R2cSTxFcJJuc-njPG_1JQGYIVg7GLuFt78pFOr-LiO08_DlHsWyphlZ4pk41R8DKSwNGzdJS9TQOV61KypVvDSp6IBfYFVZ6ZcYUm8xrakA4Z7t4mjj5kygcOKnp1I010WuioQ",
        "Connection": "keep-alive"
    }
    # response = session.request("POST", url, data=payload, headers=headers, params=querystring)
    response = session.post(url, data=payload, headers=headers, params=querystring)
    return json.loads(response.text)