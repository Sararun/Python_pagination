class Pagination:
    def __init__(self, items=None, pageSize=10):
        if items is None:
            items = []
        self.splitedContent = self.__chunk(items, int(pageSize))
        self.currentPage = 1
        self.totalPages = len(self.splitedContent)

    @staticmethod
    def __chunk(sequence, chunkSize):
        return [sequence[i:i + chunkSize] for i in range(0, len(sequence), chunkSize)]

    @staticmethod
    def __index0(index):
        return index - 1

    def getVisibleItems(self):
        return self.splitedContent[self.__index0(self.currentPage)]

    def prevPage(self):
        if self.currentPage - 1 >= 1:
            self.currentPage -= 1
        return self
        # raise ValueError

    def nextPage(self):
        if self.currentPage + 1 <= self.totalPages:
            self.currentPage += 1
        return self
        # raise ValueError

    def lastPage(self):
        self.currentPage = self.totalPages
        return self

    def firstPage(self):
        self.currentPage = 1
        return self

    def goToPage(self, page):
        if page < 1:
            self.currentPage = 1
        elif page > self.totalPages:
            self.currentPage = self.totalPages
        return self
