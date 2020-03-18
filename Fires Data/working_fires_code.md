# Dependencies
from matplotlib import pyplot as plt
from scipy import stats
import numpy as np
import pandas as pd

csvreader = pd.read_csv("fire_data.csv")
#csvreader.info()

#converting dates to Gegorian format 
csvreader["DISCOVERY_DATE"] = pd.to_datetime(csvreader['DISCOVERY_DATE'] - pd.Timestamp(0).to_julian_date(), unit='D')
csvreader["CONT_DATE"] = pd.to_datetime(csvreader['CONT_DATE'] - pd.Timestamp(0).to_julian_date(), unit='D')
csvreader["LENGTH_OF_BURN"] = csvreader["CONT_DATE"] - csvreader["DISCOVERY_DATE"]


working_data_f = csvreader.loc[csvreader["FIRE_SIZE_CLASS"] == "F"]
working_data_g = csvreader.loc[csvreader["FIRE_SIZE_CLASS"] == "G"]

working_data_full = working_data_f.append(working_data_g)



