OK_FORMAT = True

test = {   'name': 'q2_4',
    'points': [0, 0],
    'suites': [   {   'cases': [   {'code': ">>> poverty_map.labels == ('latitude', 'longitude', 'name', 'region', 'poverty_total')\nTrue", 'hidden': False, 'locked': False},
                                   {'code': ">>> list(np.sort(np.unique(poverty_map.column('region'))))\n['africa', 'americas', 'asia', 'europe']", 'hidden': False, 'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
