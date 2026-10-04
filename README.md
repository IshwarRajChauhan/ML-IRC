# ML-IRC

Machine Learning notes, definitions, and hands-on practice.

## Folder Plan

```
ML-IRC/
├── 1-sqlite/         # data storage basics
├── 2-logging/        # logging basics
├── 3-flask/          # serving basics
├── 4-ml-basics/      # definitions + notes
├── 5-supervised/     # regression, classification
├── 6-unsupervised/   # clustering, PCA
├── 7-evaluation/     # metrics, validation
└── 8-deployment/     # Flask/FastAPI model serving
```

## Core Definitions

| Term | Meaning |
|---|---|
| **Machine Learning** | Algorithms that learn patterns from data to make predictions without being explicitly programmed. |
| **Model** | The learned function mapping inputs to outputs. |
| **Feature** | An input variable used for prediction. |
| **Label / Target** | The output value the model tries to predict. |
| **Training set** | Data used to fit the model. |
| **Validation set** | Data used to tune hyperparameters. |
| **Test set** | Held-out data used for final evaluation. |
| **Parameter** | Value learned during training (weights, biases). |
| **Hyperparameter** | Value set before training (learning rate, depth). |
| **Loss function** | Measures how wrong the predictions are. |
| **Gradient descent** | Optimization method that updates parameters to reduce loss. |
| **Epoch** | One full pass over the training data. |

## Types of ML

- **Supervised**: learns from labeled data (regression, classification).
- **Unsupervised**: finds structure in unlabeled data (clustering, dimensionality reduction).
- **Semi-supervised**: mix of labeled and unlabeled data.
- **Reinforcement learning**: an agent learns by reward and penalty.

## Key Problems

- **Regression**: predict a continuous value (e.g., house price).
- **Classification**: predict a category (e.g., spam / not spam).
- **Clustering**: group similar items without labels.
- **Dimensionality reduction**: reduce the number of features (e.g., PCA).

## Common Algorithms

- Linear / Logistic Regression
- Decision Trees, Random Forest
- k-Nearest Neighbors (kNN)
- Support Vector Machine (SVM)
- Naive Bayes
- k-Means
- Gradient Boosting (XGBoost)
- Neural Networks

## Problems to Know

- **Overfitting**: model memorizes training data, performs poorly on new data.
- **Underfitting**: model is too simple to capture the pattern.
- **Bias-variance tradeoff**: balance between simplicity (bias) and sensitivity to data (variance).
- **Data leakage**: test information leaking into training.
- **Curse of dimensionality**: too many features make data sparse.

## Evaluation Metrics

- **Regression**: MAE, MSE, RMSE, R²
- **Classification**: Accuracy, Precision, Recall, F1, ROC-AUC, Confusion Matrix
- **Cross-validation**: k-fold splitting to estimate generalization.

## Typical Workflow

1. Define the problem
2. Collect and clean data
3. Feature engineering
4. Split data (train / val / test)
5. Train model
6. Evaluate and tune
7. Deploy and monitor

## Tech Stack

Python, NumPy, Pandas, Matplotlib, scikit-learn, Flask, SQLite

## Author

[IshwarRajChauhan](https://github.com/IshwarRajChauhan)
