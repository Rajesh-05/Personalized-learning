import streamlit as st
import pyrebase

# Firebase configuration
firebaseConfig = {
  "apiKey": " ",
  "authDomain": "personalized-learning-ff3dd.firebaseapp.com",
  "projectId": "personalized-learning-ff3dd",
  "databaseURL": "https://default.firebaseio.com",
  "storageBucket": "personalized-learning-ff3dd.appspot.com",
  "messagingSenderId": "74751939597",
  "appId": "1:74751939597:web:bc9de6ba0a5dbb5815f144",
  "measurementId": "G-2CXQRPPY4W"
};
# Initialize Firebase
firebase = pyrebase.initialize_app(firebaseConfig)
auth = firebase.auth()

# Streamlit page configurations
st.set_page_config(page_title="Personalized Learning Platform", layout="centered", initial_sidebar_state="collapsed")

# Define color scheme
COLOR_PRIMARY = "#0B3D91"  # Dark blue
COLOR_SECONDARY = "#FFFFFF"
COLOR_ACCENT = "#F39C12"  # Golden for buttons and accents

st.markdown(
    f"""
    <style>
    .stButton > button {{
        background-color: {COLOR_PRIMARY}; 
        color: {COLOR_SECONDARY};
        border-radius: 10px;
        padding: 10px 20px;
        border: none;
        font-size: 16px;
    }}
    .stButton > button:hover {{
        background-color: {COLOR_ACCENT};
        color: {COLOR_PRIMARY};
    }}
    body {{
        background-color: #f5f5f5;
    }}
    </style>
    """,
    unsafe_allow_html=True
)

# Firebase Authentication Functions
def login_user(email, password):
    try:
        user = auth.sign_in_with_email_and_password(email, password)
        return user
    except:
        st.error("Invalid email or password. Please try again.")
        return None

def signup_user(email, password, name, age, status):
    try:
        user = auth.create_user_with_email_and_password(email, password)
        st.success("Account created successfully! Please login.")
        return user
    except Exception as e:
        print(e)
        st.error(e.__context__)
        return None

# Function to display the login/signup form
def login_signup_form():
    st.title("Welcome to the Personalized Learning Platform")
    st.markdown(
        f"<h4 style='color:{COLOR_PRIMARY}; text-align: center;'>Learn in a way that fits YOU!</h4>", unsafe_allow_html=True
    )

    # Initialize session state for toggling between login and signup
    if "is_signup" not in st.session_state:
        st.session_state.is_signup = False

    if st.session_state.is_signup:
        st.markdown(f"<h3 style='color:{COLOR_PRIMARY};'>Sign Up</h3>", unsafe_allow_html=True)
        signup_name = st.text_input("Name", placeholder="Enter your full name")
        signup_age = st.number_input("Age", min_value=10, max_value=100, value=18)
        signup_status = st.selectbox("Current Academic Status", ["Student", "Professional", "Other"])
        signup_email = st.text_input("Email", placeholder="Enter your email", key="signup_email")
        signup_password = st.text_input("Password", placeholder="Enter your password", type="password", key="signup_password")
        
        if st.button("Sign Up"):
            if signup_name and signup_email and signup_password:
                user = signup_user(signup_email, signup_password, signup_name, signup_age, signup_status)
                if user:
                    st.success(f"Account created for {signup_email}. Please login!")
            else:
                st.warning("Please fill out all fields.")

        # Link to switch to Login
        if st.button("Already have an account? Login here"):
            st.session_state.is_signup = False
            st.experimental_rerun()  # Refresh the app

    else:
        st.markdown(f"<h3 style='color:{COLOR_PRIMARY};'>Login</h3>", unsafe_allow_html=True)
        login_email = st.text_input("Email", placeholder="Enter your email")
        login_password = st.text_input("Password", placeholder="Enter your password", type="password")

        if st.button("Login"):
            user = login_user(login_email, login_password)
            if user:
                st.success(f"Welcome back, {login_email}!")

        # Link to switch to Sign Up
        if st.button("New User? Sign up here"):
            st.session_state.is_signup = True
            st.experimental_rerun()  # Refresh the app

# Main app
def main():
    st.sidebar.image("https://your-logo-url.com", width=150)
    st.sidebar.title("Navigation")
    st.sidebar.markdown("Explore our features:")
    st.sidebar.markdown("- Personalized Learning")
    st.sidebar.markdown("- Track your progress")
    st.sidebar.markdown("- Adaptive Quizzes")

    login_signup_form()

if __name__ == "__main__":
    main()
