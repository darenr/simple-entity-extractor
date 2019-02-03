#!/usr/bin/env python
# -*- coding: utf-8 -*--


import unittest
import codecs
from entity_extractor import EntityExtractor

class TestEntityExtractor(unittest.TestCase):

    def test_1(self):

        with codecs.open('test_documents/text_document1.txt', 'rb', 'utf-8') as f:
            result = EntityExtractor().extract_entities(f.read())

            self.assertTrue(u'Robert Adams' in result['PERSON'])
            self.assertTrue(u'Alfred Stieglitz' in result['PERSON'])
            self.assertTrue(u'Claude Cahun' in result['PERSON'])
            self.assertTrue(u'Hans Bellmer' in result['PERSON'])
            self.assertTrue(u'Edward Weston' in result['PERSON'])
            self.assertTrue(u'William Eggleston' in result['PERSON'])
            self.assertTrue(u'Lewis Baltz' in result['PERSON'])
            self.assertTrue(u'Diane Arbus' in result['PERSON'])
            self.assertTrue(u'Larry Sultan' in result['PERSON'])
            self.assertTrue(u'Charles Sheeler' in result['PERSON'])
            self.assertTrue(u'Rineke Dijkstra' in result['PERSON'])
            self.assertTrue(u'Man Ray' in result['PERSON'])

    def test_news(self):
        with codecs.open('test_documents/text_document2.txt', 'rb', 'utf-8') as f:
            result = EntityExtractor().extract_entities(f.read())

            self.assertTrue(u'Donald Trump' in result['PERSON'])
            self.assertTrue(u'Brian France' in result['PERSON'])
            self.assertTrue(u'Howard Lorber' in result['PERSON'])
            self.assertTrue(u'Hillary Clinton' in result['PERSON'])

    def test_url1(self):
        result = EntityExtractor().extract_entities_from_url('https://en.wikipedia.org/wiki/Todd_Hido')

        self.assertTrue(u'Todd Hido' in result['PERSON'])
        self.assertTrue(u'Alec Soth' in result['PERSON'])
        self.assertTrue(u'David Campany' in result['PERSON'])
        self.assertTrue(u'Stephen Shore' in result['PERSON'])
        self.assertTrue(u'Nan Goldin' in result['PERSON'])
        self.assertTrue(u'Rineke Dijkstra' in result['PERSON'])
        self.assertTrue(u'Larry Sultan' in result['PERSON'])


if __name__ == '__main__':
    unittest.main()
