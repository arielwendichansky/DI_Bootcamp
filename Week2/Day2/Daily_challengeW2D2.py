class Pagination:
    def __init__(self, items=None, pagesize=10):
        self.items = items or [] # Use the provided items or an empty list if None
        self.pagesize = int(pagesize)
        self.totalpages = (len(self.items) + self.pagesize-1) // self.pagesize # Calculate total pages
        self.currentpage = 1 # Current page can't be 0 so initiate with 1
        self.update_visible_items()

    def update_visible_items(self):
        start_index = (self.currentpage-1)*self.pagesize
        end_index = start_index + self.pagesize
        self.visible_items = self.items[start_index:end_index]
    def getvisibleitems(self):
        print(self.visible_items)

    def prevpage(self):
        if self.currentpage > 1:
            self.currentpage -= 1
            self.update_visible_items()
            print(self.currentpage)
        else:
            print("You are on the first page")
            print(self.currentpage)

    def nextpage(self):
        if self.currentpage < self.totalpages:
            self.currentpage += 1
            self.update_visible_items()
            print(self.currentpage)
        else:
            print("You are on the last page.")

    def firstpage(self):
        self.currentpage = 1
        self.update_visible_items()
        print(self.currentpage)

    def lastpage(self):
        self.currentpage = self.totalpages
        self.update_visible_items()
        print(self.currentpage)

    def gotopage(self, pagenum):
        if pagenum <= 0:
            self.currentpage = 1
        elif pagenum > self.totalpages:
            self.currentpage = self.totalpages
        else:
            self.currentpage = pagenum

        self.update_visible_items()
        print(self.currentpage)

alphabetList = list("abcdefghijklmnopqrstuvwxyz")
p = Pagination(alphabetList, 4)

p.gotopage(10)
p.getvisibleitems()
p.gotopage(1)
p.getvisibleitems()
