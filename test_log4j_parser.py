#!/usr/bin/env python
import log4j_parser
import unittest

class TestApacheLogParser(unittest.TestCase):
    def setUp(self):
        pass

    def testCombineExample2(self):
        # test the combined example from apache.org
        combined_log_entry="2010-10-13 18:02:30   INFO [main] (FrameworkServlet.java:277) - FrameworkServlet 'SpringMVC': initialization started"
        self.assertEqual(log4j_parser.dictify_logline(combined_log_entry),{'date':'2010-10-13','time':'18:02:30','level':'INFO'})

if __name__=="__main__":
    unittest.main()
