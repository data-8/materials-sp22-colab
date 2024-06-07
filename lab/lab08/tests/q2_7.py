OK_FORMAT = True

test = {   'name': 'q2_7',
    'points': None,
    'suites': [   {   'cases': [   {   'code': '>>> import hashlib # This imports a hashing library for the autograder.\n'
                                               '>>> def get_hash(num):\n'
                                               '...     """Helper function for assessing correctness."""\n'
                                               '...     return hashlib.md5(str(num).encode()).hexdigest()\n'
                                               '>>> \n'
                                               '>>> get_hash(set(np.array(pop_vs_sample).astype(int))) == get_hash(set(np.array(make_array(3, 4)).astype(int)))\n'
                                               'True',
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
