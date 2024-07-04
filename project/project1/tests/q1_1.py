OK_FORMAT = True

test = {   'name': 'q1_1',
    'points': [0, 0],
    'suites': [   {   'cases': [   {'code': ">>> b_pop.labels == ('time', 'population_total')\nTrue", 'hidden': False, 'locked': False},
                                   {'code': ">>> all(b_pop.sort('time').column('time') == np.arange(1970, 2021))\nTrue", 'hidden': False, 'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
