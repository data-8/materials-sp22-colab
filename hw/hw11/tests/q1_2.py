OK_FORMAT = True

test = {   'name': 'q1_2',
    'points': [0],
    'suites': [   {   'cases': [   {   'code': ">>> abs(correlation(Table().with_columns('a', np.random.normal(0, 1, 10), 'b', np.random.normal(0, 1, 10)), 'a', 'b')) <= 1\nTrue",
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
