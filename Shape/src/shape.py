'''
Created on Dec 6, 2019

@author: Alyona
'''
from rdflib import Graph, Literal, BNode, Namespace, RDF, URIRef
from rdflib.graph import ConjunctiveGraph, ReadOnlyGraphAggregate

from rdflib.namespace import DC, FOAF

class IsomorphicGraph(ConjunctiveGraph):

    def __init__(self, **kwargs):
        super(IsomorphicGraph, self).__init__(**kwargs)

    def __eq__(self, other):
        """Graph isomorphism testing."""
        if not isinstance(other, IsomorphicGraph):
            return False
        elif len(self) != len(other):
            return False
        elif list(self) == list(other):
            return True  # TODO: really generally cheaper?
        return self.internal_hash() == other.internal_hash()

    def __ne__(self, other):
        """Negative graph isomorphism testing."""
        return not self.__eq__(other)

    def internal_hash(self):
        """
        This is defined instead of __hash__ to avoid a circular recursion
        scenario with the Memory store for rdflib which requires a hash lookup
        in order to return a generator of triples.
        """
        return _TripleCanonicalizer(self).to_hash()

class _TripleCanonicalizer(object):

    def __init__(self, graph, hashfunc=hash):
        self.graph = graph
        self.hashfunc = hashfunc

    def to_hash(self):
        return self.hashfunc(tuple(sorted(
            map(self.hashfunc, self.canonical_triples()))))

    def canonical_triples(self):
        for triple in self.graph:
            yield tuple(self._canonicalize_bnodes(triple))

    def _canonicalize_bnodes(self, triple):
        for term in triple:
            if isinstance(term, BNode):
                yield BNode(value="cb%s" % self._canonicalize(term))
            else:
                yield term

    def _canonicalize(self, term, done=False):
        return self.hashfunc(tuple(sorted(self._vhashtriples(term, done),
                                          key=_hetero_tuple_key)))

    def _vhashtriples(self, term, done):
        for triple in self.graph:
            if term in triple:
                yield tuple(self._vhashtriple(triple, term, done))

    def _vhashtriple(self, triple, target_term, done):
        for i, term in enumerate(triple):
            if not isinstance(term, BNode):
                yield term
            elif done or (term == target_term):
                yield i
            else:
                yield self._canonicalize(term, done=True)
                
def _hetero_tuple_key(x):
    "Sort like Python 2 - by name of type, then by value. Expects tuples."
    return tuple((type(a).__name__, a) for a in x)

def to_isomorphic(graph):
    if isinstance(graph, IsomorphicGraph):
        return graph
    return IsomorphicGraph(store=graph.store)

def isomorphic(graph1, graph2):
    """Compare graph for equality.
    Uses an algorithm to compute unique hashes which takes bnodes into account."""

    gd1 = _TripleCanonicalizer(graph1).to_hash()
    gd2 = _TripleCanonicalizer(graph2).to_hash()
    return gd1 == gd2

def similar(g1, g2):
    """Checks if the two graphs are "similar".
    Checks if the two graphs are "similar", by comparing sorted triples where
    all bnodes have been replaced by a singular mock bnode (the
    ``_MOCK_BNODE``).
    This is a much cheaper, but less reliable, alternative to the comparison
    algorithm in ``isomorphic``.
    """
    return all(t1 == t2 for (t1, t2) in _squashed_graphs_triples(g1, g2))

def _squashed_graphs_triples(g1, g2):
    for (t1, t2) in zip(sorted(_squash_graph(g1)), sorted(_squash_graph(g2))):
        yield t1, t2

def _squash_graph(graph):
    return (_squash_bnodes(triple) for triple in graph)


def _squash_bnodes(triple):
    return tuple((isinstance(t, BNode) and _MOCK_BNODE) or t for t in triple)

def graph_diff(g1, g2):
    """Returns three sets of triples: "in both", "in first" and "in second"."""
    # bnodes have deterministic values in canonical graphs:
    cg1 = to_canonical_graph(g1)
    cg2 = to_canonical_graph(g2)
    in_both = cg1 * cg2
    in_first = cg1 - cg2
    in_second = cg2 - cg1
    return (in_both, in_first, in_second)


_MOCK_BNODE = BNode()

def to_canonical_graph(g1, stats=None):
    """Creates a canonical, read-only graph.
    Creates a canonical, read-only graph where all bnode id:s are based on
    deterministical SHA-256 checksums, correlated with the graph contents.
    """
    graph = Graph()
    graph += _TripleCanonicalizer(g1).canonical_triples(stats=stats)
    return ReadOnlyGraphAggregate([graph])

if __name__ == '__main__':
    
    
    g = Graph()
    graph1 = Graph()
    graph2 = Graph()
    graph3 = Graph()


#creating inteface to use as the subject for cat
    m = BNode()
    m1 = BNode()
    m2 = BNode()
    l= BNode()
    l1 = BNode()
    l2 = BNode()
    x = BNode()
    x1 = BNode()
    x2  = BNode()
    y = BNode()
    y1 = BNode()
    y2 = BNode()

    g.add ((l1, FOAF.above, m1))

    
    graph1.add((x2, FOAF.below, y2))
    graph1.add((x1, FOAF.samesize, x2))
    graph1.add((x1, FOAF.above, y1))
    graph1.add((y1, FOAF.samesize, y2))
    
    graph2.add((x1, FOAF.samesize, x2))
    graph2.add((y1, FOAF.samesize, y2))
    graph2.add((x1, FOAF.above, y1))
    graph2.add((x2, FOAF.leftof, y2))
    
    graph3.add((x1, FOAF.samesize, x2))
    graph3.add((y1, FOAF.samesize, y2))
    graph3.add((x1, FOAF.above, y1))
    graph3.add((x2, FOAF.rightof, y2))


   
    print('explain how L(new) relate to M(new) on second image')
    quest = input()
    mwords = quest.split()
    print(mwords)
    
    for i in mwords : 
        g.add((l1,FOAF[i],m1))
        
    print('_________printing g_____________')
    for s, p, o in g:
        print ((s, p, o))
        
    print('is L(new) same size as L(old)?')
    if input() == 'yes':
        g.add((l1, FOAF.samesize, l2))
    else: g.add((l1, FOAF.difsize, l2))
    
    print('is M(new) same size as M(old)?')
    if input() == 'yes':
        g.add((m1, FOAF.samesize, m2))
    else: g.add((m1, FOAF.difsize, m2))
    
    print('_________printing g_____________')
    
    for s, p, o in g:
        print ((s, p, o))
        
    iso1 = to_isomorphic(graph1)
    iso2 = to_isomorphic(graph2)
    iso3 = to_isomorphic(graph3)
    isoo = to_isomorphic(g)

    print('I choose 2')
    
    if isoo == iso1 :
        print('I choose 1')
    elif isoo == iso2: 
        print('I choose 2')
    elif isoo == iso3:
        print('I choose 3')
    else: print("I don't like any of those")
    
    
    
    print(isomorphic(g, graph1))
    print(isomorphic(isoo, iso1))
    
    print(isomorphic(g, graph2))
    print(isomorphic(isoo, iso2))
    print(isomorphic(g, graph3))
    print(isomorphic(isoo, iso3))
    
    if isomorphic(g, graph2)==True:
        print('true')
    else: print('not true')
    
    in_both = graph_diff(isoo, iso2)

    
        

        
 
    
