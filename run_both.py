from Functions.data_visulization import *
from set_variables import *
import numpy as np


dataframe = txn_database(Contract,Page_factor)
write_excel("IVY BOYS",dataframe)
price = np.array(dataframe['Eth Value'])
normal_distribution(price,price.std(),price.mean())
