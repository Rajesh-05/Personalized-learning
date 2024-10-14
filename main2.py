import os
import streamlit as st
import pyrebase
from neo4j import GraphDatabase
from groq import Groq


# Neo4j Database Driver
driver = GraphDatabase.driver(uri="bolt://localhost:7687", auth=("neo4j", "12345678"), database="GDG")

# Groq API Client
client = Groq(
    api_key=" ",
)

# Function to create a new conversation with Zen
def engage_with_zen(user_input):
    chat_completion = client.chat.completions.create(
        messages=[{"role": "user", "content": user_input}],
        model="llama3-8b-8192",
    )
    return chat_completion.choices[0].message.content

# Function to insert user data into Neo4j database
def insert_user_data(user_name, user_age, user_academic_status):
    def create_user(tx, user_name, user_age, user_academic_status):
        query = """
        CREATE (u:User {
            name: $name,
            age: $age,
            academicStatus: $academicStatus
        })
        """
        tx.run(query, name=user_name, age=user_age, academicStatus=user_academic_status)

    with driver.session() as session:
        session.write_transaction(create_user, user_name, user_age, user_academic_status)

# Function to store user preference in Neo4j
def store_user_preference(user_input):
    def create_preference(tx, user_input):
        query = f"CREATE (p:UserPreference {{content: '{user_input}'}})"
        tx.run(query)

    with driver.session() as session:
        session.write_transaction(create_preference, user_input)


# Streamlit "Share About Me" Page
def share_about_me_page():
    st.title("Share About Me")
    st.subheader("Chat with Zen")

    # Chat message container
    message_container = st.empty()

    if "conversation" not in st.session_state:
        st.session_state.conversation = [("Zen", "Share something about you!")]

    # Create a scrollable chat area
    chat_area = st.container()
    with chat_area:
        st.markdown(
            """
            <style>
            .chat-box {
                height: 400px;
                overflow-y: scroll;
                padding: 10px;
                border: 1px solid #ccc;
                border-radius: 10px;
                background-color: #f9f9f9;
            }
            </style>
            """,
            unsafe_allow_html=True,
        )
        
        chat_box = st.markdown('<div class="chat-box"></div>', unsafe_allow_html=True)
        
        for speaker, message in st.session_state.conversation:
            if speaker == "Zen":
                chat_box.markdown(
                    f"<div style='display: flex; align-items: center; margin-bottom: 10px;'>"
                    f"<img src='https://via.placeholder.com/40' alt='Zen' style='border-radius: 50%; margin-right: 10px;'>"
                    f"<div style='background-color: #007bff; color: white; padding: 10px; border-radius: 10px;'>"
                    f"**{speaker}:** {message}</div></div>", 
                    unsafe_allow_html=True
                )
            else:
                chat_box.markdown(
                    f"<div style='display: flex; align-items: center; margin-bottom: 10px; justify-content: flex-end;'>"
                    f"<div style='background-color: #f1f1f1; color: black; padding: 10px; border-radius: 10px; margin-left: 10px;'>"
                    f"**{speaker}:** {message}</div>"
                    f"<img src='https://via.placeholder.com/40' alt='User' style='border-radius: 50%; margin-left: 10px;'></div>",
                    unsafe_allow_html=True
                )

    # Fixed user input field at the bottom
    user_input = st.text_input("You:", placeholder="Type your message...", key="user_input", max_chars=100)

    if st.button("Send") and user_input:
        # Append user's message to conversation
        st.session_state.conversation.append(("You", user_input))

        # Get response from Zen
        zen_response = engage_with_zen(user_input)
        st.session_state.conversation.append(("Zen", zen_response))

        # Store user preference in Neo4j
        # store_user_preference(user_input)

        # Clear input
        st.experimental_rerun()  # Refresh the app to display new message

# Main app for logged-in users
def main_page():
    st.sidebar.title("Navigation")
    page = st.sidebar.radio("Go to:", ["Share About Me", "Learn", "Progress"])

    if page == "Share About Me":
        share_about_me_page()
    elif page == "Learn":
        st.title("Learn")
        st.write("This page will contain learning resources and materials.")
    elif page == "Progress":
        st.title("Progress")
        st.write("This page will show users their progress in learning.")

# Main app
def main():
    # if st.session_state.get('user'):  # Assuming user authentication state is stored in session
        main_page()
    # else:
        # Assuming login_signup_form() handles login/signup
        # login_signup_form()

if __name__ == "__main__":
    main()
