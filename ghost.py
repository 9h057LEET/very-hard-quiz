print('Dobrodosao u πΏΚ°πΆπ»π½ Kviz')
answer=input('Jesi spreman/na za Kviz ? (da/ne) :')
score=0
total_questions=3
 
if answer.lower()=='da':
    answer=input('Pitanje 1: Ko je pitao?')
    if answer.lower()=='tvoja keva':
        score += 1
        print('tacno')
    else:
        print('Netacno (posevatujte se sa lekarom ili farmaceutom)')
 
 
    answer=input('Pitanje 2: Imas li πΏΚ°πΆπ»π½#1337 u prijateljima ')
    if answer.lower()=='da':
        score += 1
        print('ok')
    else:
        print('Netacno (posevatujte se sa lekarom ili farmaceutom)')
 
    answer=input('Pitanje 3: Hoces li dodati πΏΚ°πΆπ»π½#1337 u prijatelje na discordu??')
    if answer.lower()=='da':
        score += 1
        print('super')
    else:
        print('Netacno (posevatujte se sa lekarom ili farmaceutom)')
 
print('Hvala sto si igrao ovaj Kviz,dao si',score,"odgovor/a tacno!")
mark=(score/total_questions)*120
print(f'Dobijena ocena:',mark)
print('mrs u kurac')