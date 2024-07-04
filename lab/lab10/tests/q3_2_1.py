OK_FORMAT = True

test = {   'name': 'q3_2_1',
    'points': None,
    'suites': [   {   'cases': [   {   'code': '>>> import hashlib\n'
                                               '>>> \n'
                                               '>>> def get_hash(num):\n'
                                               '...     """Helper function for assessing correctness."""\n'
                                               '...     return hashlib.md5(str(num).encode()).hexdigest()\n'
                                               '>>> get_hash(int(rough_prob_cancer_given_positive))\n'
                                               "'a87ff679a2f3e71d9181a67b7542122c'",
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
