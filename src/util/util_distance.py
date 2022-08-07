import requests


def get_distance(destination):
    url = (
        f"https://pt.distancia24.org/route.json?stops=Foz+do+Igua%C3%A7u|{destination}"
    )
    r = requests.get(url)

    data = r.json()
    return data["distances"][0]


if __name__ == "__main__":
    print(get_distance("Curitiba"))
    # print(get_distance("São Paulo"))
    # print(get_distance("Rio de Janeiro"))
    # print(get_distance("Porto Alegre"))
    # print(get_distance("Cuiaba"))
    # print(get_distance("Cuiabá"))
