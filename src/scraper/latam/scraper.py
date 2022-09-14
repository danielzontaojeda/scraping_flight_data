from datetime import date

import requests
from scraping_flight_data.config import AIRPORT_ORIGIN
from scraping_flight_data.src.util import util_get_logger

LOGGER = util_get_logger.get_logger(__name__)


def get_flight_list(lookup_date: date, airport: str) -> dict:
    url = "https://www.latamairlines.com/bff/air-offers/offers/search"
    date_str = lookup_date.strftime("%Y-%m-%d")

    querystring = {f"sort": "RECOMMENDED", "cabinType": "Economy", "origin": {airport}, "destination": {AIRPORT_ORIGIN},
                   "inFlightDate": "null", "inFrom": "null", "inOfferId": "null", "outFlightDate": "null",
                   "outFrom": {date_str}, "outOfferId": "null", "adult": "1", "child": "0", "infant": "0",
                   "redemption": "false"}

    headers = {
        "cookie": "_abck=559073DD0832BEDBC78DE03990908B57~-1~YAAQFTMcuHgsVPOCAQAAgXAGPQjfM4fBg4SwP90ExcBT8GLWG3PMFuLVTZhgbFwThzig7wnUADpDgB5%2BAMgEcOd35UDCr%2B2GTqwuNao8Q40PZ2TlT5UUena2HQ%2FGFlZlo4rfLyFv8g9DdXjdeLn%2BmZTQoyhawF68rTDAoncJZCpiiwfZbB4u5Kt38sOh5UDEhh3dmiSWhiCB9mE3wkEB2MXem7GZZc%2Fq6%2FXiZ5cKCgust1YVpWYoyRckwPl5D1rc3eARk7IdlXA9yVPpTQl%2Bl8gjWg7YWvrL8CeuAj0HjNkZU%2FSNtBQbbu5b1P25u2ep3i0XSTEz6%2FqIlgllm24xmyUXMYiq6K8qppiMv9jySI3%2Fwj4qZnSaY6m50aJNC4EZvHTOYpuy7CR%2Fu2UA8h0cxXwUyq1APpVQVyPscGE%2BCRo6~-1~-1~-1; bm_sv=96F5868B06FBAC866B8F6296F37A5B5E~YAAQFTMcuHosVPOCAQAAgXAGPRF8ny%2FVokGiau4%2BiSi4GI7RF02jZOSCp2djuA1UbrtxXFSPuINZSTskDuxcmChC29sxBVfSP9K37ia66%2BGYzeLFJiHnNx6N8li3YbvRzssDw7kANcEZlI%2BFjkpMruCNSDRt3%2Fcb1IwEjJveM2GRIv2nJVhaQWjntYAd6qSgz3mZKzaN0yimXMwJr9uSZSJQscKVDYNd%2FGATKZSBrqGj4W6BjyGu6D5%2BZ%2FjAKPSFqpqPRhwVkSk%3D~1; ak_bmsc=06C4DCA7C24AEDC6BD1EBFBAD6C8928D~000000000000000000000000000000~YAAQFTMcuHksVPOCAQAAgXAGPREZPEgaSVnTjZkz%2BJn3IgkPIVtLXrwJRY97jJ2HKsH2m6DJWGSr5lMD9waun%2Bn20%2FF32EBoEDPnGjMmiGRNTgvaxFNxWw87%2FG6bY2sydIaxbdfT9JfOd%2FF6JvqcMoxpqr0BSS4jqtyQX4CXPc3%2BwjntbUOZB6DGrjXgEkUJWSFABRtQRYIKCNtJChUkiuBz8HiXvS78ixbzxkyCJ%2BAVu%2BVaYRbqWJJiGDjCajCo0UEcfAlBnXIjKsUq1V4OrjmD5hd4Hd47nauiB8%2F7EXx3w0OhAiWevDmbiW3guAcS4nW%2Bvwo088l2QvWE4zTiBrrOuBPwx%2BjSOdWXPg04GVdck2zRhEAicHnP2fLup9jb1Yta6EzgiOaCd95GfGwo4DlXrNdayC7s0pHqVbcGB%2B%2Bvmi8IOopHuHTqCRYEkMHn50GaUvZ75p0XfOhC7p%2BS05AcXkcOJ24M; bm_sz=E1A0DDB11DEB234F275C14B5FBCFB44B~YAAQLDMcuEsYIgCDAQAARUfmPBGJqFDLMJ%2F%2Bv0yyNcyWTqkcdhpWeGCWSlgh68QfTiTQCCaOXdb4TcikHZa%2F6P6Rf%2FN1JliIMhsgPy%2Bj5YkVGNJRugniF87EV%2F%2Bqf55FRGSm4c%2FJdHXBLzW2HMJY3Yr7KYSMp3DreuSgWT6%2BBNRi7DGce3bOxiqg52tRm%2FNHA3JZeE%2BFi9kGvQFdOfWK7yJOMjg621%2Bgbm7Ig12Fm9t9bngfd%2BfgrPucG1Mr5G2WHTTlNFpBswx9Rj1aTa4Jxmt6ernlk9Db36v%2FK8ckdDgjCYckLzV2vXd5~3420468~4601138; _xp_session=s%253AvKciXUd4dRqWpVMzZuQqaAo6PkEvYZhY.07cAP5TmFU8wolZbq%252BzZPQ8%252FCE%252Fwxi%252FYa7l%252BzKi9XnQ",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:104.0) Gecko/20100101 Firefox/104.0",
        "Accept": "*/*",
        "Accept-Language": "pt-BR,pt;q=0.8,en-US;q=0.5,en;q=0.3",
        "Accept-Encoding": "gzip, deflate, br",
        "Referer": "https://www.latamairlines.com/br/pt/oferta-voos?origin=GRU&inbound=null&outbound=2022-09-30T15%3A00%3A00.000Z&destination=IGU&adt=1&chd=0&inf=0&trip=OW&cabin=Economy&redemption=false&sort=RECOMMENDED",
        "X-latam-App-Session-Id": "84196897-1687-4d8c-8e63-083091ac204f",
        "Content-Type": "application/json",
        "X-latam-Action-Name": "search-result.flightselection.offers-search",
        "X-latam-Application-Name": "web-air-offers",
        "X-latam-Client-Name": "web-air-offers",
        "X-latam-Track-Id": "3a4ae189-e218-4606-bd9e-8b17efc93463",
        "X-latam-Request-Id": "ff44ef24-e6d0-4cb0-984c-df1db18cee19",
        "X-latam-Application-Country": "BR",
        "X-latam-Application-Oc": "br",
        "X-latam-Application-Lang": "pt",
        "Connection": "keep-alive",
        "Cookie": "_abck=559073DD0832BEDBC78DE03990908B57~-1~YAAQLDMcuL4XIgCDAQAAuUXlPAig8mbOzGGPkE9oJGfBPUQAQGNh2emJzNYRI8YWihakg8iWKFnitaNA5FAIdx8XKr5/BkPL98R/pDG8PgRSIty1l9CJXeb3OgH28GjO6p0HJD9vUF5WBYrDarHzjzFK7SPEiJuctJvTxu+risqXdluatrBn0wcVtcf3jtNnQOncgK5qgiOZhRqZSoIqU1yiJ/wrR7xsX+CpRpBA5ErU2A9l15mrSIbYWLQRG0eKAl0xf7f27+OxXQb309Baw1JuLgxcb5UZbuhQmNaad9L5Lg90LsVkJdSM8+/a0adUTlNYKoe4jLznWLNLpAbe9J7YVgxJLuzEUQIE6Cd/eacrK5GWYYvxb3Zm5s0o7C8ql37YsPW3s+ATX2zx9xPygFhpCFlVGaVdW4vyqGACHMs=~0~-1~-1; mdLogger=false; kampyle_userid=5590-4672-ecee-a6b5-f838-328f-83fb-eb4d; kampyleUserSession=1663173973711; kampyleSessionPageCounter=1; kampyleUserSessionsCount=38; _xp_session=s%3AeOa3GlOPlV9njy53fzGymbTXyfJrNWwe.Tt58Sn4NG2pUNQK06xe8amYX%2BBMvUwhjYKHPNZaYLk4; bm_sz=8BECE9DE91EC8125D621CCFDD2800251~YAAQLDMcuLAWIgCDAQAAQ1rjPBH6ypnmgt9jz8QQ+6CFlk6Bp8cfKskCsBYhc31H3BXVUiNdBf7IyCvCPKzrsIEdz9HHGShA4jpt/mGnee9oiw4MrGtNIWar70uGug2prNzl8yKvKxlT0A0lqVIVwTHWCeRubM2ErLX7PG0TQ4mfemjkinYWbqpQlJ7sXu0A3+xk22FrWm4MhEFSgieQab9EJZwv664OBGcIsTfK2/BqRsIL3QOD/FHv429VdpS8Ll+Z0yRQvYCk6U+oOvJAj5P2Fj5ghJF1lwWlUNoM7t9B8/8FSwambr6F~4536386~3289153; ak_bmsc=DA53DCE4FD3B22A36192590DD7C2AAC8~000000000000000000000000000000~YAAQLDMcuJYXIgCDAQAAQB/lPBGwnUOrVBPJNgejprTte78e1wPYyxLK487E61O9qnpbPGRIqLYai5W2r9/p3CaBdeuNrwQQQj+QlGmhdslJt0VAMNrWx+/jioIUD5RjNE/QqwZaopJiGCXhDlNwIxcOcCGAinMf31qzKNeCU+VoXyrYtgB8BRYhSosbnk6bARaQLXMCiT3sKHu8lsYfx1rgTMnhg11D4C5Zka/DW0W1xaedoI8AfqJUL/hAXGZLj04oZ3vc81Yn4ezm2dnjLkZfL3j8XLroADSOnuxvPiwLCPv4YK+fYXu9q8VP8zdDD8MMUKiyiSkAPSTNr/D9fGKQ3hwEgX+kMuX7D7Kvy2M3VMzGa+S+7ZIdbLB9Nt9A8xe3fDv3q1pOOq67tt4zgSWY4XTcecRdn8t/YiIIHma7aeikzjnIhL1vzK1pgAgKoFmwh0ZpgUF2YSLqJN5K12J1sYOLHDYB; bm_sv=96F5868B06FBAC866B8F6296F37A5B5E~YAAQLDMcuL8XIgCDAQAAuUXlPBEiJYC8T6FbBhRN71xXPd9S11fTpD/Ij9sEiS5sQ9EUUxH0ev6or16dw1vbJvHJnsw4cNmNakfIgW2I+QzIiPKYh2zYAZlGAkFre3M+5XzOmbhloRJ25Mw8cA7Q6+dXMWUayO5FYw58ryQeTqgvgnf00gB6KK5w1V2SrJnTLPFn+nY9ylh9JmKmbCZ49TBVTzdqxMsKdY1hDxj74gNffQ9qu2n1Abpam/c5F0ZAFAGGxrpC5SE=~1; bm_mi=2675F36B6B405D222B7A6A62A479967A~YAAQLDMcuGMXIgCDAQAAeNDkPBGl0l3ds6BDDiO0dYwyJmkk6VkUo044dOt9R14XG/oIdSOTPkNjNXIfrOeYBLtreo0/hdDJmGXYWS6ZevkkS3HKVf05uyV2hteSdLPGMe4CfAKUyG+AMb4uNz+b84wo49rw3s7iGQbGt7bGOFJin5pAMhcbehFQb+FTG+8l8SF2jwTQjrmpyS5P885K3mtRX/5Vvg+YJDqXotgufH/1DfmQG1KIOWVZlVMjELDNaloRIpqI/bpijMSnT73LB4fqaKkhQtvvs4j1otRifS9aM0XqKniL9GFcq36Zn2zN9yX6rqjr/PNR5g==~1; _xp_application_lang=pt; _xp_application_country=br",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-origin",
        "TE": "trailers"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)

    return response.json()["content"]