import sys
import time
import os
import unittest

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
TEST_DATA_DIR = os.path.join(os.path.dirname(__file__), 'data')

docs_ = os.path.expanduser(os.path.join(TEST_DATA_DIR, 'docs.jsonl'))
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
        # {"url": "", "title": "", "body": ""}

        input_fh = open(docs_, 'rb')
        output_fh = open(docs_+'.phm', 'wb')
        cmp_ = open(docs_extraction_, 'rb')

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
            # print test_extraction
            # print true_extraction

            output_fh.write(json.dumps(test_extraction))
            if not jsoncompare.are_same(test_extraction, true_extraction, True)[0]:
                output_fh.write(' != ' + json.dumps(true_extraction))
            output_fh.write('\n')


        input_fh.close()
        output_fh.close()
        cmp_.close()

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
        content = "MOMOCOCO SPA give you HIGHEST CARE! Tired? Stressed? Simply need to relax? Cute Asian Relaxation! BEST RELAXATION! BEST HOT ASIANS! BEST SERVICE! GUARANTEED! MASSAGES EXCELLENT RELAXING! NO RUSH! MOMOCOCO SPA ~ (click below for Maps Directions) #2 954-652-1555 #1 954-514-7158 MM32149"
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
        content = "http://346-804-3627.escortphonelist.com/incall-and-outcalls-come-check-me-out-4173798.html"
        content = self.matcher.match(content, source_type='url')
        print content


        # 09921488 433 0888866 5466

    

if __name__ == '__main__':
    # unittest.main()

    def run_main_test():
        suite = unittest.TestSuite()
        # suite.addTest(TestMainMethods("test_text_extractor_file"))
        suite.addTest(TestMainMethods("test_text_extractor_string"))
        # suite.addTest(TestMainMethods("test_url_extractor_file"))
        # suite.addTest(TestMainMethods("test_url_extractor_string"))
        
        # suite.addTest(TestMainMethods("test_extractor"))
        runner = unittest.TextTestRunner()
        runner.run(suite)

    run_main_test()



