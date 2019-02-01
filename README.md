# simple-name-extractor

Uses NLTK to extract people's names from a document returning names and their
frequency of occurrence.

# install

```
pip install -r requirements.txt
```

# Example Usage:

```from name_extractor import extract_names

txt = u'''Today the photography collection numbers more than 17,000 objects, and is the largest
collection at the museum. Its strengths include outstanding examples of work by West Coast
modernist masters such as Ansel Adams, Edward Weston and their counterparts on the East Coast,
most notably Alfred Stieglitz and Charles Sheeler. A small but important group of European
modernist works by Hans Bellmer, Claude Cahun, Laszlo Moholy-Nagy and Man Ray, among others,
represents another highlight of this period. The collection also demonstrates a deep commitment
to the work of major 20th- and 21st-century figures, including Robert Adams, Diane Arbus,
Lewis Baltz, Rineke Dijkstra, William Eggleston and Larry Sultan.'''

extract_names(txt)

Counter({u'Robert Adams': 1,
         u'Alfred Stieglitz': 1,
         u'Claude Cahun': 1,
         u'Hans Bellmer': 1,
         u'Edward Weston': 1,
         u'William Eggleston': 1,
         u'Ansel Adams': 1,
         u'Lewis Baltz': 1,
         u'Diane Arbus': 1,
         u'Larry Sultan': 1,
         u'Charles Sheeler': 1,
         u'Rineke Dijkstra': 1,
         u'Man Ray': 1})

```

# Tests

```
nosetests
```
