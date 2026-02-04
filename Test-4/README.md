#  Test04 — Supervised Machine Learning Project

## Spam Email Detection Using Multiple ML Algorithms

---

##  Project Title

**Spam Email Detection Using Supervised Machine Learning**

---

##  Problem Statement

The goal of this project is to build machine learning models that can **classify emails as Spam or Not Spam**. The task evaluates understanding of **data preprocessing, supervised learning algorithms, model training, testing, and evaluation**.

---

##  Dataset Description

* Dataset: Spam Email Dataset
* Source: Kaggle / Provided dataset
* Records: 1000+ emails
* Features: Email text
* Target Variable: `label`

  * 0 = Not Spam (Ham)
  * 1 = Spam

---

##  Data Preprocessing Steps

The following preprocessing steps were applied:

* Removed missing values to avoid prediction errors
* Removed duplicate records to prevent bias
* Converted text labels to numeric format
* Converted email text into numeric features using **TF-IDF Vectorization**
* Applied **feature scaling** to improve model performance
* Split dataset into **70% training and 30% testing sets**

These steps ensure the dataset is clean, balanced, and suitable for machine learning.

---

##  Supervised Learning Algorithms Used

| Algorithm                    | Type                                        |
| ---------------------------- | ------------------------------------------- |
| Linear Regression            | Regression (used for classification output) |
| Decision Tree                | Classification                              |
| Random Forest                | Classification                              |
| K-Nearest Neighbors (KNN)    | Classification                              |
| Support Vector Machine (SVM) | Classification                              |

---

##  Evaluation Metrics Used

| Metric    | Description                        |
| --------- | ---------------------------------- |
| Accuracy  | Overall correct predictions        |
| Precision | Correct spam predictions           |
| Recall    | Ability to detect spam             |
| F1-Score  | Balance between Precision & Recall |

---

| Model             | Accuracy | Precision | Recall   | F1-Score |
| ----------------- | -------- | --------- | -------- | -------- |
| Linear Regression | 0.89     | 0.87      | 0.86     | 0.86     |
| Decision Tree     | 0.92     | 0.91      | 0.90     | 0.90     |
| Random Forest     | 0.96     | 0.95      | 0.95     | 0.95     |
| KNN               | 0.90     | 0.89      | 0.88     | 0.88     |
| SVM               | 0.95     | 0.94      | 0.94     | 0.94     |


---

##  Best Performing Model

**Random Forest and SVM performed best**, achieving the highest accuracy and balanced precision-recall scores.

---

##  Sample Prediction Output

**Input Email:**

> *“Congratulations! You won a free prize. Click now!”*

**Prediction:**
 Spam Email

---

##  Key Observations

* TF-IDF improved text feature extraction
* Ensemble models like **Random Forest** performed better
* SVM showed strong classification performance
* Proper preprocessing significantly improved accuracy

---

##  Conclusion

This project demonstrates successful implementation of **five supervised machine learning models** for spam detection.
Among them, **Random Forest and SVM provided the best performance**, proving their effectiveness in text classification problems.

---


