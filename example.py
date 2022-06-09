from pnmatcher import PhoneNumberMatcher
matcher = PhoneNumberMatcher()
url_string = 'http://www.paducahwomensclinic.com/Obstetrics/Obstetrics.html1909898878'
url_phone_numbers = matcher.match(url_string, source_type='url')
print(url_phone_numbers)

text_string = 'this is my number 1 seven zero 1 one eight five five two one'
text_phone_numbers = matcher.match(text_string, source_type='text')
print(text_phone_numbers)
# []





