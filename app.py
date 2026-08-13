import streamlit as st
import pandas as pd
import joblib


# ============================================================
# PAGE CONFIGURATION
# ============================================================

st.set_page_config(
    page_title="Student Stress Level Prediction",
    page_icon="🎓",
    layout="wide"
)


# ============================================================
# LOAD TRAINED RANDOM FOREST MODEL
# ============================================================

model = joblib.load(
    "models/stress_level_random_forest.pkl"
)


# ============================================================
# HELPER FUNCTION
# ============================================================

def get_value(question, options, values):
    """
    Display a user-friendly question.

    The user selects a text answer.
    The selected answer is converted into
    the numerical value required by the ML model.
    """

    answer = st.selectbox(
        question,
        options
    )

    # Convert selected text answer to numerical value
    return values[options.index(answer)]


# ============================================================
# TITLE
# ============================================================

st.title(
    "🎓 Student Stress Level Prediction System"
)

st.write(
    "Please answer the following questions based on your "
    "current academic, personal and social situation."
)

st.divider()


# ============================================================
# SECTION 1
# ACADEMIC & MENTAL WELL-BEING
# ============================================================

st.header(
    "📚 Academic & Mental Well-being"
)

col1, col2 = st.columns(2)


# ------------------------------------------------------------
# COLUMN 1
# ------------------------------------------------------------

with col1:

    anxiety_level = get_value(
        "How often do you feel anxious about your studies or daily life?",
        [
            "Never",
            "Rarely",
            "Sometimes",
            "Often",
            "Very Often"
        ],
        [
            0,
            5,
            10,
            16,
            21
        ]
    )


    depression = get_value(
        "How frequently have you been feeling depressed or emotionally low?",
        [
            "Never",
            "Rarely",
            "Sometimes",
            "Often",
            "Very Often"
        ],
        [
            0,
            7,
            13,
            20,
            27
        ]
    )


    self_esteem = get_value(
        "How would you describe your confidence and self-esteem?",
        [
            "Very Low",
            "Low",
            "Moderate",
            "High",
            "Very High"
        ],
        [
            0,
            8,
            15,
            23,
            30
        ]
    )


    academic_performance = get_value(
        "How would you describe your current academic performance?",
        [
            "Very Poor",
            "Poor",
            "Average",
            "Good",
            "Very Good"
        ],
        [
            0,
            1,
            2,
            4,
            5
        ]
    )


    study_load = get_value(
        "How heavy is your current study workload?",
        [
            "Very Low",
            "Low",
            "Moderate",
            "High",
            "Very High"
        ],
        [
            0,
            1,
            2,
            4,
            5
        ]
    )


# ------------------------------------------------------------
# COLUMN 2
# ------------------------------------------------------------

with col2:

    mental_health_history = get_value(
        "Have you previously experienced mental health difficulties?",
        [
            "No",
            "Yes"
        ],
        [
            0,
            1
        ]
    )


    headache = get_value(
        "How often do you experience headaches?",
        [
            "Never",
            "Rarely",
            "Sometimes",
            "Often",
            "Very Often"
        ],
        [
            0,
            1,
            3,
            4,
            5
        ]
    )


    sleep_quality = get_value(
        "How would you describe your sleep quality?",
        [
            "Very Poor",
            "Poor",
            "Average",
            "Good",
            "Very Good"
        ],
        [
            0,
            1,
            2,
            4,
            5
        ]
    )


    future_career_concerns = get_value(
        "How worried are you about your future career?",
        [
            "Not Worried",
            "Slightly Worried",
            "Moderately Worried",
            "Very Worried",
            "Extremely Worried"
        ],
        [
            0,
            1,
            2,
            4,
            5
        ]
    )


# ============================================================
# SECTION 2
# SOCIAL & ENVIRONMENTAL SITUATION
# ============================================================

st.divider()

st.header(
    "👥 Social & Environmental Situation"
)

col1, col2 = st.columns(2)


# ------------------------------------------------------------
# COLUMN 1
# ------------------------------------------------------------

with col1:

    teacher_student_relationship = get_value(
        "How would you describe your relationship with your teachers?",
        [
            "Very Poor",
            "Poor",
            "Average",
            "Good",
            "Very Good"
        ],
        [
            0,
            1,
            2,
            4,
            5
        ]
    )


    social_support = get_value(
        "How much social support do you receive from friends or family?",
        [
            "None",
            "Low",
            "Moderate",
            "High"
        ],
        [
            0,
            1,
            2,
            3
        ]
    )


    peer_pressure = get_value(
        "How much peer pressure do you experience?",
        [
            "None",
            "Low",
            "Moderate",
            "High",
            "Very High"
        ],
        [
            0,
            1,
            2,
            4,
            5
        ]
    )


    bullying = get_value(
        "How often do you experience bullying or negative treatment?",
        [
            "Never",
            "Rarely",
            "Sometimes",
            "Often",
            "Very Often"
        ],
        [
            0,
            1,
            2,
            4,
            5
        ]
    )


# ------------------------------------------------------------
# COLUMN 2
# ------------------------------------------------------------

