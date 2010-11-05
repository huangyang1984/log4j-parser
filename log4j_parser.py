#!/usr/bin/env python
"""
USAGE:
log4j_parser.py some_log_file
"""

import sys
import re
log_line_re=re.compile(r'''(?P<date>\S+) #Date
                            \s+ #whitespace
                            (?P<time>\S+) #time
                            \s+ #whitespace
                            (?P<level>\S+) #level
                            \s+ #whitespace
                            \S+ #thread
                            \s+ #whtespace
                            \S+ #src
                            \s+ #whitespace
                            -   #-
                            \s+ #whitespace
                            \s* #other
                            ''',re.VERBOSE)

def dictify_logline(line):
    '''return'''
    m=log_line_re.match(line)
    if m:
        groupdict=m.groupdict()
        return groupdict
    else:
        return {'date':None,
                'time':None,
                'level':None,
        }
def generate_log_report(logfile):
    '''return'''
    report_dict={}
    for line in logfile:
        line_dict=dictify_logline(line)
        print line_dict
        report_dict.setdefault(line_dict['level'],[])
    return report_dict

if __name__=="__main__":
    if not len(sys.argv)>1:
        print __doc__
        sys.exit(1)
    infile_name=sys.argv[1]
    try:
        infile=open(infile_name,'r')
    except IOError:
        print "You must specify a valid file to parse"
        print __doc__
        sys.exit(1)
        
    log_report=generate_log_report(infile)
    print log_report
    infile.close()
