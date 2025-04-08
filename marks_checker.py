import streamlit as st
import pandas as pd
import datetime


# THIS MUST COME FIRST
st.set_page_config(page_title="Marks Checker", page_icon="📊")

# THEN your custom CSS
st.markdown(
    """
    <style>
    .stApp {
        background-image: url("https://wallpaperaccess.com/full/14500493.png");
        background-size: cover;
        background-repeat: no-repeat;
        background-attachment: fixed;
    }

    .block-container {
        background-color: rgba(255, 255, 255, 0.85);
        padding: 2rem;
        border-radius: 20px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# 🚀 Page configuration


# 📱 Make app mobile responsive
st.markdown("""
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <style>
        .block-container {
            max-width: 100% !important;
            padding: 1rem !important;
        }
    </style>
""", unsafe_allow_html=True)



# 🌗 Dark mode toggle
mode = st.toggle("🌙 Dark Mode")

if mode:
    st.markdown(
        """
        <style>
        body {
            background-color: #0e1117;
            color: white;
        }
        .stTextInput > div > input,
        .stNumberInput > div > input,
        .stDownloadButton button,
        .stTextArea textarea {
            background-color: #1f2937;
            color: white;
            border: 1px solid #374151;
        }
        .st-bb {
            color: white;
        }
        </style>
        """,
        unsafe_allow_html=True
    )


st.markdown("""
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <style>
        /* Makes widgets wrap nicely on small screens */
        .block-container {
            max-width: 100% !important;
            padding: 1rem !important;
        }
    </style>
""", unsafe_allow_html=True)



st.title("📊 Marks Checker")
st.markdown("Welcome! Enter your subject marks below to calculate your percentage and get your grade.")

# Add a nice section header
st.markdown("### 🧮 Step 1: Set Subject Details")

# Then your inputs like:
num_subjects = st.number_input("Number of Subjects", min_value=1, max_value=20, step=1)
total_per_subject = st.number_input("Total Marks per Subject (like 100)", min_value=1)

# Then another section:
st.markdown("### ✍️ Step 2: Enter Your Marks")


# Set the page title and icon


# Title
st.markdown("<h1 style='text-align: center; color: #4CAF50;'>📊 Marks Percentage & Grade Checker</h1>", unsafe_allow_html=True)
st.write("### Welcome! Enter your marks below to check your performance 🎓")

# Divider
st.markdown("---")

# Step 1: Subject details
st.subheader("🔢 Step 1: Enter Subject Details")

num_subjects = st.number_input("How many subjects do you have?", min_value=1)
total_per_subject = st.number_input("Total marks per subject (e.g. 100):", min_value=1.0)

# Divider
st.markdown("---")

# Step 2: Marks entry
st.subheader("✍️ Step 2: Enter Your Marks")

marks = []
if num_subjects and total_per_subject:
    for i in range(int(num_subjects)):
        mark = st.number_input(f"Marks obtained in Subject {i+1}", min_value=0.0, max_value=float(total_per_subject), key=f"mark_{i}")
        marks.append(mark)

# Divider
st.markdown("---")

# Step 3: Results
st.subheader("📈 Step 3: Result & Grade")

if len(marks) == int(num_subjects):
    total_marks_obtained = sum(marks)
    total_maximum = int(num_subjects) * total_per_subject
    percentage = (total_marks_obtained / total_maximum) * 100

    st.success(f"✅ Your Total Marks: **{total_marks_obtained} / {total_maximum}**")
    st.info(f"📊 Your Percentage: **{percentage:.2f}%**")

    # Grade logic
    grade = ""
    if 90 <= percentage <= 100:
        grade = "A+ Grade 🏅"
    elif 80 <= percentage < 90:
        grade = "A Grade 🥈"
    elif 70 <= percentage < 80:
        grade = "B Grade 🥉"
    elif 50 <= percentage < 70:
        grade = "C Grade 👍"
    elif 33 <= percentage < 50:
        grade = "D Grade 👀"
    else:
        grade = "Fail 😞"

    st.warning(f"🎓 Your Grade: **{grade}**")

    st.markdown("### 🧾 Step 3: Your Result")

# Show calculated percentage
st.success(f"✅ Your Percentage is: **{percentage:.2f}%**")

# Show grade with a nice message
if percentage >= 90:
    st.balloons()
    st.markdown("🎉 **Grade: A+** - Excellent! You're a topper!")
elif percentage >= 80:
    st.markdown("🥳 **Grade: A** - Great job!")
elif percentage >= 70:
    st.markdown("👏 **Grade: B** - Good work, keep it up!")
elif percentage >= 50:
    st.markdown("👍 **Grade: C** - Not bad, you can improve!")
elif percentage >= 33:
    st.markdown("⚠️ **Grade: D** - Just passed. Focus more!")
else:
    st.error("❌ **Fail** - Don’t give up. Try harder next time!")



mark_list = total_marks_obtained

# Create a DataFrame for the chart
df = pd.DataFrame({
    'Subject': [f'Subject {i+1}' for i in range(num_subjects)],
    'Marks Obtained': marks,
    'Total Marks': [total_per_subject] * int(num_subjects)
})

# Bar Chart
st.markdown("### 📊 Marks Comparison")
st.bar_chart(df.set_index('Subject')[['Marks Obtained', 'Total Marks']])

st.markdown("### 👤 Student Information")
name = st.text_input("Enter your name")
roll = st.text_input("Enter your roll number")
student_class = st.text_input("Enter your class")

if name and roll and student_class:
    # Grade calculation
    grade_text = ""
    if percentage >= 90:
        grade_text = "A+"
    elif percentage >= 80:
        grade_text = "A"
    elif percentage >= 70:
        grade_text = "B"
    elif percentage >= 50:
        grade_text = "C"
    elif percentage >= 33:
        grade_text = "D"
    else:
        grade_text = "Fail"

    # Result text
    result_text = f"""
    Student Name: {name}
    Roll Number: {roll}
    Class: {student_class}
    Date: {datetime.date.today()}

    Total Subjects: {num_subjects}
    Total Marks per Subject: {total_per_subject}
    Marks Obtained: {sum(marks)}
    Percentage: {percentage:.2f}%
    Grade: {grade_text}
    """

    # Download button
    st.download_button(
        label="📥 Download Result",
        data=result_text,
        file_name=f"{name}_result.txt",
        mime="text/plain"
    )
else:
    st.warning("⚠️ Please fill in your Name, Roll Number, and Class to generate your result.")

