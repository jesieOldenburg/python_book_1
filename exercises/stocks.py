stocks_dict = dict()

def build_stock_dict(ticker_symbol, company_name):
    stocks_dict[f'{ticker_symbol}'] = f'{company_name}'
    
build_stock_dict('TGT', 'Target Corporation')
build_stock_dict('SQ', 'Square inc')
build_stock_dict('V', 'Visa inc')
build_stock_dict('SDC', 'SmileDirectClub')
build_stock_dict('PEP', 'PepsiCo Holdings')
# print(stocks_dict)

purchase_list = list()

def create_purchase_list(ticker, share, date, price):
    purch_list_item = tuple((ticker, share, date, price))
    purchase_list.append(purch_list_item)
    
create_purchase_list('TGT', 100, '01-JAN-2020', 117.00)
create_purchase_list('SQ', 100, '03-AUG-2003', 70.47)
create_purchase_list('V', 300, '13-MAY-2007', 43.92)
create_purchase_list('SDC', 200, '21-OCT-2006', 100.00)
create_purchase_list('PEP', 150, '11-FEB-2012', 119.00)

print(purchase_list)