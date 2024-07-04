OK_FORMAT = True

test = {   'name': 'q2_9',
    'points': None,
    'suites': [   {   'cases': [   {'code': '>>> len(differences)\n5000', 'hidden': False, 'locked': False},
                                   {'code': '>>> abs(np.average(differences)) < 0.05\nTrue', 'hidden': False, 'locked': False},
                                   {'code': '>>> all(differences == differences.item(0)) == False\nTrue', 'hidden': False, 'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
