import streamlit as st
import pandas as pd
import numpy as np
import time

# Function to generate random values for temperature and pulse rate with mild changes within a range
def generate_random_data(prev_temp, prev_pulse):
    temp_change = np.clip(np.random.uniform(-0.8, 0.8), -0.8, 0.8)
    pulse_change = np.clip(np.random.uniform(-1.5, 1.5), -1.5, 1.5)
    
    temp = np.clip(prev_temp + temp_change, 37.0 - 2.5, 37.0 + 2.5)
    pulse = np.clip(prev_pulse + pulse_change, 70 - 6, 70 + 6)
    
    return temp, pulse

def app():
    # Initialize data storage for each user
    if 'data' not in st.session_state:
        st.session_state.data = {
            'skanda': pd.DataFrame(columns=['Time', 'Temperature', 'Pulse']),
            'deekhsith': pd.DataFrame(columns=['Time', 'Temperature', 'Pulse']),
            'sanjana_wg': pd.DataFrame(columns=['Time', 'Temperature', 'Pulse']),
            'sanjana_bj': pd.DataFrame(columns=['Time', 'Temperature', 'Pulse'])
        }
        st.session_state.prev_temp = 37.0
        st.session_state.prev_pulse = 70

    # Function to update data for a user
    def update_data(user):
        temp, pulse = generate_random_data(st.session_state.prev_temp, st.session_state.prev_pulse)
        st.session_state.prev_temp = temp
        st.session_state.prev_pulse = pulse
        new_data = pd.DataFrame([[time.time(), temp, pulse]], columns=['Time', 'Temperature', 'Pulse'])
        st.session_state.data[user] = pd.concat([st.session_state.data[user], new_data], ignore_index=True)
        return temp, pulse

    # Function to run the live update loop
    def run_live_update(user, duration_minutes):
        duration_seconds = duration_minutes * 60
        start_time = time.time()
        end_time = start_time + duration_seconds

        temp_placeholder = st.empty()
        pulse_placeholder = st.empty()
        chart_placeholder = st.empty()
        timer_placeholder = st.empty()

        while time.time() < end_time:
            temp, pulse = update_data(user)

            temp_placeholder.metric("Temperature (°C)", f"{temp:.2f}")
            pulse_placeholder.metric("Pulse Rate (bpm)", f"{pulse:.2f}")

            chart_placeholder.line_chart(st.session_state.data[user].set_index('Time'))

            remaining_time = int(end_time - time.time())
            minutes, seconds = divmod(remaining_time, 60)
            timer_placeholder.write(f"Time remaining: {minutes} minutes {seconds} seconds")

            time.sleep(2.8)
        st.success(f"Monitoring for {user.replace('_', ' ').title()} completed.")

    gradient_text_html = """
        <style>
        .gradient-text {
            font-weight: bold;
            background: -webkit-linear-gradient(left, #07539e, #4fc3f7, #ffffff);
            background: linear-gradient(to right, #07539e, #4fc3f7, #ffffff);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            display: inline;
            font-size: 2.9em;
        }
        </style>
        <div class="gradient-text">Live Patient Temperature and Pulse Rate Monitoring</div>
        """

    # Render the gradient text
    st.markdown(gradient_text_html, unsafe_allow_html=True)
    st.image('divider.png')
    
    st.write('')

    # Patient info
    patient_info = {
        'deek': {'Name': 'Deek', 'Gender': 'Male', 'Cancer Type': 'Kidney', 'Headache': False},
        'sanjana': {'Name': 'Sanjana W G', 'Gender': 'Female', 'Cancer Type': 'Breast', 'Headache': False},
        'sanjana_bj': {'Name': 'Shreyashri', 'Age': 34, 'Gender': 'Female', 'Cancer Type': 'Liver'},
        'skanda': {'Name': 'Skanda', 'Age': 45, 'Gender': 'Male', 'Cancer Type': 'Lung'}
    }

    # User forms in two columns
    col1, col2 = st.columns(2)

    users = {
        'skanda': 'Skanda',
        'deekhsith': 'Deek',
        'sanjana_wg': 'Sanjana',
        'sanjana_bj': 'Sanjana BJ'
    }

    with col1:
        for user in ['skanda', 'deekhsith']:
            with st.form(key=user):
                st.write(f"Session for patient - {users[user]}")
                col8, col9 , col7 = st.columns([0.5,1,0.5])
                with col9:
                    st.image('user.jpeg')
                duration = st.number_input(f"Set duration for {users[user]} (minutes)", min_value=1, step=1, value=1)
                info_button = st.form_submit_button(label='Patient Info')
                submit_button = st.form_submit_button(label='Start Session')

                if info_button:
                    st.write(f"Patient Info for {users[user]}:")
                    st.json(patient_info[user])
                
                if submit_button:
                    st.session_state.duration = duration
                    st.session_state.selected_user = user
                    st.session_state.prev_temp = 37.0  # Reset to baseline values for each session
                    st.session_state.prev_pulse = 70

    with col2:
        for user in ['sanjana_wg', 'sanjana_bj']:
            with st.form(key=user):
                st.write(f"Session for patient - {users[user]}")
                col4, col5 , col6 = st.columns([0.5,1,0.5])
                with col5:
                    st.image('user.jpeg')
                duration = st.number_input(f"Set duration for {users[user]} (minutes)", min_value=1, step=1, value=1)
                info_button = st.form_submit_button(label='Patient Info')
                submit_button = st.form_submit_button(label='Start Session')

                if info_button:
                    st.write(f"Patient Info for {users[user]}:")
                    st.json(patient_info[user])
                
                if submit_button:
                    st.session_state.duration = duration
                    st.session_state.selected_user = user
                    st.session_state.prev_temp = 37.0  # Reset to baseline values for each session
                    st.session_state.prev_pulse = 70

    # Check if a user has been selected and display their graph
    if 'selected_user' in st.session_state and 'duration' in st.session_state:
        selected_user = st.session_state.selected_user
        duration = st.session_state.duration
        st.write(f"Displaying data for {users[selected_user]}")
        run_live_update(selected_user, duration)

if __name__ == "__main__":
    app()
