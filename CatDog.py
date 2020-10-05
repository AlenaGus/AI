'''
Created on Nov 8, 2019

@author: Alyona
'''
from rdflib import Graph, Literal, BNode, Namespace, RDF, URIRef
from rdflib.namespace import DC, FOAF


g = Graph()
mammal = BNode()

#creating inteface to use as the subject for cat
cat = URIRef('cat')
dog = URIRef('dog')
tail = URIRef('tail')

#add triplets using store's add method
g.add ((cat, RDF.type, FOAF.Animal))
g.add ((cat, FOAF.has, URIRef('tail')))
g.add ((cat, FOAF.has, Literal('fur')))
g.add ((cat, FOAF.has, URIRef('claws')))
g.add ((cat, FOAF.can, Literal('meow')))

g.add ((dog, RDF.type, FOAF.Animal))
g.add ((dog, FOAF.has, URIRef('tail')))
g.add ((dog, FOAF.can, Literal('bark')))
g.add ((dog, FOAF.chase, cat))

print("__________printing raw triples_______")
for s, p, o in g:
    print ((s, p, o))
    
print(g.serialize(format='n3'))

    # Serialize as XML
print("--- start: rdf-xml ---")
print(g.serialize(format="pretty-xml"))
print("--- end: rdf-xml ---\n")

    # Serialize as Turtle
print("--- start: turtle ---")
print(g.serialize(format="turtle"))
print("--- end: turtle ---\n")

    # Serialize as NTriples
print("--- start: ntriples ---")
print(g.serialize(format="nt"))
print("--- end: ntriples ---\n")
    
    
print("________printing has ____________")
for animal in g.subjects(RDF.type, FOAF.Animal):
    for part in g.objects(animal, FOAF.has):
        print(part)
        
print("________printing cat has ____________")
for i in g.objects(cat, FOAF.has):
    print (i)

    
        
# g.bind ("dc", DC)
# g.bind ("foaf", FOAF)
# 
# print( g.serialize(format='n3'))     



qors = input("Q-uestion or S-tatment: ")
if qors == 'q' or qors == 'Q':
    print(qors, 'What you would like to know?')
    
    question = input()
    zero, *rest = question.split()
    
    if zero == 'who':
        print("___")
        whoqu = question
        first, second, third, *rest = whoqu.split()
        print(second)
        
        #for animal in g.subjects(RDF.type, FOAF.Animal):
            #if g.objects(animal, FOAF.match(second),  URIRef.match(third) ):
               #print(animal)
        print("________printing has ____________")
        for animal in g.subjects(RDF.type, FOAF.Animal):
            for has in g.objects(animal, FOAF.has):
                print(animal,second,has)   
            #print('written by: %s' % writer['name'].encode('utf-8'))
            
        for s,p,o in g:
            if p == has:
                print ((s,p,o))
                
    else: print ('not found')
        
    
    
    
 
elif qors == 's' or qors == "S":
    print(qors, 'What are you going to teach me?')
    
    statment = input()
    first, second, third, *rest = statment.split()
    
    if first == 'cat' or first == 'dog':
        print(first, second, third)
    elif third == 'cat' or third =='dog':
        third, first = first, third
        print(first, second, third)
    g.add((BNode(first), FOAF.__new__(second), URIRef(third)))
    

    print("__________printing raw triples_______")
    for s, p, o in g:
        print ((s, p, o))
        
    print(g.serialize(format='n3'))
    
   
else: print('Oh, come on, q or s?')



def addStuff(sub,pred,obj):
    
    
  
    if pred == 'has':
        g.add((URIRef(sub),FOAF.has, URIRef(obj)))
    elif pred == 'can':
        g.add((URIRef(sub), FOAF.can, URIRef(obj)))
    elif pred == 'likes':
        g.add((URIRef(sub), FOAF.likes, URIRef(obj)))
    elif pred == 'is a' or pred =='is' or pred =='is an':
        g.add((URIRef(sub), FOAF.isa, URIRef(obj)))
    elif pred == 'eats':
        g.add((URIRef(sub), FOAF.eats, URIRef(obj)))
    else: print("Use defined connaction")