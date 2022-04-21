# Buscador de manutenções programadas da CEMIG

* Fonte dos dados: [link](https://www.cemig.com.br/atendimento/aviso-de-desligamento-programado/)
* Biblioteca desenvolvida e testada com `Python@3.8`
* Bibliotecas necesssárias para funcionamento (vide `requirements.txt`):
  * `BeautifulSoup`
  * `Pandas`
  * `requests`
  * `xlrd`

## Como executar

#### Manual
```bash
usage: main.py [-d DATE] [-h] city

Crawler para verificar manutenções programadas da CEMIG

positional arguments:
  city                  Nome da cidade para procurar

optional arguments:
  -d DATE, --date DATE  Data para verificar no formato dd/mm/yyyy
  -h, --help            Mostra essa mensagem e sai.
```

#### Exemplo genérico

```bash
python main.py <Nome da cidade>
python main.py <Nome da cidade> -d <Data desejada no formato dd/mm/yyyy>
```

#### Exemplo específico
```bash
python main.py Timóteo
python main.py Ipatinga -d 05/05/2022
```