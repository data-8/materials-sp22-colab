OK_FORMAT = True

test = {   'name': 'q521',
    'points': None,
    'suites': [   {   'cases': [   {'code': '>>> import numpy as np\n>>> type(total_charges) == np.ndarray\nTrue', 'hidden': False, 'locked': False},
                                   {'code': '>>> import numpy as np\n>>> sum(abs(total_charges - np.array([24.144, 47.88, 37.212]))) < 1e-06\nTrue', 'hidden': False, 'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
