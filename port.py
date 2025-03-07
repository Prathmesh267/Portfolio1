import streamlit as st
from PIL import Image

# Set Page Configuration (Must be the first Streamlit command)
st.set_page_config(page_title="Prathmesh's Portfolio", page_icon="🚀", layout="wide")

# Apply Background Image Using CSS
st.markdown(
    """
    <style>
        .stApp {
            background: url("static/bg.jpg") no-repeat center center fixed;
            background-size: cover;
        }
        .title {
            text-align: center;
            font-size: 30px;  # Reduced font size here
            font-weight: bold;
            color: #00e6e6;
            text-shadow: 2px 2px 8px rgba(0, 255, 255, 0.5);
        }
        .subtitle {
            text-align: center;
            font-size: 20px;  # Reduced font size here
            font-weight: bold;
            color: #d1d1d1;
            margin-bottom: 20px;
        }
        .section-title {
            font-size: 28px;
            font-weight: bold;
            color: #00e6e6;
            margin-top: 30px;
            border-bottom: 3px solid #00e6e6;
            padding-bottom: 8px;
            transition: transform 0.3s ease, box-shadow 0.3s ease;
        }
        .section-title:hover {
            transform: scale(1.1);
            box-shadow: 0px 8px 16px rgba(0, 255, 255, 0.3);
        }
    </style>
    """,
    unsafe_allow_html=True
)

# Load Image
image_path = "Passport_Photograph.jpeg"
image = Image.open(image_path)

# Resize the image to a specific width and height (e.g., 200x200)
image = image.resize((200, 200))

# Create a layout with columns
col1, col2, col3 = st.columns([1, 3, 1])

# Display Image on the left column (top-left corner)
with col1:
    st.image(image, use_container_width=False)

# Title and Subtitle on Home Page in center column
with col2:
    st.markdown('<p class="title">Hello, I am Prathmesh Bondre</p>', unsafe_allow_html=True)
    st.markdown('<p class="subtitle">Data Engineer | Data Analyst | Big Data Enthusiast</p>', unsafe_allow_html=True)

# Create Buttons for Navigation
st.sidebar.title("🔍 Navigate")
home_button = st.sidebar.button("Home")
about_me_button = st.sidebar.button("About Me")
skills_button = st.sidebar.button("Skills")
projects_button = st.sidebar.button("Projects")
certifications_button = st.sidebar.button("Certifications")
contact_button = st.sidebar.button("Contact")

# Home Section
if home_button:
    st.write("**Welcome to my portfolio!**")
    st.write("I specialize in **Data Engineering, Analytics, and Big Data Technologies.**")

# About Me Section
elif about_me_button:
    st.markdown('<p class="section-title">📝 About Me</p>', unsafe_allow_html=True)
    st.write(""" 
    I am a highly motivated Data Engineer and Analyst with hands-on experience in building scalable data pipelines, performing data analysis, and implementing machine learning solutions. 
    My journey revolves around extracting insights from data and using those insights to drive business value. I'm particularly passionate about working with big data technologies such as Apache Spark, Kafka, and AWS services. 
    I thrive on solving real-world challenges and am always eager to learn and explore new technologies in the ever-evolving data field.
    """)

# Skills Section
elif skills_button:
    st.markdown('<p class="section-title">🛠 Skills</p>', unsafe_allow_html=True)
    skills = [
        "**Programming Language:** Python",
        "**Database:** MySQL",
        "**Data Visualization Tool:** Power BI",
        "**Big Data Technologies:** PySpark, Hive, Kafka, Airflow",
        "**Operating System:** Linux",
        "**Cloud Computing:** AWS (S3, EC2, Glue, SageMaker)",
        "**Machine Learning:** Supervised and Unsupervised Learning"
    ]
    for skill in skills:
        st.markdown(f"✅ {skill}")

# Projects Section
elif projects_button:
    st.markdown('<p class="section-title">📌 Projects</p>', unsafe_allow_html=True)

    st.subheader("🔹 Credit Card Fraud Detection")
    st.write("""
    Built an ML-based system using Decision Tree & AWS to identify fraudulent transactions.
    - Developed an interactive UI using Streamlit to upload transaction data for fraud detection.
    - Integrated AWS S3 for secure storage and retrieval of the trained Decision Tree model.
    - Implemented PySpark-based data preprocessing in AWS Glue to clean and transform input data.
    - Leveraged Machine Learning (MLlib) to classify transactions as Fraudulent or Legitimate in real-time.
    - Connected AWS Athena with Power BI to visualize fraud patterns and enhance data-driven insights.
    - Enabled CSV result download functionality, allowing users to export fraud predictions for further analysis.
    """)

    st.subheader("🔹 Travel Insight Hub")
    st.write("""
    Developed a community-driven travel platform using Streamlit and MySQL.
    - Enabled users to plan, track, and share their travel experiences.
    - Provided insights into popular destinations, seasonal trends, and optimal trip durations.
    - Allowed users to log upcoming and completed trips with feedback.
    - Implemented sentiment analysis on travel feedback for better recommendations.
    - Optimized data retrieval and user experience for seamless navigation.
    """)

    st.subheader("🔹 Stock Market Analysis")
    st.write("""
    Analyzing stock market trends using historical data, technical indicators, and analytics to support informed investment decisions.
    - Exploratory Data Analysis (EDA): Analyze stock price fluctuations, trading volume, and market trends using Python.
    - Analyzes stock price fluctuations, trading volume, and market behavior.
    - Helps investors and analysts identify potential opportunities and risks.
    - Aids in making informed decisions about buying, holding, or selling stocks.
    - Provides insights into market sentiment, economic influences, and industry performance.
    - Enhances the ability to predict future stock movements based on historical data.
    """)

# Certifications Section
elif certifications_button:
    st.markdown('<p class="section-title">🏆 Certifications</p>', unsafe_allow_html=True)
    st.markdown("""- **Python** – Disha Computers  
    - **PwC Switzerland Power BI Simulation** – Forage  
    - **HackerRank - SQL**""", unsafe_allow_html=True)

# Contact Section
elif contact_button:
    st.markdown('<p class="section-title">📞 Contact</p>', unsafe_allow_html=True)
    st.markdown("""📧 **Email:** [prathmeshbondre209@gmail.com](mailto:prathmeshbondre209@gmail.com)  
    🔗 **LinkedIn:** [linkedin.com/in/prathmesh-bondre-398120218](https://www.linkedin.com/in/prathmesh-bondre-398120218/)  
    🐙 **GitHub:** [github.com/prathmeshbondre](https://github.com/prathmeshbondre)
    """, unsafe_allow_html=True)

    st.markdown('<p class="section-title">✉️ Send a Message</p>', unsafe_allow_html=True)
    name = st.text_input("Your Name")
    email = st.text_input("Your Email")
    message = st.text_area("Your Message")
    if st.button("Send Message"):
        st.success("Your message has been sent successfully!")
