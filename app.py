#import the libraries
import os


import math
import numpy as np
import pickle
import streamlit as st
import requests
import gdown 



#implementing ipl popup

#if "ipl_popup" not in st.session_state:
    #st.session_state.ipl_popup = True
#@st.dialog("🏏 Welcome to IPL 2026")
#def show_ipl_popup():

    #st.markdown("""
       # #<div style="text-align:center;">
           # <img src="" width="100%">
           # <h2 style="color:#ffcc00;">🔥 IPL Fever is ON 🔥</h2>
       # </div>
    #""", unsafe_allow_html=True)
    #st.markdown("""
       # <audio autoplay>
           # <source src="https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3" type="audio/mp3">
        #</audio>
   # """, unsafe_allow_html=True)

    
#if st.session_state.ipl_popup:
   # show_ipl_popup()


   
#SET PAGE WIDE
st.set_page_config(page_title=' T20 CRICKET SCORE PREDICTIOR',layout="centered")

#Get the ML model 

#filename='ml_model.pkl'
#model = pickle.load(open(filename,'rb'))


MODEL_URL = "https://drive.google.com/file/d/1010GY63W3yCfQyuY8bKnpWjGnm8iNnO9/view?usp=drive_link"
MODEL_PATH = "ml_model.pkl"

if not os.path.exists(MODEL_PATH):
    gdown.download(MODEL_URL, MODEL_PATH, quiet=False)

model = pickle.load(open(MODEL_PATH, 'rb'))

#Title of the page with CSS

st.markdown("<h1 style='text-align: center; color: white;'> circket Score Predictor </h1>", unsafe_allow_html=True)

#Add background image

st.markdown(
         f"""
         <style>
         .stApp {{
             background-image: url("https://t4.ftcdn.net/jpg/15/54/64/81/360_F_1554648111_UYkVgH9kET1hZScBtzVYYkWes21xHUU4.jpg");
             background-attachment: fixed;
             background-size: cover
         }}
         </style>
         """,
         unsafe_allow_html=True
     )
# ---- MENU ----
menu = st.sidebar.selectbox("⋮ Menu", 
                            ["Weather update", "Live Matches","About Developer","login","start beting"])
                            # ---- ABOUT DEVELOPER PAGE ----
if menu == "About Developer" :

    st.sidebar.title("About Developer")
    st.sidebar.image("https://i.postimg.cc/pd4y9rpY/Whats-App-Image-2026-03-23-at-05-27-26.jpg", width=150)
    st.sidebar.markdown("""
    ### Rahul Kumar  
    Department of Computer Application, NIT Trichy  
    MCA Session 2023-26  
    Machine Learning & Data Science Enthusiast  

    🔗 GitHub: https://github.com/PSF1234/circket_score_prediction7763953302  
    📧 Email: 205123078@NITT.EDU
    """)
    st.sidebar.markdown("""
---
<style>
[data-testid="stSidebar"] {
    position: relative;
                        }
.sidebar-footer {
    position: absolute;
    bottom: 10px;
    width: 100%;
    text-align: center;
    font-size: 13px;
    color: gray;
}
</style>

<div class="footer">
    © 2026 Rahul Kumar | All Rights Reserved <br>
    <a href="https://github.com/r7763953302-crypto" target="_blank">GitHub</a> |
    <a href="mailto:205123078@NITT.EDU">Email</a>
</div>
""", unsafe_allow_html=True)
    #adding login page 
# Session state for popup