with col2:

    safety = get_value(
        "How safe and secure do you feel in your daily environment?",
        [
            "Very Unsafe",
            "Unsafe",
            "Moderately Safe",
            "Safe",
            "Very Safe"
        ],
        [
            0,
            1,
            2,
            4,
            5
        ]
    )


    basic_needs = get_value(
        "How well are your basic needs such as food, housing and daily necessities met?",
        [
            "Very Poorly",
            "Poorly",
            "Moderately",
            "Well",
            "Very Well"
        ],
        [
            0,
            1,
            2,
            4,
            5
        ]
    )


    living_conditions = get_value(
        "How would you describe your living conditions?",
        [
            "Very Poor",
            "Poor",
            "Average",
            "Good",
            "Very Good"
        ],
        [
            0,
            1,
            2,
            4,
            5
        ]
    )


    noise_level = get_value(
        "How much noise disturbance do you experience while studying or resting?",
        [
            "None",
            "Very Low",
            "Moderate",
            "High",
            "Very High"
        ],
        [
            0,
            1,
            2,
            4,
            5
        ]
    )


# ============================================================
# SECTION 3
# HEALTH & DAILY ACTIVITIES
# ============================================================

st.divider()

st.header(
    "🏃 Health & Daily Activities"
)

col1, col2 = st.columns(2)


# ------------------------------------------------------------
# COLUMN 1
# ------------------------------------------------------------

with col1:

    breathing_problem = get_value(
        "How often do you experience breathing difficulties?",
        [
            "Never",
            "Rarely",
            "Sometimes",
            "Often",
            "Very Often"
        ],
        [
            0,
            1,
            2,
            4,
            5
        ]
    )


    extracurricular_activities = get_value(
        "How actively do you participate in extracurricular activities?",
        [
            "Not at all",
            "Very Little",
            "Moderately",
            "Often",
            "Very Often"
        ],
        [
            0,
            1,
            2,
            4,
            5
        ]
    )


# ------------------------------------------------------------
# COLUMN 2
# ------------------------------------------------------------

with col2:

    blood_pressure = get_value(
        "How would you describe your academic  pressure condition?",
        [
            "Normal",
            "Moderately Elevated",
            "High"
        ],
        [
            1,
            2,
            3
        ]
    )


# ============================================================
# PREDICTION SECTION
# ============================================================

st.divider()

st.header(
    "🔮 Stress Prediction"
)


# ============================================================
# PREDICTION BUTTON
# ============================================================

if st.button(
    "🔮 Predict Stress Level",
    use_container_width=True
):

    # --------------------------------------------------------
    # CREATE INPUT DATAFRAME
    # --------------------------------------------------------

    input_data = pd.DataFrame(
        [[
            anxiety_level,
            self_esteem,
            mental_health_history,
            depression,
            headache,
            blood_pressure,
            sleep_quality,
            breathing_problem,
            noise_level,
            living_conditions,
            safety,
            basic_needs,
            academic_performance,
            study_load,
            teacher_student_relationship,
            future_career_concerns,
            social_support,
            peer_pressure,
            extracurricular_activities,
            bullying
        ]],
        columns=[
            "anxiety_level",
            "self_esteem",
            "mental_health_history",
            "depression",
            "headache",
            "blood_pressure",
            "sleep_quality",
            "breathing_problem",
            "noise_level",
            "living_conditions",
            "safety",
            "basic_needs",
            "academic_performance",
            "study_load",
            "teacher_student_relationship",
            "future_career_concerns",
            "social_support",
            "peer_pressure",
            "extracurricular_activities",
            "bullying"
        ]
    )


    # --------------------------------------------------------
    # MAKE PREDICTION
    # --------------------------------------------------------

    prediction = model.predict(
        input_data
    )[0]


    # --------------------------------------------------------
    # CONVERT CLASS TO STRESS LEVEL
    # --------------------------------------------------------

    if prediction == 0:

        stress_level = "Low Stress"

        explanation = (
            "The model predicts that this student "
            "has a low level of stress."
        )

        result_type = "low"


    elif prediction == 1:

        stress_level = "Medium Stress"

        explanation = (
            "The model predicts that this student "
            "has a medium level of stress."
        )

        result_type = "medium"


    else:

        stress_level = "High Stress"

        explanation = (
            "The model predicts that this student "
            "has a high level of stress."
        )

        result_type = "high"


    # ========================================================
    # DISPLAY RESULT
    # ========================================================

    st.divider()

    st.subheader(
        "📊 Prediction Result"
    )


    # --------------------------------------------------------
    # LOW STRESS
    # --------------------------------------------------------

    if result_type == "low":

        st.success(
            "🟢 LOW STRESS"
        )


    # --------------------------------------------------------
    # MEDIUM STRESS
    # --------------------------------------------------------

    elif result_type == "medium":

        st.warning(
            "🟡 MEDIUM STRESS"
        )


    # --------------------------------------------------------
    # HIGH STRESS
    # --------------------------------------------------------

    elif result_type == "high":

        st.error(
            "🔴 HIGH STRESS"
        )


    # --------------------------------------------------------
    # EXPLANATION
    # --------------------------------------------------------

    st.write(
        explanation
    )


    # --------------------------------------------------------
    # SHOW PROCESSED VALUES
    # --------------------------------------------------------

    with st.expander(
        "View processed input values"
    ):

        st.dataframe(
            input_data,
            use_container_width=True
        )