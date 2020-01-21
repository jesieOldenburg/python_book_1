import datetime

class Building:
# instance attribute
    def __init__(self, address, stories):
        self.designer = 'Jesie'
        self.date_purchased = ''
        self.owner = ''
        self.address = address
        self.stories = stories

    def construct(self):
        self.date_purchased = datetime.datetime.now().date()
    
    def purchase(self, str):
        self.owner = str

stratford_way = Building('11041 Stratford Way', 2)
stratford_way.purchase('Billy Mays')
stratford_way.construct()
print(f'{stratford_way.address} was purchased by {stratford_way.owner} on {stratford_way.date_purchased} and has {stratford_way.stories} stories')

patriot_park_cir = Building('327 Patriot Park', 2)
patriot_park_cir.purchase('Reda Homebuilders')
patriot_park_cir.construct()
print(f'\n{patriot_park_cir.address} was purchased by {patriot_park_cir.owner} on {patriot_park_cir.date_purchased} and has {patriot_park_cir.stories} stories')

shannahan_drive = Building('1029 Shannahan Dr', 2)
shannahan_drive.purchase('Merrel Home Builders')
shannahan_drive.construct()
print(f'\n{shannahan_drive.address} was purchased by {shannahan_drive.owner} on {shannahan_drive.date_purchased} and has {shannahan_drive.stories} stories')

man_o_war = Building('1068 Man-O-War Blvd', 2)
man_o_war.purchase('Rick Flair')
man_o_war.construct()
print(f'\n{man_o_war.address} was purchased by {man_o_war.owner} on {man_o_war.date_purchased} and has {man_o_war.stories} stories')

good_hope_cemetary = Building('629 Good Hope Cemetary Rd', 3)
good_hope_cemetary.purchase('Macho Man Randy Savage')
good_hope_cemetary.construct()
print(f'\n{good_hope_cemetary.address} was purchased by {good_hope_cemetary.owner} on {good_hope_cemetary.date_purchased} and has {good_hope_cemetary.stories} stories')

class Bank:
    def __init__(self, name):
        self.bank_name = name
        self.customers = list()
        
class Customer:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        
usaa = Bank('USAA')
        
jesie = Customer('Jesie', 'Oldenburg')
tony = Customer('Tony', 'Hanson')

usaa.customers.append(jesie)
for customer in usaa.customers:
    pass
    print(f'{customer.first_name} {customer.last_name} is a customer of {usaa.bank_name}...')