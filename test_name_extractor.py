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

    def test_news(self):
        txt = u'''WASHINGTON — Democrats have long stoked suspicions about whether
        President Trump knew his son met with Russians offering dirt on Hillary
        Clinton during the 2016 campaign, pointing to phone calls that Donald Trump
        Jr. received from a blocked number around the time of the meeting.

        New evidence obtained by Senate investigators appears to have refuted that
        claim, according to two people briefed on the matter. The investigators have
        phone records showing that Donald Trump Jr. spoke with two family friends who
        used blocked numbers — Brian France, the chief executive of Nascar, and the
        investor Howard Lorber — as the meeting was being set up, according to the
        people.

        Mr. Lorber had significant investments in Russia and traveled to Moscow in
        1996 with President Trump as they considered building a Trump Tower there.

        For the younger Mr. Trump, the revelation that he had not called his father
        was seen among Trump allies as a victory over Democrats at a crucial moment
        in the investigation, according to people close to the White House.

        In a statement, the younger Mr. Trump said, “After a year of hearing about
        this one ad nauseam, yet another left-wing narrative officially bites
        the dust.”

        A Nascar spokesman did not respond to an email seeking comment, and attempts
        to reach Mr. Lorber were unsuccessful. CNN first reported that the Senate
        Intelligence Committee had obtained the new phone records.

        Donald Trump Jr. has testified privately that he could not recall who had
        used blocked numbers, and Democrats have long expressed incredulity that
        President Trump would not have been told that his son and top campaign
        advisers attended such a meeting, given that his aides have said he was
        often briefed on the inner workings of his campaign.'''

        result = extract_names(txt)
        print(result)

if __name__ == '__main__':
    unittest.main()
