import geopy.distance

df5['lat2'] = 52.370216
df5['lon2'] = 4.895168

df5['coord1'] = df5['latitude'].astype(str) + ',' + df5['longitude'].astype(str)
df5['coord2'] = df5['lat2'].astype(str) + ',' + df5['lon2'].astype(str)

def get_distance(coord1,coord2):
    dist = geopy.distance.vincenty(coord1, coord2).km
    return dist
df5['dist'] = [get_distance(**df5[['coord1','coord2']].iloc[i].to_dict()) for i in range(df5.shape[0])]

# deleting columns we don't need anymore

del df5['address']
del df5['address2']
del df5['altitude']
del df5['latitude']
del df5['longitude']
del df5['point']
del df5['lat2']
del df5['lon2']
del df5['coord1']
del df5['coord2']
del df5['location']
