import requests

def get_token():
    url = "https://gol-auth-api.voegol.com.br/api/authentication/create-token"

    payload = ""
    headers = {
        "cookie": "visid_incap_2618276=3Mwzgl64RBeKClLxTnC2%2FssP%2FmIAAAAAQUIPAAAAAADiWEN%2Bt3%2FKPSCvrLfHtM8R; nlbi_2618276=CMRyKrBObi%2F29iKjjGAFLwAAAACmB153q8AaHz8yfyiojXPU; incap_ses_143_2618276=G0gLJAwiAl1kG3RT1Qn8AR0Q%2FmIAAAAAjnr297FACk7%2Fi7GWKsPP3Q%3D%3D; incap_ses_1477_2618276=qbrhXccDriDN9Ezi%2B1t%2FFDiaA2MAAAAAa0vhefadGStVZDasteB97w%3D%3D",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:103.0) Gecko/20100101 Firefox/103.0",
        "Accept": "text/plain",
        "Accept-Language": "pt-BR,pt;q=0.8,en-US;q=0.5,en;q=0.3",
        "Accept-Encoding": "gzip, deflate, br",
        "Referer": "https://b2c.voegol.com.br/",
        "X-AAT": "NEUgdaCsLXoDdbB0/Jfb+d6O72lprMfUJxaW/eTW7ncXFZgMqTtFpi5mQdzidn0c0EnON6hHWtrBAshheNOhtQ==",
        "Origin": "https://b2c.voegol.com.br",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-site",
        "Connection": "keep-alive"
    }

    response = requests.request("GET", url, data=payload, headers=headers)
    response = response.json()
    return response['response']['token']


if __name__ == '__main__':
    print(get_token())

