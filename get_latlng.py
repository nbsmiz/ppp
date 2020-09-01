import geocoder
import requests
import pandas as pd
import pickle
import geocoder as geo

loan_classes = ['catA', 'catB', 'catC', 'catD', 'catE']
print(loan_classes[0])

# read in loan class csv
def open_csv(lclass):
    lclass_df = pd.read_csv("data/loan_strip_catC.csv", index_col=0)
    return lclass_df

for loan_class in loan_classes[0]:
    print(loan_class)
    lclass_df = open_csv(loan_class)
    print(lclass_df.head())

# # construct full address
# c_addr['full_addr'] = c_addr.apply(lambda row: (row['Address'].split(',')[0] + ', ' 
#                             + row['City'] + ', ' + row['State']), axis=1)

# # use geocoder to grab latlngs
# with requests.Session() as session:
#     c_addr['latlng'] = c_addr.apply(lambda row: geo.osm(row['full_addr'], session=session).latlng, axis=1)

# # save latlng file
# pickle.dump(c_addr, open("static/c_addr.pkd", "wb"))