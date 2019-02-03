#!/usr/bin/env python
# -*- coding: utf-8 -*--
from __future__ import print_function

import re
import nltk
import requests
import codecs
import json
from collections import Counter, defaultdict
from nltk.corpus import stopwords

import sys
reload(sys)
sys.setdefaultencoding("utf-8")

class EntityExtractor(object):

    def __init__(self):
        pass

    def _preprocess(self,  document):
        document = ' '.join([w for w in document.split()])
        sentences = nltk.sent_tokenize(document)
        sentences = [nltk.word_tokenize(sent) for sent in sentences]
        sentences = [nltk.pos_tag(sent) for sent in sentences]
        return sentences

    def extract_entities_from_url(self, url):
        return self.extract_entities(requests.get(url).text)

    def extract_entities(self, document):
        entities = defaultdict(list)
        sentences = self._preprocess(document)
        for tagged_sentence in sentences:
            for chunk in nltk.ne_chunk(tagged_sentence):
                if type(chunk) == nltk.tree.Tree:
                    if chunk.label() in ['PERSON', 'LOCATION', 'FACILITY', 'ORGANIZATION', 'GPE']:
                        entities[chunk.label()].append(' '.join([c[0] for c in chunk]))

        # convert each value in the defaultdict to a Counter type
        for k in entities:
            entities[k] = Counter(entities[k])
        return entities

if __name__ == "__main__":

    with codecs.open('test_documents/text_document1.txt', 'rb', 'utf-8') as f:
        result = EntityExtractor().extract_entities(f.read())
        print(json.dumps(result, indent=2, sort_keys=True))

    #print(EntityExtractor().extract_entities_from_url('https://en.wikipedia.org/wiki/Todd_Hido'))
