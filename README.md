

## Project Title  
**Predicting Prices of Daegu Apartment Using Price Prediction Tool**

---

## Background and Problem Statement  
Platform A, a South Korean real estate platform, allows users to list apartments for rent or sale. However, sellers often struggle to set competitive yet profitable prices due to the complexity of the real estate market. Factors such as apartment size, age, amenities, and proximity to transportation or schools significantly influence pricing. Without a systematic approach, sellers rely on intuition or incomplete information, leading to:  

1. **Overpriced Listings**: Apartments priced 10-20% above market value remain unsold for extended periods (e.g., 30+ days).  
2. **Underpriced Listings**: Apartments priced 10-15% below market value result in significant revenue loss for sellers.  

This tool aims to address these challenges by providing accurate price predictions using machine learning, empowering sellers to make informed pricing decisions.

---

## Stakeholders  
The primary stakeholders are **apartment owners in Daegu** who actively rent or sell their properties on Platform A. By using this tool, they can align their listings with market trends, improving their chances of selling or renting properties faster and at optimal prices.

---

## Goals  
The primary goal of this project is to:  
- Empower apartment owners to make **data-driven pricing decisions**.  
- Leverage **machine learning models** to analyze key factors (e.g., apartment size, age, amenities, location) and provide accurate price predictions.  
- Improve the efficiency of the housing market by reducing prolonged listing times and revenue losses.  

For **real estate agents or landlords**, this tool can attract more property listings, increase transactions, and boost Platform A’s revenue from booking and listing fees.

---

## Model Overview  

The best-performing model for this project is **Gradient Boosting with Sequential Forward Selection (SFS)**. Below is a summary of its performance:  

1. **R² = 81.17%**  
   - The model explains 81% of the variance in apartment prices, indicating strong predictive power.  

2. **RMSE = 46,248**  
   - On average, predictions deviate by approximately 46,248 Won from actual prices.  

3. **MAE = 36,959**  
   - The mean absolute error shows an average deviation of 36,959 Won.  

4. **MAPE = 18.27%**  
   - The model's predictions are, on average, 18% off from actual prices.  

---

## Business Interpretation  
The model performs well, offering a reliable tool for pricing apartments in Daegu. While the error margins are manageable, further improvements can enhance accuracy. By using this tool, sellers can:  
- Set competitive prices aligned with market trends.  
- Reduce listing times.  
- Maximize revenue by avoiding overpricing or underpricing.  

---
## Data 
Data is a collection of past listings of apartment around Daegu. Raw Data can be accessed through **data_daegu_apartment.csv**

---
## Limitations and Future Improvements  

### 1. Hyperparameter Tuning  
- The current model uses **Random Search** for hyperparameter optimization. Switching to advanced methods like **Grid Search** or **Bayesian Optimization** could improve performance.  

### 2. Feature Limitations  
- The model currently considers a limited set of features. Adding more features, such as proximity to parks, shopping centers, crime rates, or recent market trends, could improve accuracy.  

### 3. Data Quality and Quantity  
- The model's performance depends on the quality and quantity of training data. Collecting more recent and detailed data (e.g., transaction prices, property descriptions) could enhance predictions.  
- Addressing heteroscedasticity in the error distribution (e.g., using log transformations) could improve model robustness.  

### 4. Model Complexity  
- Gradient Boosting is computationally expensive. Exploring lighter algorithms like **LightGBM** or **XGBoost** could improve scalability and efficiency.  

---

## How to Use the Tool  

### App Access  
The tool is hosted on a Streamlit web app:  
[Daegu Apartment Price Prediction Tool](https://daegu-price-predict.streamlit.app/)  

### Requirements  
To run the app locally, ensure the following dependencies are installed:  
- `streamlit`  
- `pandas`  
- `scikit-learn==1.4.2`  

## Conclusion  
This tool provides a data-driven solution for apartment pricing on Platform A, helping sellers optimize their listings and improve profitability. While the current model performs well, addressing its limitations can further enhance its accuracy and usability, making it an even more valuable asset for stakeholders in the real estate market.
