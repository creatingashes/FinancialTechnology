from sklearn.datasets import load_iris
from sklearn.cluster import KMeans
import pandas as pd
import matplotlib.pyplot as plt

#import data
iris = load_iris()
names = pd.DataFrame(iris.data, columns=iris['feature_names'])
data = names[['sepal length (cm)', 'sepal width (cm)', 'petal length (cm)']]

#optimum number of clusters
sse = {}
for i in range(1, 10):
    kmeans = KMeans(n_clusters=i, max_iter=1000).fit(data)
    data["clusters"] = kmeans.labels_
    sse[i] = kmeans.inertia_

#plotting figure
fig = plt.figure()
plt.plot(list(sse.keys()), list(sse.values()))
plt.xlabel("Number of cluster")
plt.ylabel("SSE")
plt.show()
fig.savefig('KmeansElbow.jpeg')

#Help from https://stackoverflow.com/questions/19197715/scikit-learn-k-means-elbow-criterion
