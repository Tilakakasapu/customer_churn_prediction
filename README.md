
# **Customer Churn Prediction**

![Project Banner](https://user-images.githubusercontent.com/58620359/174948746-5dc3418a-8296-4cc8-9561-f8f12ca9a0a4.png))  


APP: https://churnpredic.streamlit.app/
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
