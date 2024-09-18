featureVecs, labels = [], []
for i in range(2000): #それぞれの繰り返しで、４つの標本を作る
    featureVecs.append([random.gauss(0, 0.5), random.gauss(0,0.5), random.random()])
    labels.append('A')
    featureVecs.append([random.gauss(2, 0.5), random.gauss(2,0.5), random.random()])
    labels.append('D')
model = sklearn.linear_model.LogisticRegression().fit(featureVecs, labels)
print('model classes_ =', model.classes_)
print('[0, 0] probs =', model.predict_proba([[0, 0, 1]])[0])
print('[0, 2] probs =', model.predict_proba([[0, 2, 2]])[0])
print('[2, 0] probs =', model.predict_proba([[2, 0, 3]])[0])
print('[2, 2] probs =', model.predict_proba([[2, 2, 4]])[0])
