OK_FORMAT = True

test = {   'name': 'q2_4',
    'points': None,
    'suites': [   {   'cases': [   {   'code': '>>> import hashlib\n'
                                               '>>> \n'
                                               '>>> def get_hash(num):\n'
                                               '...     """Helper function for assessing correctness."""\n'
                                               '...     return hashlib.md5(str(num).encode()).hexdigest()\n'
                                               '>>> get_hash(set(np.array(q2_4).astype(int))) == get_hash(set(np.array(make_array(1, 4)).astype(int)))\n'
                                               'True',
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
