from Main.contract_class import *
from Main.transaction_class import *

import pandas as pd
import matplotlib.pyplot as plt 
from math import *


def txn_database(contract_address,page_factor):
    contract1 = contract(contractaddress=contract_address)
    contract1.get_transactions(page_factor=page_factor)
    contract1.quit()

    txns1 = txns(contract1.txn_ids)
    txns1.quit()

    data = {'TxnID':txns1.newIDs,'Eth Value':txns1.values_eth,'$ Value':txns1.values_dollar,'Date':txns1.dates,'Time':txns1.times,'TokenID':txns1.tokenIDs}

    dataframe = pd.DataFrame(data=data)

    return dataframe


def write_excel(name,pand_dataframe):
    datatoexcel = pd.ExcelWriter(f"{name}.xlsx",'xlsxwriter')
    pand_dataframe.to_excel(datatoexcel,sheet_name="Sheet1")
    datatoexcel.save()



def normal_distribution(x,sdev,mean):
    y = []
    for i in x:
        y_i = (1/(sdev*sqrt(2*pi)))*exp((-1/2)*((i-mean)/sdev)**2)
        y.append(y_i)

    
    plt.plot(x,y,'x')
    plt.show()
