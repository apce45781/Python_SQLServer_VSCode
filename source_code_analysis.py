import bs4
class source_code_analysis:

    def __init__(self , source_code):
        self.source = bs4.BeautifulSoup(source_code , "html.parser")

    def getTitle(self):

        html_title = self.source.title.string

        title_name = html_title.split("(")
        title_ID = title_name[1].split(")")
        return [title_ID[0]] + [title_name[0]]

    def getBank(self):
        bank_sale = self.source.find("table" , width="100%" , border="0" , cellspacing="1" , cellpadding="3")
        count = 0
        bank = []
        for i in bank_sale:
            if i != "\n":      
                sell = []
                for j in i:
                    if j != "\n":
                        sell += j.text.split()
                bank += [sell]

        return bank

    def getTime(self):
        day_data = self.source.find("td" , width="180" , align="left" , class_="tt")
        day = ""
        for i in day_data.text:
            if i != "/" and i != "\n" and i != " ":
                day += i
        date = day.split("：")
        return int(date[1]) + 19110000