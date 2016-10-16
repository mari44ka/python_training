import re


def test_home_page(app):
    contact_from_homepage = app.contact.get_contact_list()[0]
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(0)
    assert contact_from_homepage.hphone == clear(contact_from_edit_page.hphone)
    assert contact_from_homepage.mphone == clear(contact_from_edit_page.mphone)
    assert contact_from_homepage.wphone == clear(contact_from_edit_page.wphone)
    assert contact_from_homepage.secondphone == clear(contact_from_edit_page.secondphone)
    assert contact_from_homepage.fname==contact_from_edit_page.fname
    assert contact_from_homepage.lname == contact_from_edit_page.lname
    assert contact_from_homepage.address == contact_from_edit_page.address
    assert contact_from_homepage.e_mail==contact_from_edit_page.e_mail
    assert contact_from_homepage.e_mail3 == contact_from_edit_page.e_mail3
    assert contact_from_homepage.e_mail2 == contact_from_edit_page.e_mail2



def clear(s):
    return re.sub("[() -]","",s)
