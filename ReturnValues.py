'''
def allowed_dating_age(my_age):
    girls_age= my_age/2+7
    return girls_age

Bittus_limit= allowed_dating_age(18)
deepaks_limit=allowed_dating_age(21)
aloks_limit=allowed_dating_age(20)
print("Bittu can date girls",Bittus_limit,"or over")
print("deepak can date girls",deepaks_limit,"or over")
print("alok can date girls",aloks_limit,"or over")
'''

#GO from 15 to 60 age and print all dating ages..

def my_age():
    print(15,61)

def allowed_dating_age(my_age):
    girls_age= my_age/2+7
    return girls_age

Peoples_limit= allowed_dating_age(my_age())
print("People  can date girls",Peoples_limit,"or over")


