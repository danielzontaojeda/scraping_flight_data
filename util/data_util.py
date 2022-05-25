import re


def is_time(string):
    pattern = "^([0-1]?[0-9]|2[0-3]):[0-5][0-9]$"
    return re.search(pattern, string)

def date_long(string):
    month = ["janeiro",
             "fevereiro",
             "março",
             "abril",
             "maio",
             "junho",
             "julho",
             "agosto",
             "setembro",
             "outubro",
             "novembro",
             "dezembro"
             ]

    string_split = string.split('/')
    return (f"{string_split[0]} de {month[int(string_split[1])-1]} de {string_split[2]}")


def string_to_float(string) -> float:
    pattern = "[\d]+[\.]?[0-9]+[,]?[0-9]{2}"
    result = re.search(pattern, string).group().replace('.', '').replace(',', '.')
    return float(result)
