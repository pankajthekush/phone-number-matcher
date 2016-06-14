import re
import sys
import os
from string import maketrans

# sys.path.append(os.path.join(os.path.dirname(__file__), '..', '..', 'vendor'))
# import en
import re
class Cleaner():

    def __init__(self):
        pass

    def prep_misspelled_numeral_words(self, raw):
        raw = re.sub(r"th0usand", "thousand", raw, flags=re.I)
        raw = re.sub(r"th1rteen", "thirteen", raw, flags=re.I)
        raw = re.sub(r"f0urteen", "fourteen", raw, flags=re.I)
        raw = re.sub(r"e1ghteen", "eighteen", raw, flags=re.I)
        raw = re.sub(r"n1neteen", "nineteen", raw, flags=re.I)
        raw = re.sub(r"f1fteen", "fifteen", raw, flags=re.I)
        raw = re.sub(r"s1xteen", "sixteen", raw, flags=re.I)
        raw = re.sub(r"th1rty", "thirty", raw, flags=re.I)
        raw = re.sub(r"e1ghty", "eighty", raw, flags=re.I)
        raw = re.sub(r"n1nety", "ninety", raw, flags=re.I)
        raw = re.sub(r"fourty", "forty", raw, flags=re.I)
        raw = re.sub(r"f0urty", "forty", raw, flags=re.I)
        raw = re.sub(r"e1ght", "eight", raw, flags=re.I)
        raw = re.sub(r"f0rty", "forty", raw, flags=re.I)
        raw = re.sub(r"f1fty", "fifty", raw, flags=re.I)
        raw = re.sub(r"s1xty", "sixty", raw, flags=re.I)
        raw = re.sub(r"zer0", "zero", raw, flags=re.I)
        raw = re.sub(r"f0ur", "four", raw, flags=re.I)
        raw = re.sub(r"f1ve", "five", raw, flags=re.I)
        raw = re.sub(r"n1ne", "nine", raw, flags=re.I)
        raw = re.sub(r"0ne", "one", raw, flags=re.I)
        raw = re.sub(r"tw0", "two", raw, flags=re.I)
        raw = re.sub(r"s1x", "six", raw, flags=re.I)
        return raw

    def prep_replace_numeral_words(self, raw):
        raw = re.sub(r"hundred", "00", raw, flags=re.I)
        raw = re.sub(r"thousand", "000", raw, flags=re.I)

        raw = re.sub(r"eleven", "11", raw, flags=re.I)
        raw = re.sub(r"twelve", "12", raw, flags=re.I)
        raw = re.sub(r"thirteen", "13", raw, flags=re.I)
        raw = re.sub(r"fourteen", "14", raw, flags=re.I)
        raw = re.sub(r"fifteen", "15", raw, flags=re.I)
        raw = re.sub(r"sixteen", "16", raw, flags=re.I)
        raw = re.sub(r"seventeen", "17", raw, flags=re.I)
        raw = re.sub(r"eighteen", "18", raw, flags=re.I)
        raw = re.sub(r"nineteen", "19", raw, flags=re.I)
        
        raw = re.sub(r"zero", "0", raw, flags=re.I)
        raw = re.sub(r"one", "1", raw, flags=re.I)
        raw = re.sub(r"two", "2", raw, flags=re.I)
        raw = re.sub(r"three", "3", raw, flags=re.I)
        raw = re.sub(r"four", "4", raw, flags=re.I)
        raw = re.sub(r"five", "5", raw, flags=re.I)
        raw = re.sub(r"six", "6", raw, flags=re.I)
        raw = re.sub(r"seven", "7", raw, flags=re.I)
        raw = re.sub(r"eight", "8", raw, flags=re.I)
        raw = re.sub(r"nine", "9", raw, flags=re.I)
        raw = re.sub(r"(?<=[ilo0-9])ten", "10", raw, flags=re.I)

        raw = re.sub(r"(.*)(twenty[\\W_]{0,3})(\d)(.*)","\g<1>2\g<3>\g<4>", raw, flags=re.I)
        raw = re.sub(r"(.*)(thirty[\\W_]{0,3})(\d)(.*)","\g<1>3\g<3>\g<4>", raw, flags=re.I)
        raw = re.sub(r"(.*)(forty[\\W_]{0,3})(\d)(.*)","\g<1>4\g<3>\g<4>", raw, flags=re.I)
        raw = re.sub(r"(.*)(fifty[\\W_]{0,3})(\d)(.*)","\g<1>5\g<3>\g<4>", raw, flags=re.I)
        raw = re.sub(r"(.*)(sixty[\\W_]{0,3})(\d)(.*)","\g<1>6\g<3>\g<4>", raw, flags=re.I)
        raw = re.sub(r"(.*)(seventy[\\W_]{0,3})(\d)(.*)","\g<1>7\g<3>\g<4>", raw, flags=re.I)
        raw = re.sub(r"(.*)(eighty[\\W_]{0,3})(\d)(.*)","\g<1>8\g<3>\g<4>", raw, flags=re.I)
        raw = re.sub(r"(.*)(ninety[\\W_]{0,3})(\d)(.*)","\g<1>9\g<3>\g<4>", raw, flags=re.I)

        raw = re.sub(r"twenty", "20", raw, flags=re.I)
        raw = re.sub(r"thirty", "30", raw, flags=re.I)
        raw = re.sub(r"forty", "40", raw, flags=re.I)
        raw = re.sub(r"fifty", "50", raw, flags=re.I)
        raw = re.sub(r"sixty", "60", raw, flags=re.I)
        raw = re.sub(r"seventy", "70", raw, flags=re.I)
        raw = re.sub(r"eighty", "80", raw, flags=re.I)
        raw = re.sub(r"ninety", "90", raw, flags=re.I)

        # 26o  435  o72o
        # 2 six 9 eight 3 o 5 five 6 four
        # im at 6twentysix  4ohthree  o6oo call me
        raw = re.sub(r'((?:(?<=[0-9])(oh|o)+)|(?:(oh|o)+(?=[0-9]))|(?:(?<=\s)(oh|o)+(?=\s)))', '0', raw, flags=re.I)
        # raw = re.sub(r'(?:[a-z][0-9]+[a-z])', '', raw, flags=re.I)
        # raw = re.sub(r'[ _-]+(i|l)[ _-]+', ' 1 ', raw, flags=re.I)
        
        return raw

    def clean_digits(self, raw):
        REG = r'(.*)(\d+[(oils|oh)]+\d+)(.*)'
        if re.match(REG, raw):
            raw = re.sub(REG, '\g<1>\t\g<2>\t\g<3>', raw, re.I)
            raw = raw.split('\t')

            intab = "oils"
            outtab = "0115"
            trantab = maketrans(intab, outtab)
            raw[1] = raw[1].translate(trantab, 'h')
            raw = ''.join(raw)
        return raw


    def clean(self, raw):
        raw = self.prep_misspelled_numeral_words(raw)
        raw = self.prep_replace_numeral_words(raw)
        
        # raw = raw.split('\t')
        # for i in range(len(raw)):
        # raw = self.clean_digits(raw)
        # raw = '\t'.join(raw)
        
        # remove alphbets
        # raw = re.sub(r'[a-zA-Z]', '', raw)
        return raw.strip()

 

