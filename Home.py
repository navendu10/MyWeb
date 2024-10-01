import streamlit as st
import pandas as pd

# Set page layout
st.set_page_config(layout="wide")


# Define a function for vertical space
def add_vertical_space(space=1):
    for _ in range(space):
        st.write("")


# Define the Home page content
def home_page():
    # Create two columns for image and introduction content
    col1, col2 = st.columns([1, 2])  # Adjust column width ratios

    # Adjust vertical alignment with padding
    with col1:
        add_vertical_space(2)  # Add space before the image to match text
        st.image('images/photo.jpg', width=350)  # Adjust image width

    with col2:
        st.title("Navendu Vyas")
        content = """
            Hello, I'm Navendu Vyas, a Product Manager with 18 years of experience in Data and Analytics. 
            I’ve built this website to showcase a diverse range of machine learning models that I’ve developed. 
            Each model is designed not only to address specific business challenges but also to harness and learn new skills, reflecting my commitment to continuous improvement in the field.

            My goal is to demonstrate my eagerness to learn, adapt, and continuously improve, showcasing how my evolving skills and experience can add value to your organization.
        """
        st.info(content)

    # Project display intro text
    st.markdown("""
        <div style='text-align: center; font-size:20px; color: #1E90FF;'>
            Below you can find some of the apps/projects I have worked on using Python, ML, and Deep Learning. 
        </div>
        """, unsafe_allow_html=True)

    # Create three columns for projects
    col3, empty_col, col4 = st.columns([1, 0.1, 1])  # Narrow gap between the project columns

    # Load project data
    df = pd.read_csv('data.csv', sep=";")

    # Display first 3 projects in col3
    with col3:
        for index, row in df[:3].iterrows():
            st.header(row["title"])
            st.write(row["description"])
            st.image("images/" + row["image"], use_column_width=True)  # Scale images to column width
            st.write(f"[Source Code]({row['url']})")

    # Display remaining projects in col4
    with col4:
        for index, row in df[3:].iterrows():
            st.header(row["title"])
            st.write(row["description"])
            st.image("images/" + row["image"], use_column_width=True)
            st.write(f"[Source Code]({row['url']})")


# Define the Contact Me page content
def contact_page():
    st.title("Contact Me")
    st.write("""
        If you have any questions or would like to get in touch, please reach out via the following methods:

        - **Email:** navendu.vyas1005@gmail.com
        - **LinkedIn:** [Navendu Vyas](https://www.linkedin.com/in/navendu-vyas-34b22017a/)
    """)


# Add sidebar navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Home", "Contact Me"])

# Display the selected page
if page == "Home":
    home_page()
elif page == "Contact Me":
    contact_page()
