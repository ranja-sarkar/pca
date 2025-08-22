# PCA 
Principal Component Analysis (PCA) is based on the eigen-decomposition of a covariance matrix.
To understand eigenvector and eigenvalue visually, please refer: https://setosa.io/ev/eigenvectors-and-eigenvalues/

📌 PCA is the same as finding the principal moments of inertia (in Physics); just that we have a body made of data points instead of a body having a mass.  
Instead of finding the eigenvalues and eigenvectors of the inertia tensor, we find them by decomposing the covariance matrix.

📌 PCA is unsupervised. It detects the directions in which data varies the most.  

# Detecting anomaly by PCA

 **PCA** uses a cluster method to detect an anomaly. Typically in unsupervised learning, a minor percentage of datapoints are assumed as outliers. So PCA assumes the inliers belong to large and dense clusters and the outliers belong to either smaller and sparse clusters or none, in short **PCA determines what constitutes a normal class**. 

Considering time-series data and assuming 1% outliers in the dataset, here's the result of PCA (anomalies marked in red).
 
<img width="360" alt="11" src="https://github.com/user-attachments/assets/58072a54-7c01-46ee-8f74-b639f3e67ef9">

# PCA in my book

Considering the first two (extracted) principal components (PCs) namely, 0 and 1, the percentage of variance explained (PVE) for the dataset by them is as shown here:

<img width="377" alt="22" src="https://github.com/user-attachments/assets/3e1495ee-f06c-4b67-9afe-d7a8144231c8" />


Learn more about PCA from **Chapter 3** of **my book**: 

<img width="173" alt="mm" src="https://github.com/user-attachments/assets/a41c6d0d-de7b-4767-a4a0-488593c606f6">

Buy at Amazon: https://a.co/d/2JY2rdj


# LDA

Linear Discriminant Analysis is a supervised method to reduce dimensionality that projects the data onto a subspace in a way that maximizes the separability between classes/groups.

![lda](https://github.com/user-attachments/assets/e9764d7d-5098-40b8-84e8-125166d6b3a4)


# Other matrix-factorization methods

They are SVD, ICA, FA. 

Overview: https://scikit-learn.org/stable/modules/decomposition.html

# ICA

ICA is a technique used to separate mixed signals into their independent components by maximizing their statistical independence. It is widely used in signal processing, image analysis, and biomedical data analysis.  

📌 In PCA, principal components are orthogonal, in ICA independent components are not orthogonal. 

📌 PCA assumes data follows a Gaussian distribution, identifying orthogonal components, whereas ICA assumes a non-Gaussian distribution and does not constrain components to be orthogonal.

![1](https://github.com/user-attachments/assets/a0262fc4-8741-428c-92c9-149f27686670)


# SVD 

SVD (singular value decomposition): https://www.ams.org/publicoutreach/feature-column/fcarc-svd

An excellent blog on SVD: https://gregorygundersen.com/blog/2018/12/10/svd/


# FA

Factor analysis (FA) is used when we're interested in identifying underlying behavior and causes and in modelling relationships between observed and hidden (latent) variables. The latent constructs (with expectations) inferred from data are called factors. 


![2](https://github.com/user-attachments/assets/2776560d-8767-4c6d-8960-4460dc2485a5)

PCA works directly with observed variables, FA assumes that they are influenced by few hidden factors and typically employs techniques like MLE.
While PCs are often complicated to interpret, factors can be aligned with behavioral or theoretical ideas. 


