import gzip
import http.client
import json
from datetime import date
from gzip import BadGzipFile


def get_flight_list(lookup_date: date, airport: str) -> dict:
    conn = http.client.HTTPSConnection("www.latamairlines.com")

    date_str = lookup_date.strftime("%Y-%m-%d")

    payload = ""

    headers = {
        "cookie": "_abck=559073DD0832BEDBC78DE03990908B57~-1~YAAQXX%2FNFxQwo66BAQAAc1gP2gg57yGuvT8zzw5lWm9dN4FZjM4NLMWY2Wyjtm4qjhl%2Fy2tXD2%2FnVEdNHSNkHnPmLGfKp6cf6OgiOBEFm7ErpKkHrvu1khJzaHSuNsWhXVKJBEIEilqOspbgg8iZbIW%2BX0R%2Fk00XR20GCCmRYKC7dTVA9xqajFJL%2BLamv5hLwqR9ZLDwWiG763Ru8bvOKnP%2FNmz5kHEKMDhc%2FGW8EEq66XgwVt7ZZzhIRshnsGEhsVQABml5U%2BqPImwqdOXgvzx%2ByAGvBPC6Iu3jlWmwE%2FvgRTsXVmNjL3zqmhZ1pEWA78OVGF65qkkPZhOQs3hBbrA5pX%2B5pBkFfDLAPqCCnPdHvNC4SVD6xyb0z7RsABBg%2BlxpNhjaBGmEtWpG84WFUaRh~-1~-1~-1",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:102.0) Gecko/20100101 Firefox/102.0",
        "Accept": "*/*",
        "Accept-Language": "pt-BR,pt;q=0.8,en-US;q=0.5,en;q=0.3",
        "Accept-Encoding": "gzip, deflate, br",
        "Referer": "https://www.latamairlines.com/br/pt/oferta-voos?origin=GRU&inbound=null&outbound=2022-07-08T15%3A00%3A00.000Z&destination=IGU&adt=1&chd=0&inf=0&trip=OW&cabin=Economy&redemption=false&sort=RECOMMENDED",
        "X-latam-App-Session-Id": "688fb7eb-93a9-4eb3-ad0a-9e4121efca7e",
        "Content-Type": "application/json",
        "X-latam-Action-Name": "search-result.flightselection.offers-search",
        "X-latam-Application-Name": "web-air-offers",
        "X-latam-Client-Name": "web-air-offers",
        "X-latam-Track-Id": "7320001d-4349-46c2-9148-7aaa2719ea57",
        "X-latam-Request-Id": "ccacacb8-e1cd-4258-8edd-695163d76822",
        "X-latam-Application-Country": "BR",
        "X-latam-Application-Oc": "br",
        "X-latam-Application-Lang": "pt",
        "Connection": "keep-alive",
        "Cookie": "_abck=559073DD0832BEDBC78DE03990908B57~-1~YAAQXX/NF0woo66BAQAAxV8O2ghBGPX0o34uNqlfK+VpXUUpKWCg99q84ve6K01r0L9bPE2B/gK4RcRjEhIDjGEbzc4WZTj+XvzFSCZBArDzCDiXF366XY8kH7L9ZJPwd3eZKZX7agTCCetoQvJjo9SA0dQOoHsPpEVTA6h72o15lq4yOyT2Qp0QigqLk5xsvdRrjNyy0wxNmpU76zY4wklEru5KGBDb3PLiJQ0JPdCCroBL6JpYZUA5P5zVMrWP8LJiGBb6Yi1oADf5gnLo2EWTcB1NEe5e0ep0p4SfdJh1NfpPtbpPURQv0SCX2lNzfzoVW/v1cQ7v7lcRZXv4JXs1fK4NQ6Ers1/ApYoSuFPbxBzaE9ShBVoixtZ3ZGzuFpjKNOwD6txVkGyCKj5u7NUVKUxIW7ZyzOZUgaYkyYs=~0~-1~-1; mdLogger=false; kampyle_userid=5590-4672-ecee-a6b5-f838-328f-83fb-eb4d; kampyleUserSession=1657220754470; kampyleSessionPageCounter=1; kampyleUserSessionsCount=29; bm_sz=C57C5EE8857B6FF73E0A09555943EC6C~YAAQXX/NF/Yio66BAQAACd0N2hBi2V8v4CXGuGt7LRzmPNKVnw/aODOiVDf7hlP42ZzBH8JYLIUSMKAH8pFe5fTtlUffZ8EtdYhiz7Bkx4ZB5qZe6tDP4z6s85e4GPsq5cHg4DTkmidxABM87ZbA9/yOgz+idxbdonoFMOc2aP4MgStrJ9Yip1MZWgfODCXBjPkJZBbRebiCwRr+FRnihGd0VgIgt9kSSO60vuXggdTY3OfirdF1y1NanPiqjJ09qJLfyN1x4Hof55337CEnIidT7kk1fVde3MkxoGR4LG5c2qr5m3MaVARN~3294534~3618866; _xp_application_lang=pt; _xp_application_country=br; _xp_session=s%3ADoms1KEb8k7mN8sQhp3lIu6n0mc8Wb7f.VOdNAb2vet5f0BzsF0vGH89XGmR9TTxOzInKJj0sThI; ak_bmsc=48F9A0DC08CE31ED521B2287A3236491~000000000000000000000000000000~YAAQXX/NFw8jo66BAQAA4uAN2hB43xeNyELwC8xVNQNirxDzgVQ5ABvO/hRIpI+xMKer796IzwF6pcVSO2yo2OqwRr/ofjr/YU9N6BHM+fxEC8ABEd1wnpBBxWcqQ0BONTUR1oNiqzwVv7Z31YZuZwVetbGnHvKTq00IESY/08RLafS+XMKRJ+20tdFIjzSMz2pXsrOuWq92R/iOsSk8uK8Z8uQvAoNz0BWC8Kh5k2hChYkh820+uNANewuHX0qgPkMDXotisl7UXjN0e3oooGgfgTjuDRiGFF8KS0ad375sK3Rqdrj+q/b5NC1OpWK75cIw4q6SjoWynIV9Qsoost3R2GJkIoQgUJPJMxWjv9A3Ti9oBAZXso0rGAz89gMTqMYr/SB0Jvsj7HslVF8I25qO; bm_sv=1A359E058C64435610CAACCE67B8B39A~YAAQXX/NF04oo66BAQAAxV8O2hARcA4EekLC0eRBdUKuZvSkjXtTByYwRatr2p/y+wMuF5m/C8XfXsISP63A6GRzxzDs4kmcWZ06IknjO5v3mQBhpAxuD1YIx51T6fZcv/Jv+Vo2YzAo5jnQM47nzt3ZWBq7/ChL3KkZOdQvTppJIXgMJ+cAzH18MZxDqWYFyBcnVUd9rrLEKz7A/3tlLEih18WRlvGP3dEoLe0l7bW1ZnJT/zJ1qC2qgJT9uirRrSIl+YqA+Q==~1; bm_mi=8BE91DEBDB31D0BC6F4403C3BF7C2809~YAAQXX/NF00oo66BAQAAxV8O2hA8kfWrSC2DA4YIFf1Ov1OEaB1fJR+jm/9RiweXriMCVFJPzRcrgv9flUPaJPTAve1Zyyq/Vlqt2xGWMbYEcip4+YYn7O7o31XcmGp0c8xM3w1heXDx0fMlmcT5mh/Aiobooc+OL8TUhukQ0+PMWKSQZ7VQV1g7ZApe9Nd82+k8C9lpY1LsnIeAgW+gT/I+CZBrbtQam2x4deq5i8WpOci9B0M/9gPfTViEqv18db87f7qv4LP0EnUx5htJXP+Ttq11yoTZj5wMcjI48MWZxZzF2y2h2fdn5c2G/QDZBeZfRICYvwn0JBTQkpr2bBb6vQZO~1",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-origin",
        "TE": "trailers",
    }

    conn.request(
        "GET",
        f"/bff/air-offers/offers/search?sort=RECOMMENDED&cabinType=Economy&origin={airport}&destination=IGU&inFlightDate=null&inFrom=null&inOfferId=null&outFlightDate=null&outFrom={date_str}&outOfferId=null&adult=1&child=0&infant=0&redemption=false",
        payload,
        headers,
    )

    res = conn.getresponse()
    data = res.read()
    try:
        data_json = json.loads(gzip.decompress(data))["content"]
    # sometimes data comes only half compressed?
    except BadGzipFile:
        data = gzip.compress(data)
        decompressed_data = gzip.decompress(data)
        data_json = json.loads(decompressed_data)["content"]
    return data_json
