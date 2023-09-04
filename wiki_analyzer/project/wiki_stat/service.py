# this code fetch summary section of wikipedia pages

import wikipediaapi
from django.core.mail import EmailMessage


class SignificantWordCountException(Exception):
    # Raise an exception when the summary has more than 20% 5+ words
    pass


def summary_word_count(str):
    # Function which interpret the amount of 5+ letter words
    five_plus_word_count = 0
    list_s = str.split()
    word_count = len(list_s)
    for element in list_s:
        if len(element) >= 5:
            five_plus_word_count += 1
    quotient = five_plus_word_count/word_count
    return quotient


def fetch_from_wikipediaapi(input):
    # fetch the page from wikipediaapi
    wiki = wikipediaapi.Wikipedia('wiki_stats (jjj226417@gmail.com)', 'en')
    page = wiki.page(input)
    return page


def is_legit_title(str):
    # ban character that are not allowed in titles
    for char in '#><}[]|{':
        if char in str:
            return False
    return True


def alert(title, quotient):
    # I don't really understand why but need that first if
    if title != 'favicon.ico':
        # Create a message with relevent information and send it using send mail.
        message_content = "The article about " + title + \
            " was found to contain " + str(quotient) + "% of big words"
        message = EmailMessage("A dangerous article was found",
                               message_content,
                               to=['alexei.yadrin@isae-supmeca.fr'])
        message.send()
        return 0


class Result:
    # This class is used to create if possible the content that we will need later in the view
    # and make it more easier at the other end.
    def __init__(self,  input):
        try:
            if is_legit_title(input):
                self.is_legit = True
                self.title = input
                page = fetch_from_wikipediaapi(input)
                if page.exists():
                    self.summary = page.summary
                    self.quotient = summary_word_count(self.summary)
                    if self.quotient >= 0.2:
                        raise SignificantWordCountException
                else:
                    self.error_message = "Page not found."
            else:
                self.error_message = "Error: Key words cannot contain #><}[]|{"
        except SignificantWordCountException:
            if not alert(self.title, self.quotient):
                print("The mail could not be sent")
    # An error message will be sent to the user whenever needed. Other information might be used
    # as well.
    summary = ""
    is_legit = False
    error_message = "no error"
    quotient = 0
    title = ""


def is_legit_title(str):
    # ban character that are not allowed in titles
    illegal_char = '#><}[]|{'
    for char in illegal_char:
        if char in str:
            return False
    return True
