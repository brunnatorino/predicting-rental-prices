dummies = pd.get_dummies(amsterdam.postcode2,prefix=['p'])
amsmodel1 = pd.concat([amsterdam,dummies],axis = 1)
dummies2 = pd.get_dummies(amsterdam.rental_agency,prefix=['ag'])
amsmodel1 = pd.concat([amsmodel1,dummies2],axis = 1)

amsmodel1['house_price'] = pd.to_numeric(amsmodel1['house_price'])
amsmodel1['bedrooms'] = pd.to_numeric(amsmodel1['bedrooms'])
amsmodel1['surface'] = pd.to_numeric(amsmodel1['surface'])

del amsmodel1['latitude']
del amsmodel1['longitude']

amsmodel1 = amsmodel1.dropna()
print(len(amsmodel1.columns))
