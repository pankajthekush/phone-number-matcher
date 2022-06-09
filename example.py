from pnmatcher import PhoneNumberMatcher
matcher = PhoneNumberMatcher()
import json
#url_string = 'http://www.paducahwomensclinic.com/Obstetrics/Obstetrics.html'
#url_phone_numbers = matcher.match(url_string, source_type='url')
# []

#with open('/home/pankaj/Downloads/22994248.json','r') as f:
#    jdata = json.load(f)
#    vtext = jdata['url_visible_text']

text_string = 'this is my number 1 seven zero 1 one eight five five two one'
text_phone_numbers = matcher.match(text_string, source_type='text')
print(text_phone_numbers)
# []





