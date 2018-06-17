try:
    import urllib2 as request
except:
    from urllib import request

import json

FUEL_TYPES = [
    'gasolina_93',
    'gasolina_95',
    'gasolina_97',
    'glp_vehicular',
    'gnc',
    'kerosene',
    'petroleo_diesel'
]


def get(fuel_type, commune=None, dist=None):
    result = {}
    url = 'http://api.cne.cl/api/listaInformacion/%s' % TOKEN
    response = request.urlopen(url)
    encoding = response.headers['content-type'].split('charset=')[-1]
    res = json.loads(response.read().decode(encoding))

    if res.get('estado') != 'OK':
        return {}

    data = res.get('data')

    if commune:
        data = filter(
            lambda x: x['nombre_comuna'].lower() == commune, data)

    if dist:
        data = filter(
            lambda x: x['nombre_distribuidor'].lower() == dist, data)

    if fuel_type in FUEL_TYPES:
        data = list(filter(
            lambda x: fuel_type in x['precio_por_combustible'], data))

        if len(data) > 0:
            result = min(
                data,
                key=lambda x: x['precio_por_combustible'][fuel_type])

    return result
