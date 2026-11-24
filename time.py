import time
timestrip=time.strftime('%A, %d, %B %Y %H:%M:%S')
print('Today is\t  ',timestrip)
timestri=int(time.strftime('%H'))
if(timestri>0 or timestri<12):
    print("Good Morning Sir",'\nHave a good breakfast')
elif(timestri>=12 or timestri<17):
    print("Good Afternoon",'\nHave a good lunch')
elif(timestri>=17 or timestri<20):
    print("Good Evening",'\nhave a good dinner')
else:
    print("Good Night",'\nHave sweet dreams')
match timestri:
    case 9:
        print(timestri,'bje gye bhai')
    
    case _:
        print(timestri,'hour of day is over now and yet you not start study yet')