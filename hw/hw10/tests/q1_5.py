OK_FORMAT = True

test = {   'name': 'q1_5',
    'points': [0, 0, 0],
    'suites': [   {   'cases': [   {'code': '>>> len(parameters) == 3\nTrue', 'hidden': False, 'locked': False},
                                   {'code': '>>> type(parameters) == np.ndarray\nTrue', 'hidden': False, 'locked': False},
                                   {'code': '>>> np.isclose(parameters.item(0), 0.8343076972837598)\nTrue', 'hidden': False, 'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
