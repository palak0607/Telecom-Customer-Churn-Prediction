# Telecom-Customer-Churn-Prediction
Telecom Customer Churn Prediction uses machine learning to predict which customers are likely to leave a telecom service, helping companies retain them. It leverages Gradient Boosting algorithms and provides a user-friendly web interface for easy deployment.

Project Title Telecom Customer Churn Prediction
A brief description of what this project does and who it's for Telecom Customer Churn Prediction This project focuses on predicting customer churn in the telecom sector using machine learning techniques, specifically Gradient Boosting algorithms. Customer churn refers to the process where customers leave a service provider for a competitor, a significant issue in the highly competitive telecom industry. Predicting churn allows telecom companies to proactively take steps to retain customers, which is cost-effective compared to acquiring new customers.

Overview The goal of this project is to develop a churn prediction system using Python and machine learning, primarily leveraging Gradient Boosting algorithms due to their high predictive accuracy and ability to identify intricate patterns in large datasets. The system will provide telecom providers with valuable insights into customer behavior, allowing them to implement targeted retention strategies and reduce churn rates.
![Screenshot 2023-10-30 200618](https://github.com/user-attachments/assets/1374ff31-44bd-4c05-89ad-a7c485a3e169)
![Screenshot 2023-10-30 200625](https://github.com/user-attachments/assets/84795f48-1bdf-4649-bc4d-f1181ea3c73d)
![Screenshot 2023-10-30 200639](https://github.com/user-attachments/assets/ac7170b5-72a3-4bbd-9ea3-56a2027f1b21)
![Screenshot 2023-10-30 200711](https://github.com/user-attachments/assets/cd366a06-a9a3-4f03-8a6d-ebd7a5adbb39)
![Screenshot 2023-10-30 200734](https://github.com/user-attachments/assets/9edd4f14-2889-4e6d-9305-ded9971041af)



Motivation Reduce Costs: Retaining existing customers is cheaper than acquiring new ones. This project helps telecom companies reduce the costs associated with customer acquisition by identifying customers who are likely to churn and enabling early intervention. Data-Driven Decisions: Telecom companies gather large amounts of customer data. This project utilizes that data for predictive modeling to make informed decisions about customer retention strategies. Advanced Machine Learning: Gradient Boosting is a powerful algorithm known for its ability to deliver high predictive accuracy, making it well-suited for churn prediction. Key Features Churn Prediction Model: Utilizes Gradient Boosting for accurate customer churn prediction. Data Preprocessing: Handles missing data, encodes categorical variables, and scales numerical features. Model Evaluation: Compares different machine learning models, including Random Forest, Logistic Regression, and Decision Trees, to identify the best performer based on accuracy and F1 score. Deployment: A web interface has been developed using Streamlit and Uvicorn, making the system user-friendly for telecom operators. System Design Data Collection and Preprocessing:

Collects historical customer data, including billing information, call logs, demographic details, and service interactions. Data preprocessing involves handling missing values, feature scaling, and encoding categorical data. Model Development:

Gradient Boosting algorithm (e.g., XGBoost, CatBoost) is used to create a highly accurate predictive model. Other algorithms such as Logistic Regression, Decision Trees, and Random Forests are also compared for performance. Model Deployment:

The model is deployed as a web application using Streamlit for the frontend and Uvicorn for backend hosting. Results The Gradient Boosting model achieved the highest accuracy and F1 score, making it the best model for telecom churn prediction in this project. The system is capable of predicting which customers are most likely to churn, providing valuable insights for telecom companies to craft retention strategies. Future Enhancements Improved Model Interpretability: Implement SHAP and LIME techniques to enhance the interpretability of the model's predictions. Real-time Prediction: Extend the model to handle real-time data processing for instant churn prediction. Multi-Channel Data Integration: Incorporate data from social media interactions, customer feedback, and online reviews to enrich the predictive power of the model. Global Expansion: Adapt the model to work across different regions and customer behaviors globally. Prerequisites Python 3.x Libraries: pandas numpy scikit-learn XGBoost Streamlit Uvicorn pickle





