import streamlit as st

st.title("Kryptonic")
st.write("Hello, Streamlit!")

# Add an interactive widget
user_input = st.text_input("Enter your name:")
if user_input:
    st.write(f"Welcome, {user_input}!")


st.button("Reset", type="primary")
if st.button("Say hello"):
    st.write("Why hello there")
else:
    st.write("Goodbye")

if st.button("Aloha", type="tertiary"):
    st.write("Ciao")
# Using object notation
add_selectbox = st.sidebar.selectbox(
    "How would you like to be contacted?",
    ("Email", "Home phone", "Mobile phone")
)

# Using "with" notation
with st.sidebar:
    add_radio = st.radio(
        "Choose a shipping method",
        ("Standard (5-15 days)", "Express (2-5 days)")
    )

# Add a slider and display its value squared
value = st.slider("Select a number:", 0, 100, 50)
st.write(f"The square of {value} is {value * value}")
