# Fraud Detection via Machine Learning
## Goal

The goal of this project was to explore machine learning in a real-world setting by detecting fraudulent credit card transactions.

## Dataset & Challenges

The dataset was obtained from Kaggle. After initial ETL and exploratory data analysis, it became clear that the dataset is highly imbalanced — fraud cases are extremely rare. This imbalance presented a challenge for training a model that could reliably detect fraud.

## Approach

I started with logistic regression, but due to the class imbalance, the model mostly predicted transactions as “no fraud.” To address this, I applied SMOTE (Synthetic Minority Over-sampling Technique) and trained a Random Forest classifier.

## Results

The best model achieved a recall of 83% for detecting fraudulent transactions — meaning it correctly identifies 83% of actual fraud cases.

## How to Run

### Install dependencies:

pip install -r requirements.txt


### Run the main script:

python main.py


The script loads the trained model and outputs predictions for your dataset.

## Future Improvements

Experiment with model thresholds or probabilities to increase recall.

Explore additional ensemble methods or deep learning approaches.

Tailor model sensitivity to the operational system’s needs for real-time fraud detection.