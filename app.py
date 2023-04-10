# Mengimpor library
import pandas as pd
import streamlit as st
import pickle

# Menghilangkan warning
import warnings
warnings.filterwarnings("ignore")

# Menulis judul
st.markdown("<h1 style='text-align: center; '> Loan Prediction </h1>", unsafe_allow_html=True)
st.markdown('---'*10)

# Load model
my_model = pickle.load(open('model_klasifikasi_loan.pkl', 'rb'))

# Pilihan utama

pilihan = st.selectbox('Apa yang ingin Anda lakukan?',['Prediksi dari file csv','Input Manual'])

if pilihan == 'Prediksi dari file csv':
    # Mengupload file
    upload_file = st.file_uploader('Pilih file csv', type='csv')
    if upload_file is not None:
        dataku = pd.read_csv(upload_file)
        st.write(dataku)
        st.success('File berhasil diupload')
        hasil = my_model.predict(dataku)
        #st.write('Prediksi',hasil)
        # Keputusan
        for i in range(len(hasil)):
            if hasil[i] == 1:
                st.write('Data pelanggan',dataku['Loan_ID'][i],'= Approved')
            else:
                st.write('Data pelanggan',dataku['Loan_ID'][i],'= Reject')
    else:
        st.error('File yang diupload kosong, silakan pilih file yang valid')
        #st.markdown('File yang diupload kosong, silakan pilih file yang valid')
else:
   # Baris Pertama
   with st.container():
       col1, col2, col3 = st.columns(3)
       with col1:
           loan_id = st.number_input('Loan_ID', value=1012)
       with col2:
           gender = st.selectbox('Gender',['Male','Female'])
       with col3:
           married = st.selectbox('Married',['Yes','No'])
           
   # Baris Kedua
   with st.container():
       col1, col2, col3 = st.columns(3)
       with col1:
           dependents = st.selectbox('Dependents',['0','1','2','>3'])
       with col2:
           education = st.selectbox('Education',['Graduate','Not Graduate'])
       with col3:
           self_employed = st.selectbox('Self_Employed',['Yes','No'])        
           
   # Baris Ketiga
   with st.container():
       col1, col2 = st.columns(2)
       with col1:
           app_inc = st.number_input('ApplicantIncome', value=2000)
       with col2:
           coapp_inc = st.number_input('CoapplicantIncome', value=1000)
       
   # Baris Keempat
   with st.container():
       col1, col2 = st.columns(2)
       with col1:
           loan_amount = st.number_input('LoanAmount', value=50)
       with col2:
           loan_amount_term = st.number_input('Loan_Amount_Term', value=360)

   # Baris Kelima
   with st.container():
       col1, col2 = st.columns(2)
       with col1:
           credit_history = st.selectbox('Credit_History',['0','1'])
       with col2:
           property_area = st.selectbox('Property_Area',['Semiurban','urban', 'Rural']) 

   # Inference
   data = {
           'Loan_ID': str('LP00')+ str(loan_id),
           'Gender': gender,
           'Married': married,
           'Dependents': dependents,
           'Education': education,
           'Self_Employed': self_employed,
           'ApplicantIncome': app_inc,
           'CoapplicantIncome': coapp_inc,
           'LoanAmount': loan_amount,
           'Loan_Amount_Term': loan_amount_term,
           'Credit_History': float(credit_history),
           'Property_Area': property_area        
           }

   # Tabel data
   kolom = list(data.keys())
   df = pd.DataFrame([data.values()], columns=kolom)
   
   # Melakukan prediksi
   hasil = my_model.predict(df)
   keputusan = ''
   if hasil == 0:
       keputusan = 'Reject!'
   else:
       keputusan = 'Approve!'

   # Memunculkan hasil di Web
   cust_num = 'LP00' 
   st.write('<center><b><h3>Customer Loan ID', cust_num+str(loan_id),'</b></h3>', unsafe_allow_html=True)
   st.write('<center><b><h3>Decision = ', keputusan,'</b></h3>', unsafe_allow_html=True)