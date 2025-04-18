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

## 💻 Installation

Clone the repo and set up the environment:

```bash
git clone https://github.com/your-username/EmailOptix.git
cd EmailOptix
pip install pandas numpy scikit-learn matplotlib seaborn streamlit pyngrok joblib
```
---
## Outputs:

- **Data**: data/output/ (e.g., targeted_users.csv, high_prob_users.csv).
- **Model**: models/click_prediction_model.pkl.
- **Visuals**: images/ (e.g., ctr_by_segment.png).
- **Text**: text/ (e.g., monitoring_plan.txt, slides.txt).

---

## 🔍 Key Features

- **Feature Engineering**: Binned user_past_purchases into purchase_bin (‘0’, ‘1-2’, ‘3-5’, ‘6-10’, ‘11+’) and hour into hour_bin (‘Night’, ‘Morning’, etc.) for robust modeling.
- **Model**: Random Forest with label-encoded categories, handling low probabilities (~0.0294) via a low threshold (0.02).
- **Deployment**: score_users pipeline generates targeted_users.csv for high-probability users, deployed via Streamlit.
- **Segmentation**: Identified high-CTR segments (e.g., 4–6% CTR for ‘6-10’ purchase users, US/UK, personalized emails).
- **Monitoring**: Plan to track CTR, detect feature drift, and retrain monthly.
---

## 📈 Results

- **Open Rate**: ~10.35% (Phase 2).
- **CTR**: ~2.12% baseline, ~3–4% for targeted users (Phase 4).
- **CTR Lit**: ~40–90% by targeting top users (Phase 4).
- **Segments**: Loyal buyers (‘6-10’, ‘11+’ purchases), US/UK, and morning sends drive high CTR (Phase 5).
- **Deliverables**: PowerPoint slides, Streamlit app, and monitoring plan for VP-level presentation.

---

## 🛠️ Challenges & Solutions

Low Probabilities (~0.0294): Adjusted threshold to 0.02 and used top 10% filtering to target users effectively.
Imbalanced Data: Leveraged Random Forest and focused on high-CTR segments to maximize lift.
Deployment: Used Ngrok for Streamlit access, with robust error handling in score_users.

---
## 📝 License

This project is licensed under the MIT License.

## 🙌 Acknowledgments

- Built as a case study to optimize email campaigns.
- Inspired by real-world marketing analytics challenges.
- **Tools**: Python, Pandas, Scikit-learn, Streamlit, Ngrok.

## 📫 Contact

Connect with me on LinkedIn or GitHub for collabs or inquiries!

Star this repo if you find it useful! 🌟
