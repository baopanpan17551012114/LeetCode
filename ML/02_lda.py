# coding: utf-8
import numpy as np
from sklearn import datasets
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis

iris = datasets.load_iris()  # 直接从datasets 导出数据
X, y = iris.data, iris.target  # 切分数据集

# LDA降维（有类别，考虑样本标签）
lda = LinearDiscriminantAnalysis(n_components=2).fit(X, y)
data_lda = lda.transform(X)
print('LDA:', data_lda.shape)
# print(data_lda)

#
np.set_printoptions(precision=4)

mean_vectors = []
for cl in range(0, 3):
    mean_vectors.append(np.mean(X[y == cl], axis=0))
    print('Mean Vector class %s: %s\n' % (cl, mean_vectors[cl]))

#用代码实现上面的公式
S_W = np.zeros((4,4))
for cl, mv in zip(range(0,3), mean_vectors):
    class_sc_mat = np.zeros((4, 4))                  # scatter matrix for every class
    for row in X[y == cl]:
        row, mv = row.reshape(4, 1), mv.reshape(4, 1) # make column vectors
        class_sc_mat += (row-mv).dot((row-mv).T)
    S_W += class_sc_mat                             # sum class scatter matrices
print('within-class Scatter Matrix:\n', S_W)

overall_mean = np.mean(X, axis=0)

S_B = np.zeros((4, 4))
for i, mean_vec in enumerate(mean_vectors):
    i -= 1
    n = X[y == i+1,:].shape[0]
    mean_vec = mean_vec.reshape(4, 1)  # make column vector
    overall_mean = overall_mean.reshape(4, 1)  # make column vector
    S_B += n * (mean_vec - overall_mean).dot((mean_vec - overall_mean).T)

print('between-class Scatter Matrix:\n', S_B)

eig_vals, eig_vecs = np.linalg.eig(np.linalg.inv(S_W).dot(S_B))

for i in range(len(eig_vals)):
    eigvec_sc = eig_vecs[:, i].reshape(4, 1)
    print('\nEigenvector {}: \n{}'.format(i+1, eigvec_sc.real))
    print('Eigenvalue {:}: {:.2e}'.format(i+1, eig_vals[i].real))

#Make a list of (eigenvalue, eigenvector) tuples
eig_pairs = [(np.abs(eig_vals[i]), eig_vecs[:,i]) for i in range(len(eig_vals))]

# Sort the (eigenvalue, eigenvector) tuples from high to low
eig_pairs = sorted(eig_pairs, key=lambda k: k[0], reverse=True)

# Visually confirm that the list is correctly sorted by decreasing eigenvalues

print('Eigenvalues in decreasing order:\n')
for i in eig_pairs:
    print(i[0])

print('Variance explained:\n')
eigv_sum = sum(eig_vals)
for i,j in enumerate(eig_pairs):
    print('eigenvalue {0:}: {1:.2%}'.format(i+1, (j[0]/eigv_sum).real))

W = np.hstack((eig_pairs[0][1].reshape(4,1), eig_pairs[1][1].reshape(4,1)))
print('Matrix W:\n', W.real)

X_lda = X.dot(W)
assert X_lda.shape == (150,2), "The matrix is not 150x2 dimensional."















