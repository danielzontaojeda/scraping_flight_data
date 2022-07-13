from file_manager import input

def teste(cidade):
	data = input.get_municipios_json()
	for city in data:
		if city['nome'] in cidade:
			print(city['regiao-imediata']['regiao-intermediaria']['UF']['nome'])
			break

teste("São Paulo")
teste("Curitiba")
teste("Rio de Janeiro")
teste("Brasília")
teste("Salvador da Bahia")
teste("Recife")
teste("Vitória")