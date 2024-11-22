
# **Customer Churn Prediction**

![Project Banner]data:image/png;base64,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)  

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
