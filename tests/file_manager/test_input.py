from scraping_flight_data.src.file_manager import input


def test_get_airport_list():
    assert input.get_airport_list() == [
        "GRU",
        "CWB",
        "CGH",
        "VCP",
        "GIG",
        "POA",
        "BSB",
        "SSA",
        "FLN",
        "REC",
        "BEL",
        "VIX",
        "SDU",
        "CGB",
        "CGR",
        "FOR",
        "MCP",
        "GYN",
        "NVT",
        "MAO",
        "NAT",
        "BPS",
        "MCZ",
        "PMW",
        "SLZ",
        "PVH",
        "RBR",
        "CXJ",
        "BVB",
        "CFB",
    ]


def test_get_municipios_json():
    assert input.get_municipios_json()
