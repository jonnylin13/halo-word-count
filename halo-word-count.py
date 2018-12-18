#!/usr/bin/env python

import re
import string
import collections

expected = ['the', 'and', 'to', 'of', 'i', 'you', 'a', 'my', 'hamlet', 'in']


def count_words():
    hamlet = open('hamlet.txt', 'r').read().lower()
    hamlet = hamlet.translate(string.punctuation)
    hamlet_count = collections.Counter(re.findall(r'\w+', hamlet)).most_common(10)
    return [x[0] for x in hamlet_count]

if __name__ == '__main__':
    print('Most Frequent Words...')
    answer = count_words()

    print('Answer: %s' % answer)    
    assert(answer == expected)
    print('SUCCESS!')