if menu == "login":
    
    st.markdown("""
    <style>
    .insta-box{
        width:350px;
        margin:auto;
        padding:40px;
        border:1px solid #dbdbdb;
        background:white;
        text-align:center;
        border-radius:8px;
    }

    .insta-logo{
        font-size:40px;
        font-family:cursive;
        margin-bottom:20px;
    }

    .login-btn button{
        background:#0095f6 !important;
        color:white !important;
        font-weight:bold;
        width:100%;
        border-radius:6px;
    }
    </style>
    """, unsafe_allow_html=True)

    # popup dialog
    @st.dialog("Login")
    def show_login():

        #st.markdown('<div class="insta-box">', unsafe_allow_html=True)
        st.markdown('<div class="insta-logo">CRICKET SCORE PREDICTOR</div>', unsafe_allow_html=True)

        username = st.text_input("", placeholder="Phone number, username, or email")
        password = st.text_input("", type="password", placeholder="Password")

        if st.button("Log In"):
            if username == "205123078@nitt.edu" and password == "7763953302@RA":
                st.success("Login Successful ✅")
            else:
                st.error("Invalid Username or Password ❌")

        st.markdown(
        "<p style='font-size:14px;'>Don't have an account? <b>Sign up</b></p>",
        unsafe_allow_html=True
        )

        st.markdown('</div>', unsafe_allow_html=True)

    # Automatically open popup when login menu selected
    show_login()


  

# ---- LIVE MATCH PAGE ----s
if menu == "Live Matches":
    st.sidebar.title(" Live Cricket Matches")

    API_KEY = "4656050f-1a9b-4033-ac35-8ffa52784361"

    url = f"https://api.cricapi.com/v1/currentMatches?apikey={API_KEY}"
    #url = f"https://api.cricapi.com/v1/series_info?apikey={API_KEY}&offset=0&search=IPL"

    response = requests.get(url)
    data = response.json()

    if data["status"] == "success":
        for match in data["data"]:
            st.sidebar.subheader(match["name"])
            st.sidebar.write("Status:", match["status"])
            st.sidebar.write("Venue:", match["venue"])
            st.sidebar.write("-----------")
            
    else:
        st.sidebar.error("Unable to fetch live matches")

#adding weather update of city 
if menu == "Weather update":

    API_KEY = "eMP1CiJySiRNw4b5t3LLQ4bIovgai5mm"
    # Major Indian cities with coordinates
    cities = {
    "Delhi": (28.6139, 77.2090),
    "Mumbai": (19.0760, 72.8777),
    "Chennai": (13.0827, 80.2707),
    "Kolkata": (22.5726, 88.3639),
    "Bangalore": (12.9716, 77.5946),
    "Hyderabad": (17.3850, 78.4867),
    "Pune": (18.5204, 73.8567),
    "Ahmedabad": (23.0225, 72.5714),
    "Jaipur": (26.9124, 75.7873),
    "Lucknow": (26.8467, 80.9462),
    "Bhopal": (23.2599, 77.4126),
    "Patna": (25.5941, 85.1376),
    "Chandigarh": (30.7333, 76.7794),
    "Indore": (22.7196, 75.8577),
    "Surat": (21.1702, 72.8311),
    "Nagpur": (21.1458, 79.0882),
    "Visakhapatnam": (17.6868, 83.2185)
}
    # City dropdown
    city = st.sidebar.selectbox("Select City", list(cities.keys()))

    lat, lon = cities[city]
    # API call condition
#if city == "Delhi":
    #API_KEY = "eMP1CiJySiRNw4b5t3LLQ4bIovgai5mm"
    #url = f"https://dataservice.accuweather.com/locations/v1/cities/search?apikey={API_KEY}&q=Delhi"
    
    #response = requests.get(url)
    #data = response.json()
    
    #st.write(data)  # display resul


    # Flash message
    st.sidebar.warning("⚠️ We are working on weather service for cities. Please wait.")


    


    


    
    


#Add description

with st.expander("Description"):
    st.info("""A Simple ML Model to predict IPL Scores between teams in an ongoing match. To make sure the model results accurate score and some reliability the minimum no. of current overs considered is greater than 5 overs.
    
 """)

# SELECT THE BATTING TEAM


