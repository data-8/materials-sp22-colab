OK_FORMAT = True

test = {   'name': 'q1_5',
    'points': [0, 0, 0],
    'suites': [   {   'cases': [   {'code': ">>> fertility_over_time('usa', 2010).labels == ('Year', 'Children per woman')\nTrue", 'hidden': False, 'locked': False},
                                   {'code': ">>> all(fertility_over_time('usa', 2010).column('Year') == np.arange(2010, 2021))\nTrue", 'hidden': False, 'locked': False},
                                   {'code': ">>> all(fertility_over_time('usa', 2005).column('Year') == np.arange(2005, 2021))\nTrue", 'hidden': False, 'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
