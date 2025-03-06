import pandas as pd
import random
deliverNewDf = pd.read_csv(r"Data_transformator/Input/dummy_data.csv")
City = ["Tokyo", "Osaka", "Kyoto", "Sapporo", "Fukuoka", "Nagoya", "Kobe", "Yokohama"]
deliverNewDf['Age'] = [random.randint(19, 72) for _ in range(len(deliverNewDf))]
deliverNewDf['Cities'] = [random.choice(City) for _ in range(len(deliverNewDf))]
print(deliverNewDf)
deliverNewDf.to_csv(r"Data_transformator/Output/new_dummy_data.csv")