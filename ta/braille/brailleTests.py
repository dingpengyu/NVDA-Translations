#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import sys
import louis

testHarness = {
#vowel
u'இ': 'i',
#consonant:
u'ப': 'p',
#joined
u'பி': 'pi',

# letters with dots:
u'க்': '`k',

## standalone words:
# sri alone
u' ஸ்ரீ ': ' s ',
# sri part of a word
u'பஸ்ரீ': "p`sr9",

# dont know name:
u' க்ஷ ': ' q ',

## punctuation
# left quote
u'“': '6-236',
# right quote
u'”': '356-3',

#left single quote
u'‘': '236',
#right single quote
u'’': '356',
}

# note: if the test fails saying it cant find tables then:
# copy en-us-g1.ctb and chardefs.cti into this directory.
table = ['tamil.ctb']

for test in testHarness.keys():
    #test = test.decode('utf-8')
    braille = louis.translate(table, test, typeform=None)[0]
    if testHarness[test] == braille:
        print "ok"
    else:
        print "failed for %s: got '%s' expected '%s'" %(test, braille, testHarness[test])
