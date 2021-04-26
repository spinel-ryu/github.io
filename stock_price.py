from bs4 import BeautifulSoup
from urllib import request
import datetime
from dataclasses import dataclass


@dataclass
class Ticker:
    code: str
    price: int
    time: datetime.datetime
    opening_price: int
    high_price: int
    low_price: int
    closing_price: int
    from_the_day_before: int
    from_the_day_before_percentage: float
    volume: int


class StockPrice:
    @staticmethod
    def get_ticker(code: str):
        url = 'https://kabutan.jp/stock/kabuka?code=' + code
        response = request.urlopen(url)
        soup = BeautifulSoup(response, 'html.parser')
        response.close()

        # 現在の株価と時刻は画面上部のstockinfo_i1から取得する
        div = soup.find('div', id='stockinfo_i1')
        span = div.find('span', class_='kabuka')
        time = div.find('time')

        # 時刻以外はstock_kabuka0クラスのテーブルから取得する
        table = soup.find('table', class_='stock_kabuka0')
        tbody = table.find('tbody')
        tds = tbody.find_all('td')
        if len(tds) != 7:
            raise RuntimeError('Unexpected HTML Structure.')

        price = int(span.text.replace(',', '').replace('円', ''))
        dt = datetime.datetime.fromisoformat(time.attrs['datetime'])
        opening_price = int(tds[0].text.replace(',', ''))
        high_price = int(tds[1].text.replace(',', ''))
        low_price = int(tds[2].text.replace(',', ''))
        closing_price = int(tds[3].text.replace(',', ''))
        from_the_day_before = int(tds[4].text.replace(',', '').replace('+', ''))
        from_the_day_before_percentage = float(tds[5].text.replace(',', '').replace('+', ''))
        volume = int(tds[6].text.replace(',', ''))

        daily_ticker = Ticker(code, price, dt, 
                                opening_price, high_price, low_price, closing_price, 
                                from_the_day_before, from_the_day_before_percentage, volume)
        return daily_ticker


if __name__ == '__main__':
#''の中に調べたい株価コード入れる
    print(StockPrice.get_ticker('2792'))