import streamlit as st
from google import genai
from pydantic import BaseModel
import json

class TechAnswer(BaseModel):
    topic_name: str
    explanation: str
    real_world_example: str
st.set_page_config(page_title="Mentor App", page_icon="🤖")
st.title("Tech Mentor 🤖")
st.write("Learn Tech Concepts clearly and easily")


topic = st.text_input("What tech concept do you want to learn? (eg: API,Loop)")
ask_btn = st.button("Ask Question")

if ask_btn:
    if topic != "":
        try:

            with st.spinner("Please wait, AI is thinking..."):
                API_KEY = "AQ.Ab8RN6KxLfZNjNUu63rp3JEdFElWR2w60jIQRQRc-I0uOvUe6g"
                client = genai.Client(api_key=API_KEY)
                response = client.models.generate_content(
                    model = 'gemini-3.8-flash',
                    contents = topic,
                    config = {
                        "system_instruction": "you are a strict tech mentor, Explain concepts clearly Follow the exact JSON structure . STRICT RULE: Use simple tanglish,like a tamil tech mentor If the user ask about non-technical topics(like cities, foods,movies), You MUST reject It. set topic_name as 'Out Of Syllabus' and in the explanation write 'Please ask a tech-related question' ",
                        "response_mime_type": "application/json",
                        "response_schema": TechAnswer,

                    }
                )

                answer_dict = json.loads(response.text)

                if answer_dict ["topic_name"] == 'Out Of Syllabus':
                    st.error(answer_dict["explanation"])
                else:
                    st.success(f"Topic : {answer_dict['topic_name']}")
                    st.info(f"Explanation: {answer_dict['explanation']} ")
                    st.warning(f"Example : {answer_dict['real_world_example']}")

        except Exception as e:
            st.error(f"An error occurred: {e}")

    else:

        st.warning("please type a question first ")










