import re


def string_to_float(string):
    pattern = "[\d]+[\.]?[0-9]+[,]?[0-9]{2}"
    result = re.search(pattern, string).group().replace('.', '').replace(',', '.')
    return float(result)
