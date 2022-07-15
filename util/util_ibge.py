from scraping_flight_data.file_manager import input


def get_uf_info(city_name):
	if city_name == "Porto Alegre":
		return{
			'state': 'Rio Grande do Sul',
			'region': 'Sul'
		}
	data = input.get_municipios_json()
	for city in data:
		if city['nome'] in city_name:
			return {
				'state': city['regiao-imediata']['regiao-intermediaria']['UF']['nome'],
				'region': city['regiao-imediata']['regiao-intermediaria']['UF']['regiao']['nome']
			}

