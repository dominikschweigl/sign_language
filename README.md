# sign_language

## Protocoll

05.June:
image data set got more than doubled (classes, that had only 112 images in them got x5 (2 flipps and 3 rotations))

with 2 epochs:
around 5 min. training time
Validation Accuracy: 79.91%
Training Accuracy: 86.17%

with 5 epochs:
around 15 min. training time
Validation Accuracy: 88.53%
Training Accuracy: 95.78%

# SVM

Tried to do svm without feature extraction, but grid search was running more than 12 hours.
SVM does not work with high dimensional data.

Then used pca to get good feature extraction. Experimented with number of components.

Chose 500 components to get 95% of explained variance.
