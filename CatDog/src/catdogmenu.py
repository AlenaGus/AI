'''
Created on Dec 11, 2019

@author: Alyona
'''
from rdflib import Graph, RDF, RDFS, Literal
from rdflib.namespace import FOAF
from rdflib.term import URIRef

g = Graph()

def menu():
    print('1 - Teach statment \n2 - Ask question \n3 - Print graph \n4 - Quit')
    while True:
        try:
            choise = int(input())
    
            if choise == 1:
                teach()
                menu()
        
            elif choise == 2:
                question()
                menu()
    
            elif choise == 3:
                print("__________printing raw triples_______")
                for s, p, o in g:
                    print ((s, p, o))
                menu()
        
            elif choise == 4:
                break
        
            else:
                print('Invalid choise, input 1-4')
                menu()
        except ValueError:
            print('Invalid choise, input 1-4')
    exit
        
def question():
    print ('')
    
def teach():
    print('What are you going to teach me?')
    statment = input()
    
    first, second, third, *rest = statment.split()
    
    if first == 'cat' or third == 'dog':
        print(first, second, third)
    elif third == 'cat' or third =='dog':
        third, first = first, third
        print(first, second, third)
    
   # cat.add((FOAF.__new__(URIRef(),second), URIRef(third)))
    
    g.add((URIRef(first),FOAF(second),Literal(third)))
   
    

    print("__________printing raw triples_______")
    for s, p, o in g:
        print ((s, p, o))
    


if __name__ == '__main__':

     
    cat = g.resource('urn:cat')

    cat.set(RDF.type, FOAF.Animal)  # .set replaces all other values
    cat.set(FOAF.name, Literal("Cat"))

    dog = g.resource('urn:dog')

    dog.add(RDF.type, FOAF.Animal)  # add adds to existing values
    dog.set(RDFS.label, Literal("Dog"))

    dog.add(FOAF.has, URIRef('tail'))
    dog.add(FOAF.has, Literal('fur'))
    dog.add(FOAF.can, URIRef('bark'))
    dog.add(FOAF.like, URIRef('play'))
    
    cat.add(FOAF.has, URIRef('tail'))
    cat.add(FOAF.has, Literal('fur'))
    cat.add(FOAF.has, URIRef('paw'))
    cat.add(FOAF.can, URIRef('moew'))
    cat.add(FOAF.like, URIRef('play'))
    cat.add(FOAF.like, URIRef('sleep'))

    print("Cat's has: ", cat.value(FOAF.has))
    
    print("Cat has: ")
    for parts in cat[FOAF.has]:
        print(parts)
        
    menu()