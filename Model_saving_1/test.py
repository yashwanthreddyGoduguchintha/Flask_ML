import joblib
#load the model
model = joblib.load('../flask_api/joblib_model.pkl')
result =model.predict ([[1,243,33,422,873,232,1,6]])  #random  no's
print(result)