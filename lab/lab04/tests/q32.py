OK_FORMAT = True

test = {   'name': 'q32',
    'points': None,
    'suites': [   {   'cases': [   {'code': ">>> 'Total Pay ($)' in compensation.labels\nTrue", 'hidden': False, 'locked': False},
                                   {   'code': ">>> t = compensation.sort('Total Pay ($)', descending=True)\n>>> np.isclose(t.column('Total Pay ($)').item(0), 53250000.0)\nTrue",
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
