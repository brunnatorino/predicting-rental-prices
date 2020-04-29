## creating dummy variables for the categorical columns "rental agency" and "postcode"

dummies = pd.get_dummies(amsmodel1.postcode2,prefix=['p'])
amsmodel1 = pd.concat([amsmodel1,dummies],axis = 1)
dummies2 = pd.get_dummies(amsmodel1.rental_agency,prefix=['ag'])
amsmodel1 = pd.concat([amsmodel1,dummies2],axis = 1)

del amsmodel1['rental_agency']
del amsmodel1['postcode2']
del amsmodel1['postcode']

amsmodel1['house_price'] = pd.to_numeric(amsmodel1['house_price'])
amsmodel1 = amsmodel1.dropna()
len(amsmodel1.columns)
 
