OK_FORMAT = True

test = {   'name': 'q1_13',
    'points': [0, 0],
    'suites': [   {   'cases': [   {'code': ">>> region_counts.labels == ('region', 'count')\nTrue", 'hidden': False, 'locked': False},
                                   {'code': ">>> sum(region_counts.column('count')) == 50\nTrue", 'hidden': False, 'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
