import streamlit as st
import requests
import json

# Configure the API URL
API_URL = "https://scenario-fetching-101415335665.us-central1.run.app"  

def main():
    st.title("Scenario Management System")
    st.subheader("Add New Scenario")

    # Create form for scenario input
    with st.form("scenario_form"):
        # Basic Information
        col1, col2 = st.columns(2)
        with col1:
            name = st.text_input("Scenario Name")
            type = st.selectbox("Scenario Type", ["sales", "customer"],placeholder = "Select Type", index= None)  # Add your scenario types
            persona_name = st.text_input("Persona Name")
            
        with col2:
            image_url = st.text_input("Image URL")
            voice_id = st.text_input("Voice ID")

        # Persona Description
        persona = st.text_area("AI Persona Description")

        # Prompts
        st.subheader("Prompts")
        prompt = st.text_area("Main Prompt")
        
        col3, col4, col5 = st.columns(3)
        with col3:
            easy_prompt = st.text_area("Easy Prompt")
        with col4:
            medium_prompt = st.text_area("Medium Prompt")
        with col5:
            hard_prompt = st.text_area("Hard Prompt")

        submitted = st.form_submit_button("Add Scenario")

        if submitted:
            # Prepare data for API request
            params = {
                "name": name,
                "prompt": prompt,
                "easy_prompt": easy_prompt,
                "medium_prompt": medium_prompt,
                "hard_prompt": hard_prompt,
                "type": type,
                "persona": persona,
                "persona_name": persona_name,
                "image_url": image_url,
                "voice_id": voice_id
            }

            try:
                # Make API request
                response = requests.post(f"{API_URL}/scenarios", params=params)
                
                if response.status_code == 201:
                    st.success("Scenario created successfully!")
                    st.json(response.json())
                else:
                    st.error(f"Error creating scenario: {response.text}")
            except requests.exceptions.RequestException as e:
                st.error(f"Error connecting to server: {str(e)}")

    # # Display existing scenarios
    # if st.button("Show All Scenarios"):
    #     try:
    #         response = requests.get(f"{API_URL}/scenarios")
    #         if response.status_code == 200:
    #             scenarios = response.json()
    #             st.write("Existing Scenarios:")
    #             st.json(scenarios)
    #     except requests.exceptions.RequestException as e:
    #         st.error(f"Error fetching scenarios: {str(e)}")

if __name__ == "__main__":
    main()