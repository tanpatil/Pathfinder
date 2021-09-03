import unittest
from Node import *
from Dijkstra import *


class TestDijkstra(unittest.TestCase):

    def test_path(self):
        A = Node('A')
        B = Node('B')
        C = Node('C')
        D = Node('D')
        E = Node('E')
        F = Node('F')
        G = Node('G')
        H = Node('H')
        I = Node('I')
        J = Node('J')
        K = Node('K')
        L = Node('L')
        M = Node('M')

        A.add_connection(B, 4)
        A.add_connection(K, 10)
        A.add_connection(E, 5)
        B.add_connection(C, 7)
        K.add_connection(C, 6)
        K.add_connection(E, 7)
        K.add_connection(L, 15)
        K.add_connection(G, 6)
        E.add_connection(F, 7)
        F.add_connection(H, 4)
        F.add_connection(G, 2)
        H.add_connection(I, 1)
        G.add_connection(I, 5)
        G.add_connection(L, 2)
        I.add_connection(L, 3)
        I.add_connection(J, 4)
        J.add_connection(L, 11)
        J.add_connection(M, 1)
        M.add_connection(L, 2)
        L.add_connection(D, 5)
        D.add_connection(C, 9)

        dx = Dijkstra(A, J, [A, B, C, D, E, F, G, H, I, J, K, L, M])
        self.assertEqual(dx.get_route(), "A->E->F->G->L->M->J", "The path should be \nA->E->F->G->L->M->J")


if __name__ == "__main__":
    unittest.main()
