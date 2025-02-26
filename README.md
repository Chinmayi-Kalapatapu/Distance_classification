# Distance_classification

#### 1. What are the common distance metrics used in distance-based classification algorithms? 

Euclidean Distance, Mahalanobis Distance, Manhattan Distance, Chebyshev Distance, Minkowski Distance, Cosine Distance, and Hamming Distance.

#### 2. What are some real-world applications of distance-based classification algorithms? 

Distance based classification algorithms are useful in feature classification problems. Some such applications are Customer Behaviour Prediction, Spam filtering, Face Recognition, Disease Classification, etc.
 
#### 3. Explain various distance metrics. 

a)Euclidean Distance finds the shortest distance between two vectors and is the most widely used metric. However, it doesn't account for the distribution of data.

b)Mahalanobis Distance finds the distance between a point and a distribution. It takes variance into consideration

c)Manhattan Distance measures the distance between two points measured along the axes at right angles.

d)Chebyshev Distance is defined on a vector space where the distance between two vectors is the greatest of their differences along any coordinate dimension.

e)Minkowski Distance: Distance measuring the distances between the points in space.

f)Cosine Distance is the degree of angle between two vectors. Used when the magnitude doesn't matter

g)Hamming Distance compares two strings/the number of positions. It measures the minimum number of subssets

#### 4. What is the role of cross validation in model performance? 

Cross validation is important as it prevents over-fitting. When the model is evaluated on multiple iterations of the validation set, it starts making more realistic predictions.

#### 5. Explain variance and bias in terms of KNN? 

Variance is a measure of how precise or how close the model's measurements are compared to the measurements taken from all of the previous testing. Bias is a measure of how far/inaccurate the model's measurements/outputs are compared to the actual measurements.

When k from KNN is too small, the model is more complex, there is a higher variance and an increased chance of overfitting risk. When k is too large, the model is simpler however there is a higher bias and underfitting risk.
