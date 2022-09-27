

def convert_etherscan_date(date):
    date_list = [*date]
    start = date_list.index('(') + 1
    end = date_list.index('M')
    new_list = date_list[start:end]
    space = new_list.index(" ")
    date = ""
    for i in new_list[0:space]:
        date += str(i)

    time_list = new_list[(space + 1):len(new_list)]
    if 'P' in date_list:
        time_list[0] = str(int(time_list[0]) + 1)
        time_list[1] = str(int(time_list[1]) + 2)

    time = ""

    for i in time_list:
        time += str(i)

    return date,time

def convert_etherscan_price(price):
    price_list = [*price]
    EtherLoc = price_list.index('E') - 1
    eth_price = ""
    for i in price_list[0:EtherLoc]:
        eth_price += str(i)

    dollar_loc1 = price_list.index('(') + 2
    dollar_loc2 = price_list.index(')')

    dollar_price = ""

    for i in price_list[dollar_loc1:dollar_loc2]:
        dollar_price += str(i)

    return eth_price,dollar_price


def convert_etherscan_id(tokenID):
    tokenID_list = [*tokenID]
    token_loc1 = tokenID_list.index('[') + 1
    token_loc2 = tokenID_list.index(']')

    token_ID = ""
    for i in tokenID_list[token_loc1:token_loc2]:
        token_ID += str(i)

    return token_ID
