# -*- coding: utf-8 -*-

import re

from collections import Counter

aList = ["Dog", "Cat", "Mouse", 42, "Dog", 42, "Cat", "Dog"]

a = Counter(aList)

print a

aSet = set(aList)

print len(aSet)

print "{0}:{1}".format(a.values(), a.keys())

print(a.most_common(3))

string = """   Lorem ipsum dolor sit amet, consectetur

adipiscing elit. Nunc ut elit id mi ultricies

adipiscing. Nulla facilisi. Praesent pulvinar,

sapien vel feugiat vestibulum, nulla dui pretium orci,

non ultricies elit lacus quis ante. Lorem ipsum dolor

sit amet, consectetur adipiscing elit. Aliquam

pretium ullamcorper urna quis iaculis. Etiam ac massa

sed turpis tempor luctus. Curabitur sed nibh eu elit

mollis congue. Praesent ipsum diam, consectetur vitae

ornare a, aliquam a nunc. In id magna pellentesque

tellus posuere adipiscing. Sed non mi metus, at lacinia

augue. Sed magna nisi, ornare in mollis in, mollis

sed nunc. Etiam at justo in leo congue mollis.

Nullam in neque eget metus hendrerit scelerisque

eu non enim. Ut malesuada lacus eu nulla bibendum

id euismod urna sodales.  """

words = re.findall(r'\w+', string)

print words

lower_word = [word.lower() for word in words]

print lower_word

wordCounter = Counter(lower_word)

print wordCounter

print wordCounter.most_common(1)
