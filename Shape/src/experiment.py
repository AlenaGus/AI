'''
Created on Dec 6, 2019

@author: Alyona
'''

print('explain how L1 relate to M1')
quest = input()
mwords = quest.split()
print(mwords)
    
    
print ('A to B')
ques = input('1 - right, 2- left, 3 - above, 4 - below, 5 - upsize, 6 - downsize   ')
print(ques)

print ('C to 1')
ques1 = input('1 - right, 2- left, 3 - above, 4 - below, 5 - upsize, 6 - downsize   ')
print(ques1)

print ('C to 2')
ques2 = input('1 - right, 2- left, 3 - above, 4 - below, 5 - upsize, 6 - downsize   ')
print(ques2)

print ('C to 3')
ques3 = input('1 - right, 2- left, 3 - above, 4 - below, 5 - upsize, 6 - downsize   ')
print(ques3)

if ques == ques1:
    print('!1!')
    
elif ques == ques2:
    print('!2!')
else: 
    if ques == ques3: 
        print('!3!')
    else: print ('none')
    
    
    
    
    if quest == 'y':
            g.add(l, FOAF.changed, l1)
    elif quest == 'n': g.add(l, FOAF.unchanged, l1)
    else: print ('y or n') 

def YNQestion():
    
    print('Does L chaned?')
    quest = input()
    
    if quest == 'y':
        print('is L1 bigger than L2?')
        if input() == 'y':
            g.add(l, FOAF.bigger, l1)
        else: g.add(l, FOAF.smaller, l1)
    elif quest == 'n': g.add(l, FOAF.unchanged, l1)
    else: print ('y or n')
    
    print('is there new objects?')
    quest = input()
    
    if quest == 'y':
        graphG_count = +1
        
    elif quest == 'n':
        print('is L1 bigger than L2?')
            g.add(l, FOAF.bigger, l1)
        else: g.add(l, FOAF.smaller, l1)
    elif quest == 'n': g.add(l, FOAF.unchanged, l1)
    else: print ('y or n')
    
    
            



