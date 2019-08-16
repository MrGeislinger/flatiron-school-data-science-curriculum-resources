from mrjob.job import MRJob
import string

class MRWordFreqCount(MRJob):

    def mapper(self, _, line):
        line = line.strip()
        line = line.replace(string.punctuation, '')
        words = line.split()
        for word in words:
            yield (word.lower(), 1)

    def reducer(self, word, counts):
        yield (word, sum(counts))


if __name__ == '__main__':
    MRWordFreqCount.run()