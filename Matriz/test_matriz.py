import unittest
import matriz

class TestMatrix(unittest.TestCase):

    def test_seqVertical(self):
        matrix = [
            [1, 3, 2, 4, 5],
            [2, 3, 5, 6, 7],
            [9, 8, 7, 3, 4],
            [4, 8, 6, 7, 3],
            [2, 3, 7, 6, 5]
        ]
        seq = [5, 7, 6, 7]

        self.assertTupleEqual(matriz.findSeq(matrix, seq), ((2, 3), (5, 3)))


    def test_seqHorizontal(self):
        matrix = [
            [1, 3, 2, 4, 5],
            [2, 3, 5, 6, 7],
            [9, 8, 7, 3, 4],
            [4, 8, 6, 7, 3],
            [2, 3, 7, 6, 5]
        ]
        seq = [8, 7, 3, 4]

        self.assertTupleEqual(matriz.findSeq(matrix, seq), ((3, 2), (3, 5)))


    def test_seqVerticalInvertida(self):
        matrix = [
            [1, 3, 2, 4, 5],
            [2, 3, 5, 6, 7],
            [9, 8, 7, 3, 4],
            [4, 8, 6, 7, 3],
            [2, 3, 7, 6, 5]
        ]
        seq = [8, 8, 3, 3]

        self.assertTupleEqual(matriz.findSeq(matrix, seq), ((4, 2), (1, 2)))


    def test_seqHorizontalInvertida(self):
        matrix = [
            [1, 3, 2, 4, 5],
            [2, 3, 5, 6, 7],
            [9, 8, 7, 3, 4],
            [4, 8, 6, 7, 3],
            [2, 3, 7, 6, 5]
        ]
        seq = [3, 7, 6, 8]

        self.assertTupleEqual(matriz.findSeq(matrix, seq), ((4, 5), (4, 2)))


    def test_sinCoincidencias(self):
        matrix = [
            [1, 3, 2, 4, 5],
            [2, 3, 5, 6, 7],
            [9, 8, 7, 3, 4],
            [4, 8, 6, 7, 3],
            [2, 3, 7, 6, 5]
        ]
        seq = [3, 3, 6, 8]

        self.assertEqual(matriz.findSeq(matrix, seq), 0)

if __name__ == '__main__':
    unittest.main()
