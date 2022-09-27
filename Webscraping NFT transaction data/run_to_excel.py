from Functions.data_visulization import *
from set_variables import *

dataframe = txn_database(Contract,Page_factor)

write_excel("IVY BOYS",dataframe)