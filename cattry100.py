'''
Created on Dec 12, 2019

@author: Alyona
'''
from rdflib import Graph, RDF, RDFS, Literal, BNode
from rdflib.namespace import FOAF
from rdflib.term import URIRef



g = Graph()

#main menu function
def menu():
    print('\n1 - Teach statment \n2 - Ask question \n3 - Print graph \n4 - Quit')
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
       
#question function         
def question():
    print ('What you would like to know?')
    question = input()
    question = question.replace('is', 'isa')
    extras = [" an", ' a', ' the',' to', 'does ', "?"] 
    for i in extras :  #cleaning question from extra words 
        question = question.replace(i, '')
    print ('looking for:', question) 
     
    zero, *rest = question.split()
    
    if zero == 'who': #who question
        
        first, second, third, *rest = question.split()
        WhoQ(first,second,third)
    
    elif zero == 'what': #what question
        
        first, second, third, *rest = question.split()
        WhatQ(first,second,third)
    
    else: 
        first, second, third, *rest = question.split()
        YesNoQ(first,second,third) #YesNo question
        

def WhoQ(firstQ,secondQ,thirdQ):
      
    print("________printing",secondQ, " ____________")
    for animal in g.subjects(RDF.type, FOAF.Animal):
        for parts in g.objects(animal, FOAF[secondQ]):
            if parts == URIRef(thirdQ):
                print(animal, secondQ, parts)

def WhatQ(firstQ,secondQ,thirdQ):
    
    if thirdQ == 'cat' or thirdQ == 'dog':
        secondQ, thirdQ = thirdQ, secondQ
       
    print("________printing",secondQ, thirdQ, " ____________")
    
    for animal in g.subjects(RDF.type, FOAF.Animal):
        if animal == URIRef(secondQ):
            for o in g.objects(animal, FOAF[thirdQ]):
                print(animal, thirdQ, o)
    
def YesNoQ(firstQ, secondQ, thirdQ):
    
    if secondQ == 'cat' or secondQ == 'dog':
        secondQ, firstQ = firstQ, secondQ
    if thirdQ == 'cat' or thirdQ == 'dog':
        firstQ, secondQ, thirdQ = thirdQ, firstQ, secondQ
        
       
    print("________printing",firstQ, secondQ, thirdQ, " ____________")
    
    YN = False
    for animal in g.subjects(RDF.type, FOAF.Animal):
        if animal == URIRef(firstQ):
            for o in g.objects(animal, FOAF[secondQ]):
                if o == URIRef(thirdQ):
                    YN = True
                    print('YES', animal, secondQ, o)
    
    if YN == False: print('not as I know of')

#add new line in the triplets    
def addStatment(sub,pred,obj):
    g.add((URIRef(sub),FOAF[pred], URIRef(obj)))

#paws counting
def subAdd():
    g.add((URIRef('4'), RDFS.subClassOf, URIRef('paws')))

#teaching a new piece of information    
def teach():
    print('What are you going to teach me?')
    statment = input()
    
    first, second, third, *rest = statment.split()
    
    if first == 'cat' or third == 'dog':
        print(first, second, third)
    elif third == 'cat' or third =='dog':
        third, first = first, third
        print(first, second, third)
    
    addStatment(first, second, third)

    
    print("__________printing raw triples_______")
    for s, p, o in g:
        print ((s, p, o))
    

if __name__ == '__main__':
    g = Graph()
    mammal = BNode()
    cat = URIRef('cat')
    dog = URIRef('dog')
    
#add triplets using
    g.add ((cat, RDF.type, FOAF.Animal))
    g.add ((cat, FOAF.has, URIRef('tail')))
    g.add ((cat, FOAF.has, URIRef('fur')))
    g.add ((cat, FOAF.has, URIRef('claws')))
    g.add ((cat, FOAF.can, URIRef('meow')))
    g.add ((cat, FOAF.can, URIRef('eat')))
    g.add ((cat, FOAF.likes, URIRef('sleep')))
    g.add ((cat, FOAF.likes, URIRef('play')))
    g.add ((cat, FOAF.likes, URIRef('eat')))
    
    g.add ((dog, RDF.type, FOAF.Animal))
    g.add ((dog, FOAF.has, URIRef('tail')))
    g.add ((dog, FOAF.has, URIRef('paws')))
    g.add ((Literal('4'), RDFS.subClassOf, URIRef('paws')))
    g.add ((dog, FOAF.has, URIRef('fur')))
    g.add ((dog, FOAF.has, URIRef('eyes')))
    g.add ((dog, FOAF.can, URIRef('bark')))
    g.add ((dog, FOAF.likes, URIRef('play')))
    g.add ((dog, FOAF.likes, URIRef('treats')))
    g.add ((dog, FOAF.chase, cat))
    g.add ((dog, FOAF.isa, URIRef('huskey')))
    g.add ((dog, FOAF.isa, URIRef('Snoopy')))
    
    
    menu()