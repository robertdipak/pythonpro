from sklearn.datasets import load_iris  
  
# Loading the dataset  
iris = load_iris()  
  
# Creating the dataframe of the dataset  
df = pd.DataFrame(iris.data, columns = iris.feature_names)  



# import numpy as np 
# from sklearn import preprocessing
# input_data=np.array([
#     [2.1, -1.9, 5.5],
#     [-1.5, 2.4, 3.5],
#     [0.5, -7.9, 5.6],
#     [5.9, 2.3, -5.8]]
# )

# data_binarized=preprocessing.Binarizer(threshold=0.5).transform(input_data)
# print("Mean = ", input_data.mean(axis=1))
# print("\nBinarized Data: \n ", data_binarized)




# from sklearn.datasets import load_iris
# iris = load_iris()
# x=iris.data
# y=iris.target

# from sklearn.model_selection import train_test_split

# X_train, X_test, y_train, y_test = train_test_split(
#     x,y,test_size=0.3, random_state=1

# )
# from sklearn.neighbors import KNeighborsClassifier
# from sklearn import metrics

# classifier_knn= KNeighborsClassifier(n_neighbors = 3)
# classifier_knn.fit(X_train, y_train)
# y_pred= classifier_knn.predict(X_test)
# print("Accuracy: ", metrics.accuracy_score(y_test, y_pred))
# sample = [[5,3,3,2],[2,4,3,5]]
# preds= classifier_knn.predict(sample)
# pred_species = [iris.target_names[p] for p in preds]
# print("Predictions: ", pred_species)





# from sklearn.datasets import load_iris
# iris = load_iris()
# x=iris.data
# y=iris.target

# from sklearn.model_selection import train_test_split

# X_train, X_test, y_train, y_test = train_test_split(
#     x,y,test_size=0.3, random_state=1

# )

# print(X_train.shape)
# print(X_test.shape)



# from sklearn.datasets import load_iris
# iris = load_iris()
# X = iris.data
# y = iris.target
# feature_names = iris.feature_names
# target_names = iris.target_names
# print(iris)
# print("Feature names:", feature_names)
# print("Target names:", target_names)
# print("File Names", iris.filename)
# print("\nFirst 10 rows of X:\n", X[:10])
# print("\nFirst 10 rows of Y:\n", y[:10])

