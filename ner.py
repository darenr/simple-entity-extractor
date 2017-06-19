#!/usr/bin/env python
# -*- coding: utf-8 -*--

import re
import nltk
from collections import Counter
from nltk.corpus import stopwords

import sys
reload(sys)
sys.setdefaultencoding("utf-8")

stop = set(stopwords.words('english'))

def extract_names(document, min_name_length=2):

    def ie_preprocess(document):
        document = ' '.join([i for i in document.split()])
        sentences = nltk.sent_tokenize(document)
        sentences = [nltk.word_tokenize(sent) for sent in sentences]
        sentences = [nltk.pos_tag(sent) for sent in sentences]
        return sentences

    names = []
    sentences = ie_preprocess(document)
    for tagged_sentence in sentences:
        for chunk in nltk.ne_chunk(tagged_sentence):
            if type(chunk) == nltk.tree.Tree:
                if chunk.label() == 'PERSON':
                    names.append([c[0] for c in chunk])
    return Counter([' '.join(x) for x in  names if len(x) >= min_name_length and not any([word.lower() in stop for word in x])])

if __name__ == "__main__":


    txt = u'''Today the photography collection numbers more than 17,000 objects, and is the largest collection
    at the museum. Its strengths include outstanding examples of work by West Coast modernist masters
    such as Ansel Adams, Edward Weston and their counterparts on the East Coast, most notably Alfred
    Stieglitz and Charles Sheeler. A small but important group of European modernist works by Hans
    Bellmer, Claude Cahun, Laszlo Moholy-Nagy and Man Ray, among others, represents another highlight
    of this period. The collection also demonstrates a deep commitment to the work of major 20th-
    and 21st-century figures, including Robert Adams, Diane Arbus, Lewis Baltz, Rineke Dijkstra,
    William Eggleston and Larry Sultan.'''

    print extract_names(txt)
