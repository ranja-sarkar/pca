
I have discussed the usefulness of PCA with regards to [proteins](https://ranja-sarkar.github.io/networks-graphs/). There are **other linear algebraic methods** useful in matrix-factorization problems which entail decomposition of signals into components. Understanding these methods from linear algebra becomes essential for data analysis and machine learning. They provide convenient ways to break a matrix, which perhaps contains some data we are interested in, into simpler and meaningful pieces of information.

**Chapter 3** of my book ["A handook of mathematical models with python"](https://ranja-sarkar.github.io/) is about the linear-algebraic method, principal component analysis ([PCA](https://gist.github.com/ranja-sarkar/3349477dcd8f2f46b4abc5b5c6a09496). 

# PCA

PCA reduces data dimensionality by projecting the data onto a subspace in a way that maximizes the variance. PCA works by decomposition of a covariance matrix. The matrix decomposition yields [eigenvectors and eigenvalues](https://setosa.io/ev/eigenvectors-and-eigenvalues/).

📌 PCA is the same as finding the principal moments of inertia (in Physics), just that we have a body made of data points instead of a body having a mass.  Instead of finding the eigenvalues and eigenvectors of the inertia tensor, we find them by decomposing the covariance matrix.

📌 PCA is an unsupervised method. It detects the directions in which data varies the most.  

📌 **Detecting anomaly by PCA**: It uses a cluster method to detect an anomaly. Typically in unsupervised learning, a minor percentage of datapoints are assumed as outliers. So PCA assumes the inliers belong to large and dense clusters and the outliers belong to either smaller and sparse clusters or none, in short **PCA determines what constitutes a normal class**. 

Considering time-series data and assuming 1% outliers in the dataset, here's the [result](https://github.com/ranja-sarkar/pca/blob/12b74a92ab3cf2c930290761b8e81ff9a7bbcf56/.github/workflows/code/pca.py) of PCA (anomalies marked in red).
 
<img width="360" alt="11" src="https://github.com/user-attachments/assets/58072a54-7c01-46ee-8f74-b639f3e67ef9">

Considering the first two principal components (PCs) namely, 0 and 1, the percentage of variance explained (PVE) for the dataset is as shown.

<img width="377" alt="22" src="https://github.com/user-attachments/assets/3e1495ee-f06c-4b67-9afe-d7a8144231c8" />

# LDA

Linear Discriminant Analysis (LDA) is a supervised method. It reduces data dimensionality by projecting the data onto a subspace in a way that maximizes the separability between classes/groups.

![lda](https://github.com/user-attachments/assets/e9764d7d-5098-40b8-84e8-125166d6b3a4)

[LDA](https://sebastianraschka.com/Articles/2014_python_lda.html) works well for data with multiple classes. However, it makes assumptions of normal distribution and equal class covariances.


# ICA

Independent component analysis (ICA) is a technique used to separate mixed signals into their independent components by maximizing their statistical independence. It is widely used in signal processing, image analysis, and biomedical data analysis.  

1. Principal components are orthogonal in PCA; independent components are not orthogonal in ICA. 

2. PCA assumes data follows a Gaussian distribution, identifying orthogonal components, whereas ICA assumes a non-Gaussian distribution and does not constrain components to be orthogonal.

![1](https://github.com/user-attachments/assets/a0262fc4-8741-428c-92c9-149f27686670)


# SVD 

SVD ([singular value decomposition](https://www.ams.org/publicoutreach/feature-column/fcarc-svd)) can be applied to any rectangular or square matrix, and is a more fundamental operation from which PCA can be derived. [SVD](https://gregorygundersen.com/blog/2018/12/10/svd/) directly works on the data matrix, unlike PCA. SVD is used to determine the rank of a matrix. 

<img width="146" height="128" alt="11" src="https://github.com/user-attachments/assets/a312421b-bdb3-4a20-9e8b-dec6aff50efa" />

<img width="148" height="70" alt="22" src="https://github.com/user-attachments/assets/aa1945a8-28da-427a-813a-13c9bb65c549" />

SVD is used to compress high-dimensional images by preserving only significant singular values. If some of the singular values are zero, the corresponding terms do not appear in the decomposition (linear transformation) of singular martix the rank of which is the dimension of the image. The dimension of the image is therefore equal to the number of non-zero singular values.

# FA

Factor analysis (FA) is used when we're interested in identifying underlying behavior and causes and in modelling relationships between observed and hidden (latent) variables. The latent constructs (with expectations) inferred from data are called factors. 

<img width="532" height="198" alt="pca" src="https://github.com/user-attachments/assets/b43f8191-a290-4d2c-8356-88a26bcb8817" />

[PCA and FA](https://www.theanalysisfactor.com/the-fundamental-difference-between-principal-component-analysis-and-factor-analysis/) are similar in what they do, yet different in how they do it. PCA works directly with observed variables, FA assumes that they are influenced by few hidden factors and typically employs techniques like MLE.

While PCs are often complicated to interpret, factors can be aligned with behavioral or theoretical ideas. 


