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
            type = st.selectbox("Scenario Type", ["sales", "customer"],placeholder = "Select Type", index= None)  
            persona_name = st.text_input("Persona Name")
            

        voice_dict = {"Ava":"en-US-AvaMultilingualNeural", "Andrew" :"en-US-AndrewMultilingualNeural"}
        with col2:
            image_url = st.text_input("Image URL")
            voice_id = st.selectbox("Voice ID", list(voice_dict.keys()),placeholder = "Select Voice ID", index= None) 

        # Persona Description
        persona = st.text_area("AI Persona Description")

        # Prompt
        difficulty_level = st.selectbox("Difficulty Level", ["easy", "medium", "hard"],placeholder = "Select Level", index= None)  

        prompt = st.text_area("Prompt")

        submitted = st.form_submit_button("Add Scenario")

        if submitted:
            # Prepare data for API request
            params = {
                "name": name,
                "difficulty_level": difficulty_level,
                "prompt": prompt,
                "type": type,
                "persona": persona,
                "persona_name": persona_name,
                "image_url": image_url,
                "voice_id": voice_dict[voice_id]
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
