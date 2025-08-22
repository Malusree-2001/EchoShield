import streamlit as st  

# Title of the app  
st.title("🚨 EchoShield – Hackathon Starter 🚨")  

# A welcome message  
st.write("Hello, Hackathon world! 🎉")  
st.write("This is your very first Streamlit app.")  

# Add a simple button  
if st.button("Click Me!"):  
    st.success("You just ran your first hackathon app!")  
