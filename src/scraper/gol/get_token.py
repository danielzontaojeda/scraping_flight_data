import requests

def get_token():
    url = "https://gol-auth-api.voegol.com.br/api/authentication/create-token"

    payload = ""
    headers = {
        "X-AAT": "NEUgdaCsLXoDdbB0/Jfb+d6O72lprMfUJxaW/eTW7ncXFZgMqTtFpi5mQdzidn0c0EnON6hHWtrBAshheNOhtQ==",
    }

    response = requests.request("GET", url, data=payload, headers=headers)
    response = response.json()
    return response['response']['token']


if __name__ == '__main__':
    print(get_token())

