import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
import pickle
data = pd.DataFrame({
    'cgpa':[6,7,8,9,5.5,6,8.5,9],
    'aptitude':[60,70,80,90,67,79,80,90],
    'communication':[5,6,7,8,9,9,8,7],
    'projects':[1,2,3,4,4,3,2,1],
    'placed':[0,1,0,1,1,1,0,1]
})
x =data[['cgpa','aptitude','communication','projects']]
y =data['placed']
model = LogisticRegression()
model.fit(x,y)
pickle.dump(model,open('model.pkl','wb'))
print("model trained and saved!!")