batting_team= st.selectbox('Select the Batting Team ',('Chennai Super Kings', 'Delhi capitals', 'Kings XI Punjab','Kolkata Knight Riders','Mumbai Indians','Rajasthan Royals','Royal Challengers Bangalore','Sunrisers Hyderabad' , 'India','australia','pakistan','afghanistan','canada','england','ireland','nepal','namibia','netherlands','new zealand','oman','srilanka','west indies'))

prediction_array = []
  # Batting Team
if batting_team == 'Chennai Super Kings':
    prediction_array = prediction_array + [1,0,0,0,0,0,0,0]
elif batting_team == 'Delhi capitals':
    prediction_array = prediction_array + [0,1,0,0,0,0,0,0]
elif batting_team == 'Kings XI Punjab':
    prediction_array = prediction_array + [0,0,1,0,0,0,0,0]
elif batting_team == 'Kolkata Knight Riders':
    prediction_array = prediction_array + [0,0,0,1,0,0,0,0]
elif batting_team == 'Mumbai Indians':
    prediction_array = prediction_array + [0,0,0,0,1,0,0,0]
elif batting_team == 'Rajasthan Royals':
    prediction_array = prediction_array + [0,0,0,0,0,1,0,0]
elif batting_team == 'Royal Challengers Bangalore':
    prediction_array = prediction_array + [0,0,0,0,0,0,1,0]
elif batting_team == 'Sunrisers Hyderabad':
    prediction_array = prediction_array + [0,0,0,0,0,0,0,1]
#adding new team for t20 world cup
elif batting_team == 'India':
    prediction_array = prediction_array + [0,1,0,0,0,0,0,0]
elif batting_team == 'austraila':
    prediction_array = prediction_array + [0,0,1,0,0,0,0,0]
elif batting_team == 'pakistan':
    prediction_array = prediction_array + [1,0,0,0,0,0,0,0] 
elif batting_team == 'afghanistan':
    prediction_array = prediction_array + [0,0,0,1,0,0,0,0] 
elif batting_team == 'canada':
    prediction_array = prediction_array + [0,0,0,0,0,0,1,0]  
elif batting_team == 'england':
    prediction_array = prediction_array + [1,0,0,0,0,0,0,0]
elif batting_team == 'ireland':
    prediction_array = prediction_array + [0,0,0,1,0,0,0,0]
elif batting_team == 'nepal':
    prediction_array = prediction_array + [0,0,0,1,0,0,0,0] 
elif batting_team == 'namibia':
    prediction_array = prediction_array + [0,0,1,0,0,0,0,0]  
elif batting_team == 'netherlands':
    prediction_array = prediction_array + [1,0,0,0,0,0,0,0]   
elif batting_team == 'new zealand':
    prediction_array = prediction_array + [0,0,0,0,0,1,0,0] 
elif batting_team == 'oman':
    prediction_array = prediction_array + [1,0,0,0,0,0,0,0] 
elif batting_team == 'srilanka':
    prediction_array = prediction_array + [0,0,0,0,0,0,1,0]   
elif batting_team == 'west indies':
    prediction_array = prediction_array + [0,0,0,1,0,0,0,0]   
                                        









#SELECT BOWLING TEAM

bowling_team = st.selectbox('Select the Bowling Team ',('Chennai Super Kings', 'Delhi capitals', 'Kings XI Punjab','Kolkata Knight Riders','Mumbai Indians','Rajasthan Royals','Royal Challengers Bangalore','Sunrisers Hyderabad', 'India','australia','pakistan','afghanistan','canada','england','ireland','nepal','namibia','netherlands','new zealand','oman','srilanka','west indies'))
if bowling_team==batting_team:
    st.error('Bowling and Batting teams should be different')
# Bowling Team
if bowling_team == 'Chennai Super Kings':
    prediction_array = prediction_array + [1,0,0,0,0,0,0,0]
elif bowling_team == 'Delhi capitals':
    prediction_array = prediction_array + [0,1,0,0,0,0,0,0]
