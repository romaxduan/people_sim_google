from gensim import corpora, models, similarities
import pickle
from optparse import OptionParser
import codecs

#TODO complete option parser
parser = OptionParser()
parser.add_option("-i","--input",dest="infilename",help="read corpus file",metavar="FILE")
(options, args) = parser.parse_args()
#TODO complete file reading


# Read in dictionary
dict_in_file = codecs.open("data/sg_words.lst",encoding="utf-8",mode="r")
dict_google = dict_in_file.read().split()
print len(dict_google)
dictionary = corpora.Dictionary([dict_google])

class MyCorpus(object):
	def __init__(self, filename):
		self.corpusfile = filename
		try:
			codecs.open(filename,encoding="utf-8",mode="r")
		except:
			print "Error opening corpus file!"
	def __iter__(self):
		for line in codecs.open(self.corpusfile,encoding="utf-8",mode="r"):
			yield dictionary.doc2bow(line.strip().split())

corpus_text = MyCorpus(options.infilename)
for vector in corpus_text:
	print vector
