OK_FORMAT = True

test = {   'name': 'q5_7',
    'points': [0, 2, 3],
    'suites': [   {   'cases': [   {'code': '>>> remaining_inventory.num_columns\n3', 'hidden': False, 'locked': False},
                                   {'code': ">>> remaining_inventory.column('count').item(0) != 45\nTrue", 'hidden': False, 'locked': False},
                                   {'code': ">>> remaining_inventory.where(1, 'grape')\nbox ID | fruit name | count\n57930  | grape      | 162", 'hidden': False, 'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
