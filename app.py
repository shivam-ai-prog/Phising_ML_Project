import streamlit as st
import pickle
import joblib
import pandas as pd

# ---------------------------
# Load your trained model
# ---------------------------
model_path = "phising_model.pkl"
model = joblib.load(model_path)

st.title("🔒 Phishing Website Detection")
st.write("Enter a website feature set (or URL features) and check if it's **Phishing** or **Safe**.")

# ---------------------------
# Example: if your model expects numeric features
# You can adjust this according to your dataset
# ---------------------------

# For demo: assuming model expects features like: ['having_IP_Address','URL_Length','Shortining_Service']
# Replace this with your actual features!
feature1 = st.number_input("having_IP_Address (1 = Yes, -1 = No)", min_value=-1, max_value=1, value=0)
feature2 = st.number_input("URL_Length (1 = Long, 0 = Normal, -1 = Short)", min_value=-1, max_value=1, value=0)
feature3 = st.number_input("Shortining_Service (1 = Yes, -1 = No)", min_value=-1, max_value=1, value=0)
feature4 = st.number_input("having_At_Symbol (1 = Yes, -1 = No)", min_value=-1, max_value=1, value=0)
feature5 = st.number_input("double_slash_redirecting (1 = Yes, -1 = No)", min_value=-1, max_value=1, value=0)
feature6 = st.number_input("Prefix_Suffix	 (1 = Yes, -1 = No)", min_value=-1, max_value=1, value=0)
feature7 = st.number_input("having_Sub_Domain (1 = Yes, -1 = No)", min_value=-1, max_value=1, value=0)
feature8 = st.number_input("SSLfinal_State (1 = Yes, -1 = No)", min_value=-1, max_value=1, value=0)
feature9 = st.number_input("Domain_registeration_length (1 = Yes, -1 = No)", min_value=-1, max_value=1, value=0)
feature10 = st.number_input("Favicon (1 = Yes, -1 = No)", min_value=-1, max_value=1, value=0)
feature11 = st.number_input("port (1 = Yes, -1 = No)", min_value=-1, max_value=1, value=0)
feature12 = st.number_input("HTTPS_token (1 = Yes, -1 = No)", min_value=-1, max_value=1, value=0)
feature13 = st.number_input("Request_URL (1 = Yes, -1 = No)", min_value=-1, max_value=1, value=0)
feature14 = st.number_input("URL_of_Anchor (1 = Yes, -1 = No)", min_value=-1, max_value=1, value=0)
feature15 = st.number_input("Links_in_tags (1 = Yes, -1 = No)", min_value=-1, max_value=1, value=0)
feature16 = st.number_input("SFH (1 = Yes, -1 = No)", min_value=-1, max_value=1, value=0)
feature17 = st.number_input("Submitting_to_email (1 = Yes, -1 = No)", min_value=-1, max_value=1, value=0)
feature18 = st.number_input("Abnormal_URL (1 = Yes, -1 = No)", min_value=-1, max_value=1, value=0)
feature19 = st.number_input("Redirect (1 = Yes, -1 = No)", min_value=-1, max_value=1, value=0)
feature20 = st.number_input("on_mouseover (1 = Yes, -1 = No)", min_value=-1, max_value=1, value=0)
feature21 = st.number_input("RightClick (1 = Yes, -1 = No)", min_value=-1, max_value=1, value=0)
feature22 = st.number_input("popUpWidnow (1 = Yes, -1 = No)", min_value=-1, max_value=1, value=0)
feature23 = st.number_input("Iframe (1 = Yes, -1 = No)", min_value=-1, max_value=1, value=0)
feature24 = st.number_input("age_of_domain (1 = Yes, -1 = No)", min_value=-1, max_value=1, value=0)
feature25 = st.number_input("DNSRecord (1 = Yes, -1 = No)", min_value=-1, max_value=1, value=0)
feature26 = st.number_input("web_traffic (1 = Yes, -1 = No)", min_value=-1, max_value=1, value=0)
feature27 = st.number_input("Page_Rank  (1 = Yes, -1 = No)", min_value=-1, max_value=1, value=0)
feature28 = st.number_input("Google_Index (1 = Yes, -1 = No)", min_value=-1, max_value=1, value=0)
feature29 = st.number_input("Links_pointing_to_page (1 = Yes, -1 = No)", min_value=-1, max_value=1, value=0)
feature30 = st.number_input("Statistical_report (1 = Yes, -1 = No)", min_value=-1, max_value=1, value=0)



if st.button("🔍 Predict"):
    # Create dataframe with user input
    input_data = pd.DataFrame([[feature1, feature2, feature3,feature4,feature5,feature6,feature7,feature8,feature9,feature10,feature11,feature12,feature13,feature14,feature15,feature16,feature17,feature18,feature19,feature20,feature21,feature22,feature23,feature24,feature25,feature26,feature27,feature28,feature29,feature30]],
                              columns=["having_IP_Address", "URL_Length", "Shortining_Service","having_At_Symbol","double_slash_redirecting","Prefix_Suffix","having_Sub_Domain","SSLfinal_State","Domain_registeration_length","Favicon","port","HTTPS_token","Request_URL","URL_of_Anchor","Links_in_tags","SFH","Submitting_to_email","Abnormal_URL","Redirect","on_mouseover","RightClick","popUpWidnow","Iframe","age_of_domain","DNSRecord","web_traffic","Page_Rank","Google_Index","Links_pointing_to_page","Statistical_report"])
    
    # Make prediction
    prediction = model.predict(input_data)[0]
    
    # Show result
    if prediction == 1:
        st.success("✅ The website is Safe!")
    else:
        st.error("⚠️ Warning: The website is Phishing!")
