OK_FORMAT = True

test = {   'name': 'q3_3',
    'points': None,
    'suites': [   {   'cases': [   {'code': ">>> set(faithful_residuals.labels) == set(['duration', 'wait', 'predicted wait', 'residual'])\nTrue", 'hidden': False, 'locked': False},
                                   {'code': ">>> abs(sum(faithful_residuals.column('residual'))) <= 1e-08\nTrue", 'hidden': False, 'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
