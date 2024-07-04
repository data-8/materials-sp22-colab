OK_FORMAT = True

test = {   'name': 'q2_3',
    'points': [1, 1, 1, 1],
    'suites': [   {   'cases': [   {'code': '>>> len(simulated_tvds) == 10000\nTrue', 'hidden': False, 'locked': False},
                                   {'code': '>>> all(simulated_tvds >= 0)\nTrue', 'hidden': False, 'locked': False},
                                   {'code': '>>> len(np.unique(simulated_tvds)) != 1\nTrue', 'hidden': False, 'locked': False},
                                   {'code': '>>> np.mean(simulated_tvds) < 0.1\nTrue', 'hidden': False, 'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
