#!/usr/bin/env python
# -*- coding: utf-8 -*--


import unittest
from name_extractor import extract_names

class TestNameExtractor(unittest.TestCase):

    def test_1(self):
        txt = u'''
        Today the photography collection numbers more than 17,000 objects, and is the largest collection
        at the museum. Its strengths include outstanding examples of work by West Coast modernist masters
        such as Ansel Adams, Edward Weston and their counterparts on the East Coast, most notably Alfred
        Stieglitz and Charles Sheeler. A small but important group of European modernist works by Hans
        Bellmer, Claude Cahun, Laszlo Moholy-Nagy and Man Ray, among others, represents another highlight
        of this period. The collection also demonstrates a deep commitment to the work of major 20th-
        and 21st-century figures, including Robert Adams, Diane Arbus, Lewis Baltz, Rineke Dijkstra,
        William Eggleston and Larry Sultan.
        '''

        result = extract_names(txt)

        self.assertTrue(u'Robert Adams' in result)
        self.assertTrue(u'Alfred Stieglitz' in result)
        self.assertTrue(u'Claude Cahun' in result)
        self.assertTrue(u'Hans Bellmer' in result)
        self.assertTrue(u'Edward Weston' in result)
        self.assertTrue(u'William Eggleston' in result)
        self.assertTrue(u'Lewis Baltz' in result)
        self.assertTrue(u'Diane Arbus' in result)
        self.assertTrue(u'Larry Sultan' in result)
        self.assertTrue(u'Charles Sheeler' in result)
        self.assertTrue(u'Rineke Dijkstra' in result)
        self.assertTrue(u'Man Ray' in result)

if __name__ == '__main__':
    unittest.main()
