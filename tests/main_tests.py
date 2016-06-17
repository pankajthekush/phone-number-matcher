
import sys
import time
import os
import unittest

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
TEST_DATA_DIR = os.path.join(os.path.dirname(__file__), 'data')

docs_ = os.path.expanduser(os.path.join(TEST_DATA_DIR, 'docs.json'))
docs_extraction_ = os.path.expanduser(os.path.join(TEST_DATA_DIR, 'docs_extraction.jsonl'))
text_ = os.path.expanduser(os.path.join(TEST_DATA_DIR, 'test.txt'))
url_ = os.path.expanduser(os.path.join(TEST_DATA_DIR, 'url.txt'))

import re
import json
from pnmatcher import PhoneNumberMatcher
import yaml
from jsoncompare import jsoncompare

class TestMainMethods(unittest.TestCase):
    def setUp(self):
        self.matcher = PhoneNumberMatcher()
        

    def tearDown(self):
        pass

    def test_extractor(self):
        # {"url": "", "title": "", "body": "", "url_ext_gt": [], "text_ext_gt": []}

        def load_jsonlines(raw):
            json_obj = json.loads(raw)
            return json_obj['jsonlines']

        input_fh = open(docs_, 'rb')
        lines = input_fh.readlines()
        # output_fh = open(docs_+'.phm', 'wb')
        
        json_obj = json.loads(''.join(lines))
        jsonlines = json_obj['jsonlines']

        total = 0           # total number of tests
        correct = 0         # total corrent number of tests
        missing = 0         # total number of tests that missing some extractions (no missing means that program get all extraction shown in groundtruth)
        error = 0           # total number of tests that get extra error extractions (no error means that there are no any extra extractions that shown in groundtruth)
        
        for jsonline in jsonlines:
            # json_obj = json.loads(jsonline)
            json_obj = jsonline
            
            is_correct = True
            is_error = False
            is_missing = False
            # error_ext = []
            # missing_ext = []

            url = json_obj['url']
            title = json_obj['title']
            body = json_obj['body']
            url_ext_groudtruth = json_obj['url_ext_gt']
            text_ext_groudtruth = json_obj['text_ext_gt']

            url_ext_expect = self.matcher.match(url, source_type='url').split()
            text_ext_expect = self.matcher.match(' '.join([title, body]), source_type='text').split()


            if len(url_ext_expect) < len(url_ext_groudtruth) or len(text_ext_expect) < len(text_ext_groudtruth) or len(url_ext_expect) > len(url_ext_groudtruth) or len(text_ext_expect) > len(text_ext_groudtruth):
                is_correct = False

            json_obj.setdefault('url_error', [])
            json_obj.setdefault('url_missing', [])
            json_obj.setdefault('text_error', [])
            json_obj.setdefault('text_missing', [])

            ## url
            # check if error
            for tee in url_ext_expect:
                if tee not in url_ext_groudtruth:
                    json_obj['url_error'].append(tee)
                    is_correct = False
                    is_error = True
            # check if missing
            for ueg in url_ext_groudtruth:
                if ueg not in url_ext_expect:
                    json_obj['url_missing'].append(ueg)
                    is_correct = False
                    is_missing = True

            ## text
            # check if error
            for tee in text_ext_expect:
                if tee not in text_ext_groudtruth:
                    json_obj['text_error'].append(tee)
                    is_correct = False
                    is_error = True
            # check if missing
            for ueg in text_ext_groudtruth:
                if ueg not in text_ext_expect:
                    json_obj['text_missing'].append(ueg)
                    is_correct = False
                    is_missing = True

            if is_error:
                error += 1
            if is_missing:
                missing += 1
            if is_correct:
                correct += 1
            else:
                json_obj['url_ext_ep'] = url_ext_expect
                json_obj['text_ext_ep'] = text_ext_expect

                print json.dumps(json_obj, sort_keys=True, indent=4, separators=(',', ': '))

            total += 1
        
        print 60*'-'
        print 'pass', correct, 'out of', total, 'tests', missing, 'missing,', error, 'error'

        input_fh.close()
        # output_fh.close()

    def test_text_extractor_file(self):

        output_fh = open(text_+'.phm', 'wb')
        with open(text_, 'rb') as f:
            for content in f:
                content = self.matcher.match(content, source_type='text')
                if content:
                    output_fh.write(str(content))
                output_fh.write('\n')
                # break
        output_fh.close()

    def test_text_extractor_string(self):
        content = "I'm very upscale and discreet. All of my services are unrushed and satisfying. I'm available all nite so don't hesitate to contact me. Please contact me when you're ready to be seen. Couples welcomed 7 0 8 - 8 8 0 - 9 2 9 6 708 Eight Eight Zero 9296?? Holly ?? 708 Eight Eight Zero 9296??"
        content = self.matcher.match(content, source_type='text')
        print content
                

    def test_url_extractor_file(self):

        output_fh = open(url_+'.phm', 'wb')
        with open(url_, 'rb') as f:
            for content in f:
                content = self.matcher.match(content, source_type='url')
                if content:
                    output_fh.write(str(content))
                output_fh.write('\n')
                # break
        output_fh.close()

    def test_url_extractor_string(self):
        content = "http://chicago.backpage.com/FemaleEscorts/r-u-t-a-_your-blonde-_-o-b-s-e-s-s-i-o-n-_-23-23-23-23/30688875"
        content = self.matcher.match(content, source_type='url')
        print content


        # 09921488 433 0888866 5466

    

if __name__ == '__main__':
    # unittest.main()

    def run_main_test():
        suite = unittest.TestSuite()
        # suite.addTest(TestMainMethods("test_text_extractor_file"))
        # suite.addTest(TestMainMethods("test_text_extractor_string"))
        # suite.addTest(TestMainMethods("test_url_extractor_file"))
        # suite.addTest(TestMainMethods("test_url_extractor_string"))
        
        suite.addTest(TestMainMethods("test_extractor"))
        # 3.5s
        runner = unittest.TextTestRunner()
        runner.run(suite)

    run_main_test()



"""

input_fh = open(docs_, 'rb')
    output_fh = open(docs_+'.phm', 'wb')
    cmp_ = open(docs_extraction_, 'rb')

    total_amt = 0
    correct_amt = 0

    for content in input_fh:
        json_obj = json.loads(content)

        url = json_obj['url']
        title = json_obj['title']
        body = json_obj['body']

        url_extractions = self.matcher.match(url, source_type='url')
        text_extractions = self.matcher.match(' '.join([title, body]), source_type='text')
        
        test_extraction = {}
        test_extraction["url"] = url_extractions.split()
        test_extraction["text"] = text_extractions.split()

        true_extraction = cmp_.readline()
        true_extraction = yaml.safe_load(true_extraction)
        

        
        if jsoncompare.are_same(test_extraction, true_extraction, True)[0]:
            output_fh.write(json.dumps(test_extraction))
            correct_amt += 1
        else:
            test_obj = {}
            test_obj['content'] = content
            test_obj['extraction'] = test_extraction
            test_obj['groundtruth'] = true_extraction
            print json.dumps(test_obj, sort_keys=True, indent=4, separators=(',', ': '))

            output_fh.write(json.dumps(test_extraction) + ' != ' + json.dumps(true_extraction))
        output_fh.write('\n')

        total_amt += 1

    print 'running', total_amt, 'tests in total,', correct_amt, 'are correct'

    input_fh.close()
    output_fh.close()
    cmp_.close()
"""

