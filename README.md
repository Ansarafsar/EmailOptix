# EmailOptix
Skyrocketing Clicks with Smart Targeting

## 🚀 Project Overview

**EmailOptix** is a data science pipeline that optimizes email marketing campaigns by targeting users likely to click, replacing random sends with precision. Built for a case study with 100,000 email records (CTR ~2.12%), it delivers:
- **Open/CTR Analysis**: Computed open rate (~10.35%) and CTR (~2.12%).
- **Predictive Model**: Random Forest model to predict click probabilities, achieving ~40–90% CTR lift.
- **Segmentation**: Identified high-CTR segments (e.g., loyal buyers with 6–10 purchases, US/UK, morning sends).
- **Deployment**: Streamlit app and scoring pipeline for real-time targeting.
- **Monitoring**: Plan to track CTR and retrain the model monthly.

This project showcases end-to-end data science skills: data merging, EDA, feature engineering, modeling, evaluation, segmentation, deployment, and professional communication via PowerPoint slides.

---

## 📊 Problem Statement

Given a dataset of 100,000 email campaign records, the goal was to:
1. Calculate open and click-through rates.
2. Build a model to replace random email sends with targeted ones.
3. Estimate CTR lift and propose an A/B test.
4. Identify high-CTR user segments for personalized campaigns.

The dataset was imbalanced (CTR ~2.12%, max click probability ~0.0294), testing the ability to handle messy data and deliver actionable insights.

---

---

## 💻 Installation

Clone the repo and set up the environment:

```bash
git clone https://github.com/your-username/EmailOptix.git
cd EmailOptix
pip install pandas numpy scikit-learn matplotlib seaborn streamlit pyngrok joblib
```

