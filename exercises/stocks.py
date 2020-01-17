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
    
create_purchase_list('TGT', 100, '01-JAN-2020', 117)
create_purchase_list('TGT', 100, '01-MAR-2001', 98)
create_purchase_list('SQ', 100, '03-AUG-2003', 70)
create_purchase_list('V', 300, '13-MAY-2007', 43)
create_purchase_list('SDC', 200, '21-OCT-2006', 100)
create_purchase_list('PEP', 150, '11-FEB-2012', 119)
create_purchase_list('PEP', 100, '22-SEP-2015', 74)

# print('\nPurchase list ::', purchase_list)

"""
Create a purchase history report that computes the full purchase price (shares times dollars) for each block of stock and uses the stockDict to look up the full company name. This is the basic relational database join algorithm between two tables.

Example output for one block: I purchased General Electric stock for $4800
"""

def generate_single_stock_report():
    # This works because we are only looping through the values. For the desired value in the range of values, do [...]
    
    for stocks_tuple in purchase_list:
        num_of_shares = stocks_tuple[1]
        share_price = stocks_tuple[3]
        total_cost = num_of_shares * share_price
        total_cost = str(total_cost)
        # ticker = stocks_tuple[0]
        for ticker in stocks_dict:
            # print(stocks_dict[ticker])
            full_company_name = stocks_dict[ticker]
            full_company_name = str(full_company_name)
            x = ticker in stocks_tuple
            # print(x)
            if x:
                pass
                # print(full_company_name)
                # print(f'I purchased {full_company_name} stock for ${total_cost}')
                
            # print(x)
generate_single_stock_report()
    
"""
    Create a second purchase summary that which accumulates total investment by ticker symbol. In the above sample data, there are two blocks of GE. These can easily be combined by creating a dict where the key is the ticker and the value is the list of blocks purchased. The program makes one pass through the data to create the dict. A pass through the dict can then create a report showing each ticker symbol and all blocks of stock.

    Example output:

    ------ GE ------
    100 shares at 48 dollars each on 01-jul-1998
    200 shares at 56 dollars each on 10-sep-2001

    Total value of stock in portfolio: $16000
"""

def combine_reports_to_dict():
    combined_stocks = dict()

    for k in purchase_list:
        # print(purchase_list[:], '\n')
        key = k[0]
        vals = k[1:]
        # print('Keys =>', key)
        # print('Vals =>', vals, '\n')
        if key not in combined_stocks:
            combined_stocks[f'{key}'] = vals
        else:
            combined_stocks[f'{key}'] = purchase_list[:]
            pass
        print('\n', combined_stocks)
combine_reports_to_dict()