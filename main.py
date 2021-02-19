import Web_Page
import SQL_Server
import time

stock_array = (
"0050" , "0056"
)

def main():
    
    for stock in stock_array:  

        web = Web_Page.web_page(stock)
        source_code = web.catch_data()
        data = web.analysis(source_code)

        print(f"({data[0][0]}){data[0][1]}讀取中...")

        time.sleep(1)

        print("載入SQL Server中...")
        
        sql = SQL_Server.sql_server(data)
        sql.setData()
        sql.sql_close()
        

if __name__ == "__main__":
    main()