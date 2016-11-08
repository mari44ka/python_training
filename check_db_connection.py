
from fixture.orm import Ormfixture
from model.group import Group

db = Ormfixture(host="127.0.0.1",name="addressbook",user="root",password="")

try:
    l=db.get_contacts_in_group(Group(id="96"))
    for item in l:
        print(item)
    print(len(l))

finally:
    pass
    #db.destroy()