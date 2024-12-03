# PCA 
Principal Component Analysis (PCA) is based on the eigen-decomposition of a covariance matrix.
To understand eigenvector and eigenvalue visually, please refer: https://setosa.io/ev/eigenvectors-and-eigenvalues/


Typically in unsupervised learning, a minor percentage of datapoints are assumed as outliers. **PCA** uses a cluster method to detect an anomaly, assumes
the inliers (normal datapoints) belong to large and dense clusters and the outliers/anomalies belong to either smaller and sparse clusters or none, in short PCA determines what constitutes
a normal class. 


Considering time-series data (refer to csv and py files of this repo) and assuming 1% outliers in the dataset, here's the result of PCA (anomalies are marked in red).
 
<img width="202" alt="mm" src="https://github.com/user-attachments/assets/a6f9baae-dfc6-4eef-a6e6-5f1b11da95a0">


Learn more about PCA from **Chapter 3** of **my book**: 

<img width="173" alt="mm" src="https://github.com/user-attachments/assets/a41c6d0d-de7b-4767-a4a0-488593c606f6">

Buy at Amazon: https://a.co/d/2JY2rdj


**In general, evaluating an unsupervised learning method is hard.** 

Yet, a few known metrics have been discussed here: https://ranjas.substack.com/p/exploring-metrics-in-unsupervised

**Apart from PCA, in matrix factorization problems we come across methods like Independent Component Analysis (ICA), and factor analysis**. An overview of all of them can be found at scikit-learn's page: 

https://scikit-learn.org/stable/modules/decomposition.html

Among other **anomaly detection methods in an unsupervised setting**, there is **Isolation Forest**:
<img width="316" alt="2" src="https://github.com/user-attachments/assets/fa7dfbe1-f99e-4dc6-985c-cbdc024d621a">

Another matrix decomposition linear algebraic method is SVD (singular value decomposition):
https://www.ams.org/publicoutreach/feature-column/fcarc-svd

An excellent blog on SVD: https://gregorygundersen.com/blog/2018/12/10/svd/



