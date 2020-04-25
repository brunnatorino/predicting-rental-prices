df2['lat2'] = 52.37890
df2['lon2'] = 4.9005805

import geopy.distance

df2['lat2'] = 52.370216
df2['lon2'] = 4.895168

df2['coord1'] = df2['latitude'].astype(str) + ',' + df2['longitude'].astype(str)
df2['coord2'] = df2['lat2'].astype(str) + ',' + df2['lon2'].astype(str)

def get_distance(coord1,coord2):
    dist = geopy.distance.vincenty(coord1, coord2).km
    return dist
df2['dist'] = [get_distance(**df2[['coord1','coord2']].iloc[i].to_dict()) for i in range(df2.shape[0])]

dummies = pd.get_dummies(df2.postcode2,prefix=['p'])
amsmodel1 = pd.concat([df2,dummies],axis = 1)
dummies2 = pd.get_dummies(df2.rental_agency,prefix=['ag'])
amsmodel1 = pd.concat([amsmodel1,dummies2],axis = 1)

del amsmodel1['postcode']
del amsmodel1['rental_agency']
del amsmodel1['latitude']
del amsmodel1['longitude']
del amsmodel1['postcode2']
del amsmodel1['lat2']
del amsmodel1['lon2']
del amsmodel1['coord1']
del amsmodel1['coord2']

amsmodel1['house_price'] = pd.to_numeric(amsmodel1['house_price'])
amsmodel1 = amsmodel1.dropna()
len(amsmodel1.columns)

 
