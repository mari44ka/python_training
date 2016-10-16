from sys import maxsize



class Contact1:
    def __init__(self,fname=None, mname=None, lname=None, nname=None, title=None, compname=None, address=None,
     hphone=None, mphone=None, wphone=None, faxnumber=None, e_mail=None, e_mail2=None, e_mail3=None,
                 home_page=None, birth_year=None, address_2=None, notes=None,secondphone=None,id=None):
        self.fname=fname
        self.mname=mname
        self.lname=lname
        self.nname=nname
        self.title=title
        self.compname=compname
        self.address=address
        self.hphone=hphone
        self.mphone=mphone
        self.wphone=wphone
        self.faxnumber=faxnumber
        self.e_mail=e_mail
        self.e_mail2=e_mail2
        self.e_mail3=e_mail3
        self.home_page=home_page
        self.birth_year=birth_year
        self.address_2=address_2
        self.notes=notes
        self.secondphone=secondphone
        self.id=id

    def __repr__(self):
        return "%s:%s:%s" % (self.id, self.fname, self.lname)

    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id) and self.fname == other.fname and self.lname == other.lname

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize

