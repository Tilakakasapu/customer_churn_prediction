
# **Customer Churn Prediction**

![Project Banner](https://www.google.com/imgres?q=customer%20churn%20prediction&imgurl=https%3A%2F%2Fmiro.medium.com%2Fv2%2Fresize%3Afit%3A1024%2F1*WZdoYPpmiIk1AcPQ1YHWug.png&imgrefurl=https%3A%2F%2Fmedium.com%2F%40allanouko17%2Fcustomer-churn-prediction-using-machine-learning-ddf4cd7c9fd4&docid=RL5gGA3ZCS4hUM&tbnid=GN6cI864XgUVQM&vet=12ahUKEwjNw8r72--JAxUe4zgGHeg2NugQM3oECGQQAA..i&w=1024&h=366&hcb=2&ved=2ahUKEwjNw8r72--JAxUe4zgGHeg2NugQM3oECGQQAA)  

## **Project Description**  
This project predicts customer churn using a machine learning model. The model evaluates various customer attributes and predicts the likelihood of churn, helping businesses take proactive measures to retain their customers.  

The application is built using **Streamlit** for the user interface and **TensorFlow** for the machine learning model.  

---

## **Features**
- Predicts customer churn probability.
- Accepts user input for various customer attributes, such as:
  - **Geography**
  - **Gender**
  - **Age**
  - **Balance**
  - **Credit Score**
  - **Estimated Salary**
  - **Tenure**
  - **Number of Products**
  - **Has Credit Card** (binary)
  - **Is Active Member** (binary)
- Displays churn probability with actionable results (likely to churn or not).  

---

## **Technologies Used**
- **Python**  
- **TensorFlow**  
- **Streamlit**  
- **Pandas**  
- **Scikit-learn**  

---

## **Installation and Usage**

### **1. Clone the Repository**  
```bash
git clone https://github.com/Tilakakasapu/customer_churn_prediction.git
cd customer_churn_prediction
```

### **2. Install Dependencies**  
Use the `requirements.txt` file to install the required Python packages.  
```bash
pip install -r requirements.txt
```

### **3. Run the Application**  
```bash
streamlit run app.py
```

### **4. User Input**
- Open the Streamlit app in your browser (usually at `http://localhost:8501`).
- Input the required customer details in the form to get the churn prediction.

---

## **How It Works**
1. **Data Preprocessing**:  
   - Uses a **StandardScaler** to scale input features.
   - Encodes categorical features like **Geography** and **Gender** using pre-trained encoders (`LabelEncoder` and `OneHotEncoder`).

2. **Prediction**:  
   - A pre-trained **TensorFlow** model (`model.h5`) predicts churn probability based on input data.
   - Outputs a probability score and an actionable result (churn or not).

---

## **File Structure**
```
customer_churn_prediction/
├── app.py                 # Main Streamlit app
├── experiment.ipynb       # Jupyter Notebook for experiments
├── model.h5               # Pre-trained TensorFlow model
├── label_encoder_gender.pkl   # Gender label encoder
├── onehot_encoder_geo.pkl     # Geography one-hot encoder
├── scaler.pkl                 # Scaler for feature scaling
├── requirements.txt       # Python dependencies
```

---

## **Future Enhancements**
- Include visualizations for customer segmentation.
- Add support for batch predictions (e.g., uploading CSV files).
- Enhance the model for better performance and scalability.

---

## **License**
This project is licensed under the MIT License. See the LICENSE file for more details.
