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

# print('\nPurchase list ::', purchase_list)

"""
Create a purchase history report that computes the full purchase price (shares times dollars) for each block of stock and uses the stockDict to look up the full company name. This is the basic relational database join algorithm between two tables.

Example output for one block: I purchased General Electric stock for $4800
"""

def generate_single_stock_report():
    # This works because we are only looping through the values. For the desired value in the range of values, do [...]
    
    for stocks_tuple in purchase_list:
        # print(stocks_tuple)
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
                # print(full_company_name)
                print(f'I purchased {full_company_name} stock for {total_cost}')
                pass
                
            # print(x)
generate_single_stock_report()
    
    
    