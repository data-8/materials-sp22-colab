OK_FORMAT = True

test = {   'name': 'q2_2',
    'points': [0, 0, 0],
    'suites': [   {   'cases': [   {'code': ">>> recent_poverty_total.labels == ('geo', 'poverty_percent', 'population_total', 'poverty_total')\nTrue", 'hidden': False, 'locked': False},
                                   {'code': ">>> recent_poverty_total.where('geo', 'aus').column(2).item(0)\n22154687", 'hidden': False, 'locked': False},
                                   {'code': ">>> float(recent_poverty_total.where('geo', 'aus').column(3).item(0))\n301304.0", 'hidden': False, 'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
