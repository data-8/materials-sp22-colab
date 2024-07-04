OK_FORMAT = True

test = {   'name': 'q3_2_1',
    'points': [1.5, 1.5],
    'suites': [   {   'cases': [   {   'code': '>>> from collections import Counter\n'
                                               ">>> g = train_movies.column('Genre')\n"
                                               '>>> \n'
                                               '>>> def check(r, k):\n'
                                               '...     t = test_my_features.row(r)\n'
                                               '...     return classify(t, train_my_features, g, k) == Counter(np.take(g, np.argsort(fast_distances(t, train_my_features))[:k])).most_common(1)[0][0]\n'
                                               '>>> check_5_nn = [check(i, 5) for i in np.arange(11)]\n'
                                               '>>> all(check_5_nn)\n'
                                               'True',
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': '>>> from collections import Counter\n'
                                               ">>> g = train_movies.column('Genre')\n"
                                               '>>> \n'
                                               '>>> def check(r, k):\n'
                                               '...     t = test_my_features.row(r)\n'
                                               '...     return classify(t, train_my_features, g, k) == Counter(np.take(g, np.argsort(fast_distances(t, train_my_features))[:k])).most_common(1)[0][0]\n'
                                               '>>> check_11_nn = [check(i, 11) for i in np.arange(11)]\n'
                                               '>>> all(check_11_nn)\n'
                                               'True',
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
