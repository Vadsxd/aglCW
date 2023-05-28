import unittest

import Hash_Table
import RBT

hash_test = []

answers = [[8, 4, 2, 1, 3, 6, 5, 7, 16, 12, 10, 9, 11, 14, 13, 15, 20, 18, 17, 19, 24, 22, 21, 23, 26, 25, 28, 27, 29],
           [None, None, [2, 'Yes'], None, [4, 'Mother'], [57, 'Too Hard'], None, None, None, ['a', 'Make Collition'], None, None, None, None]
           ]


class MyTestCase(unittest.TestCase):
    def test_tree(self):
        tree = RBT.Tree()
        for x in range(1, 30):
            tree.insert(x)
        self.assertEqual(tree.pre_order(tree.root, []), answers[0])

    def test_hash(self):
        table = Hash_Table.HashTable()
        table.put(2, "Yes")
        table.put(4, "Mother")
        table.put("a", "Make Collition")
        table.put(57, "Too Hard")
        self.assertEqual(table.get_table(), answers[1])


if __name__ == '__main__':
    unittest.main()
