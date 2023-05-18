from mrjob.job import MRJob

class MRWordFrequencyCount(MRJob):

    def mapper(self, _, line):
        idemp,sector,salary,year = line.split(',')
        yield sector, int(salary)

    def reducer(self, sector, values):
        l = sum(values)
        yield sector, l

if __name__ == '__main__':
    MRWordFrequencyCount.run()