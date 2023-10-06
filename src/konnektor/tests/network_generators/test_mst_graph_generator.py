# This code is part of OpenFE and is licensed under the MIT license.
# For details, see https://github.com/OpenFreeEnergy/konnektor

import pytest
import numpy as np
import networkx as nx

from konnektor.network_generator_algorithms import MstNetworkGenerator
from konnektor.tests.data.conf import nine_mols_edges


def test_mst_network_generation_find_center(nine_mols_edges):
        expected_edges = [('lig_12', 'lig_14'), ('lig_12', 'lig_13'), ('lig_12', 'lig_10'),
                          ('lig_12', 'lig_16'), ('lig_12', 'lig_8'), ('lig_12', 'lig_15'),
                          ('lig_12', 'lig_11'), ('lig_12', 'lig_9')]

        edges = [(e[0], e[1]) for e in nine_mols_edges]
        weights = [e[2] for e in nine_mols_edges]
        nodes = set([n for e in edges for n in e])

        gen = MstNetworkGenerator()
        g = gen.generate_network(edges, weights)

        assert len(nodes)-1 == len(g.edges)
        assert [e in g.edges for e in expected_edges]
        assert all([e[0]!=e[1] for e in g.edges]) # No self connectivity
        assert isinstance(g, nx.Graph)