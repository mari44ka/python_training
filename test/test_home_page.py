
import re


def test_home_page(app):
    contact_from_homepage = app.contact.get_contact_list()[0]
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(0)
    assert contact_from_homepage.all_phones_from_home_page == merge_phones_like_on_home_page(
        contact_from_edit_page)
    assert contact_from_homepage.fname==contact_from_edit_page.fname
    assert contact_from_homepage.lname == contact_from_edit_page.lname
    assert contact_from_homepage.address == contact_from_edit_page.address
    assert contact_from_homepage.all_emails_from_homepage == merge_emails_like_on_home_page(contact_from_edit_page)


def clear(s):
    return re.sub("[()-]"," ",s)




def merge_phones_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x !="",
                            map(lambda x: clear(x),filter(lambda x: x is not None,
                                                          [contact.hphone, contact.mphone, contact.wphone, contact.secondphone]))))


def merge_emails_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x !="",
                            map(lambda x: x,
                                filter(lambda x: x is not None,
                                       [contact.e_mail, contact.e_mail2, contact.e_mail3]))))

