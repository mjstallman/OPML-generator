import sys
import os
#from id3parse import ID3, ID3TextFrame


if len(sys.argv) < 2:
	print "usage python getTags.py filename.mp3"
	sys.exit()

#id3 = ID3.from_file(sys.argv[1])

#print id3

import id3reader

# Construct a reader from a file or filename.
id3r = id3reader.Reader(sys.argv[1])

# Ask the reader for ID3 values:

print 'album is \t' + str( id3r.getValue('album'))
print 'performer is \t' + str( id3r.getValue('performer'))
print 'title is \t' + str( id3r.getValue('title'))
print 'track is \t' + str( id3r.getValue('track'))
print 'year is \t' + str( id3r.getValue('year'))

print 'TT2 is    \t' + str(id3r.getValue('TT2'))