elif bowling_team == 'Kings XI Punjab':
    prediction_array = prediction_array + [0,0,1,0,0,0,0,0]
elif bowling_team == 'Kolkata Knight Riders':
    prediction_array = prediction_array + [0,0,0,1,0,0,0,0]
elif bowling_team == 'Mumbai Indians':
    prediction_array = prediction_array + [0,0,0,0,1,0,0,0]
elif bowling_team == 'Rajasthan Royals':
    prediction_array = prediction_array + [0,0,0,0,0,1,0,0]
elif bowling_team == 'Royal Challengers Bangalore':
    prediction_array = prediction_array + [0,0,0,0,0,0,1,0]
elif bowling_team == 'Sunrisers Hyderabad':
    prediction_array = prediction_array + [0,0,0,0,0,0,0,1]
elif bowling_team == 'India':
    prediction_array = prediction_array + [0,1,0,0,0,0,0,0]
elif bowling_team == 'austraila':
    prediction_array = prediction_array + [0,0,1,0,0,0,0,0]
elif bowling_team == 'pakistan':
    prediction_array = prediction_array + [1,0,0,0,0,0,0,0] 
elif bowling_team == 'afghanistan':
    prediction_array = prediction_array + [0,0,0,1,0,0,0,0] 
elif bowling_team == 'canada':
    prediction_array = prediction_array + [0,0,0,0,0,0,1,0]  
elif bowling_team == 'england':
    prediction_array = prediction_array + [1,0,0,0,0,0,0,0]
elif bowling_team == 'ireland':
    prediction_array = prediction_array + [0,0,0,1,0,0,0,0]
elif bowling_team == 'nepal':
    prediction_array = prediction_array + [0,0,0,1,0,0,0,0] 
elif bowling_team == 'namibia':
    prediction_array = prediction_array + [0,0,1,0,0,0,0,0]  
elif bowling_team == 'netherlands':
    prediction_array = prediction_array + [1,0,0,0,0,0,0,0]   
elif bowling_team == 'new zealand':
    prediction_array = prediction_array + [0,0,0,0,0,1,0,0] 
elif bowling_team == 'oman':
    prediction_array = prediction_array + [1,0,0,0,0,0,0,0]  
elif bowling_team == 'srilanka':
    prediction_array = prediction_array + [0,0,1,0,0,0,0,0]  
elif batting_team == 'west indies':
    prediction_array = prediction_array + [0,0,0,1,0,0,0,0]                       
                                      
                      




  

col1, col2 = st.columns(2)



#Enter the Current Ongoing Over
with col1:
    overs = st.number_input('Enter the Current Over',min_value=5.1,max_value=19.5,value=5.1,step=0.1)
    if overs-math.floor(overs)>0.5:
        st.error('Please enter valid over input as one over only contains 6 balls')
with col2:
#Enter Current Run
    runs = st.number_input('Enter Current runs',min_value=0,max_value=354,step=1,format='%i')


#Wickets Taken till now
wickets =st.slider('Enter Wickets fallen till now',0,9)
wickets=int(wickets)

col3, col4 = st.columns(2)

with col3:
#Runs in last 5 over
    runs_in_prev_5 = st.number_input('Runs scored in the last 5 overs',min_value=0,max_value=runs,step=1,format='%i')

with col4:
#Wickets in last 5 over
    wickets_in_prev_5 = st.number_input('Wickets taken in the last 5 overs',min_value=0,max_value=wickets,step=1,format='%i')

#Get all the data for predicting

prediction_array = prediction_array + [runs, wickets, overs, runs_in_prev_5,wickets_in_prev_5]
prediction_array = np.array([prediction_array])
predict = model.predict(prediction_array)




if st.button('Predict Score'):
    #Call the ML Model
    my_prediction = int(round(predict[0]))

    

    
    #Display the predicted Score Range
    x=f'PREDICTED MATCH SCORE : {my_prediction-5} to {my_prediction+5}' 
    st.success(x)
   
