import source_code_analysis
import urllib.request as req

class web_page:

    user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.146 Safari/537.36"
    url_head = "https://tw.stock.yahoo.com/d/s/major_"
    url_tail = ".html"

    def __init__(self , ID):
        self.ID = ID

    def catch_data(self):
        count = 0
        cookie = req.Request(self.url_head + self.ID + self.url_tail , headers = {"User-Agent" : self.user_agent})
        with req.urlopen(cookie) as url_data:
            source_code = url_data.read().decode("Big5")
        return source_code

    def analysis(self , source_code):
        sca = source_code_analysis.source_code_analysis(source_code)
        title = sca.getTitle()
        time = sca.getTime()
        bank_sale = sca.getBank()
  
        return [title] + [time] + [bank_sale]