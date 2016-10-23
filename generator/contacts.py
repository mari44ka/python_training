import random
import string
from model.contact1 import Contact1
import os.path
import jsonpickle
import getopt
import sys

try:
    opts,args=getopt.getopt(sys.argv[1:],"n:f:", ["number of groups","file"])
except getopt.GetoptError as err:
    getopt.usage()
    sys.exit(2)
n = 5
f = "data/contacts.json"

for o, a in opts:
    if o == "-n":
       n = int(a)
    elif o=="-f":
         f = a

def random_string(prefix,maxlen):
    symbols=string.ascii_letters + string.digits + string.punctuation + ""*10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])

testdata =[Contact1(fname="",mname="",lname="",nname="",title="",compname="",
           address="",hphone="",mphone="",wphone="",faxnumber="",secondphone="",
           e_mail="",e_mail2="",e_mail3="",home_page="",birth_year="",address_2="",notes="")] + [
    Contact1(fname=random_string("fname",10),mname=random_string("mname",10),lname=random_string("lname",15),
             nname=random_string("nname",5),title=random_string("title",4),compname=random_string("compname",10),
           address=random_string("address",20),hphone=random_string("hphone",10),mphone=random_string("mphone",10),
             wphone=random_string("wphone",10),faxnumber=random_string("faxnumber",10),secondphone=random_string("secondphone",10),
           e_mail=random_string("e_mail",20),e_mail2=random_string("e_mail2",20),e_mail3=random_string("e_mail3",20),
             home_page=random_string("home_page",22),birth_year=random_string("birth_year",4),
             address_2=random_string("address_2",20),notes=random_string("notes",25))
    for i in range(n)]

file = os.path.join(os.path.dirname(os.path.abspath(__file__)),"..",f)
with open(file,"w") as out:
    jsonpickle.set_encoder_options("json", indent=2)
    out.write(jsonpickle.encode(testdata))
