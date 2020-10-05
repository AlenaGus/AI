'''
Created on Dec 11, 2019

@author: Alyona

'''


#List of nodes
Nodes=[“Mathias”, “Bobby”, “Human”, “Cat”, ...]

#List of edges aka. “relations”
Edges=[(“is­a”,”cat”,”mammal”),(“has”,”mammal”,”vertebra”)  ]

#Propagating relations
def reason():
    Facts, NewFacts, i = Edges, list(Edges), 1
    while True:
        for E in Facts:
            if E[0] in Inheritable:
                R,A,B = E
                for N in Nodes:
                    if ("is­a",N,A) in Facts and (R,N,B) not in Facts:
                        NewFacts.append((R,N,B))
                        print("%d: %s %s %s"%(i,N,R,B))
        if Facts == NewFacts:
            break;
        Facts=NewFacts ; i=i+1