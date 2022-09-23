Script to create a database with flight prices from airports around Brazil to a destination, to compare how the prices changes 30, 15 and 1 days before the flight date. Needs to be setup to run once per day.

## Output

Some examples of output created from flight going to Foz do Iguaçu (IGU)

|Região |Estado           |CidadeOrigem |AERO|DataViagem|Mês     |Ano |NúmeroVoo|Equipamento/Avi|CiaAérea             |CapacidadeAeronave|Hora Partida|Hora Chegada|Tipo de Trajeto|AeroportoConexão|DistânciaAéreaKM|Preço 30d|Preço 15d|Preço 1d|PreçoMédio|Yield Pax|
|-------|-----------------|-------------|----|----------|--------|----|---------|---------------|---------------------|------------------|------------|------------|---------------|----------------|----------------|---------|---------|--------|----------|---------|
|Norte  |Acre             |Rio Branco   |RBR |22/09/2022|Setembro|2022|1799     |7M8            |GOL                  |186               |02:45:00    |22:40:00    |Conexão        |BSB, SDU, GRU   |2226            |2159.27  |2366.27  |3030.37 |2518.64   |0.97     |
|Norte  |Acre             |Rio Branco   |RBR |22/09/2022|Setembro|2022|1819     |7M8            |GOL                  |186               |22:45:00    |17:30:00    |Conexão        |MAO, BSB, GRU   |2226            |1826.27  |2366.27  |3030.37 |2407.64   |0.82     |
|Sul    |Rio Grande do Sul|Caxias do Sul|CXJ |22/09/2022|Setembro|2022|1329     |73G            |GOL                  |144               |17:25:00    |22:40:00    |Conexão        |GRU             |525             |3025.33  |3027.33  |3027.33 |3026.66   |5.76     |
|Norte  |Roraima          |Boa Vista    |BVB |22/09/2022|Setembro|2022|2063     |7M8            |GOL                  |186               |01:20:00    |11:40:00    |Conexão        |BSB, GRU        |3226            |3038.93  |3038.93  |3038.93 |3038.93   |0.94     |
|Norte  |Roraima          |Boa Vista    |BVB |22/09/2022|Setembro|2022|2063     |7M8            |GOL                  |186               |01:20:00    |22:40:00    |Conexão        |BSB, GYN, GRU   |3226            |3038.93  |3038.93  |3038.93 |3038.93   |0.94     |
|Norte  |Roraima          |Boa Vista    |BVB |22/09/2022|Setembro|2022|2063     |7M8            |GOL                  |186               |01:20:00    |22:40:00    |Conexão        |BSB, SDU, GRU   |3226            |3038.93  |3038.93  |3038.93 |3038.93   |0.94     |
|Sudeste|São Paulo        |São Paulo    |GRU |22/09/2022|Setembro|2022|3336     |321            |LATAM AIRLINES BRASIL|198               |06:15:00    |07:55:00    |Direto         |                |835             |1267.16  |1311.16  |2583.16 |1720.49   |1.52     |
|Sudeste|São Paulo        |São Paulo    |GRU |22/09/2022|Setembro|2022|3338     |320            |LATAM AIRLINES BRASIL|174               |16:20:00    |18:00:00    |Direto         |                |835             |1267.16  |1538.16  |2971.16 |1925.49   |1.52     |
|Sudeste|São Paulo        |São Paulo    |GRU |22/09/2022|Setembro|2022|3340     |320            |LATAM AIRLINES BRASIL|174               |21:40:00    |23:20:00    |Direto         |                |835             |1267.16  |1311.16  |2971.16 |1849.83   |1.52     |
|Sudeste|São Paulo        |São Paulo    |GRU |22/09/2022|Setembro|2022|3320     |320            |LATAM AIRLINES BRASIL|174               |06:55:00    |14:10:00    |Conexão        |GIG             |835             |3039.26  |3039.26  |3039.26 |3039.26   |3.64     |


## Dependencies

* requests

* airportsdata

* unidecode 

* pytest

* selenium

* retry

`pip install requests airportsdata unidecode pytest selenium retry`

## Setup

A file `secrets.json` needs to be created in the root folder with:

```
{
  "CSV_BACKUP_FOLDER" : "",
  "EMAIL_LOGIN" : "",
  "EMAIL_PASSWORD" : ""
}
```

with the relevant data inserted.

Insert origin airport and firefox binary location in `config.py`

