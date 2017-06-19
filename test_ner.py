#!/usr/bin/env python
# -*- coding: utf-8 -*--

from ner import extract_names

def test_1():
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

    assert u'Robert Adams' in result
    assert u'Alfred Stieglitz' in result
    assert u'Claude Cahun' in result
    assert u'Hans Bellmer' in result
    assert u'Edward Weston' in result
    assert u'William Eggleston' in result
    assert u'Lewis Baltz' in result
    assert u'Diane Arbus' in result
    assert u'Larry Sultan' in result
    assert u'Charles Sheeler' in result
    assert u'Rineke Dijkstra' in result
    assert u'Man Ray' in result
