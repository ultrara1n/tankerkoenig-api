# pytankerkoenig
[![](https://travis-ci.org/ultrara1n/pytankerkoenig.svg?branch=master)](https://travis-ci.org/ultrara1n/pytankerkoenig)
[![](https://img.shields.io/pypi/v/pytankerkoenig.svg)](https://pypi.org/project/pytankerkoenig/)

Python package for fuel data from tankerkoenig.de

## Prerequisites
You need to request an API-Key here: https://creativecommons.tankerkoenig.de.

For station details, find the station id via this tool: https://creativecommons.tankerkoenig.de/TankstellenFinder/index.html
## Installation
```bash
$ pip install pytankerkoenig
```
## Use
### getStationData(API_KEY, STATION_ID)
```python
>>> import pytankerkoenig
>>> data = pytankerkoenig.getStationData('00000000-0000-0000-0000-000000000002','24a381e3-0d72-416d-bfd8-b2f65f6e5802')
>>> print(data)
{
    'ok': True,
    'license': 'CC BY 4.0 -  https://creativecommons.tankerkoenig.de',
    'data': 'MTS-K',
    'status': 'ok',
    'station': {
        'id': '24a381e3-0d72-416d-bfd8-b2f65f6e5802',
        'name': 'Esso Tankstelle',
        'brand': 'ESSO',
        'street': 'HAUPTSTR. 7',
        'houseNumber': ' ',
        'postCode': 84152,
        'place': 'MENGKOFEN',
        'openingTimes': [{'text': 'Mo-Fr', 'start': '06:00:00',
                         'end': '22:00:00'}, {'text': 'Samstag',
                         'start': '07:00:00', 'end': '22:00:00'},
                         {'text': 'Sonntag, Feiertag',
                         'start': '08:00:00', 'end': '22:00:00'}],
        'overrides': [],
        'wholeDay': False,
        'isOpen': True,
        'e5': 1.009,
        'e10': 1.009,
        'diesel': 1.009,
        'lat': 48.72210601,
        'lng': 12.44438439,
        'state': None,
        },
    }
```

### getPriceList(API_KEY, STATION_IDS[])
```python
>>> import pytankerkoenig
>>> data = pytankerkoenig.getStationData('00000000-0000-0000-0000-000000000002',['5bd71e9d-7001-4908-a29d-36c28d6eb615','005056ba-7cb6-1ed2-bceb-92a737c6ad35'])
>>> print(data)
{
    'ok': True,
    'license': 'CC BY 4.0 -  https://creativecommons.tankerkoenig.de',
    'data': 'MTS-K',
    'prices': {'005056ba-7cb6-1ed2-bceb-92a737c6ad35': {
        'status': 'open',
        'e5': 1.234,
        'e10': 1.234,
        'diesel': 1.234,
        }, '5bd71e9d-7001-4908-a29d-36c28d6eb615': {
        'status': 'open',
        'e5': 1.234,
        'e10': 1.234,
        'diesel': 1.234,
        }},
    }
```
