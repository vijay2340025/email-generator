import sys

import streamlit as st
from streamlit.web import cli

from prompt.email_prompt import build_email_prompt
from generator.email_generator import Model

def run_app():
    st.set_page_config(page_title="Email Generator", layout="centered")

    with st.sidebar:
        st.markdown("### Model Settings: ")
        model_choice = st.selectbox("Choose a model", ["Gemini", "Custom"])
        custom_model_url = None
        custom_api_key = None

        if model_choice == "Custom":
            model_choice = st.text_input(
                "Model Name", placeholder="provider:model_name"
            )
            custom_model_url = st.text_input("URL")
            custom_api_key = st.text_input("API Key", type="password")

    st.markdown("### Email Generator")
    st.markdown("---")

    col1, col2, col3 = st.columns(3)

    with col1:
        purpose = st.selectbox(
            "Purpose of Email",
            [
                "Leave Request",
                "Follow-up",
                "Meeting Request",
                "Project Update",
                "Apology",
                "Thank You",
                "Custom",
            ],
        )

    with col2:
        tone = st.selectbox(
            "Tone",
            ["Formal", "Friendly", "Direct & Concise", "Urgent"],
        )

    with col3:
        recipient = st.selectbox(
            "Recipient Type",
            ["HR / Manager", "Colleague", "Client"],
        )

    if purpose == "Custom":
        purpose = st.text_input(
            "Specify Email Purpose",
            placeholder="e.g., Informing delay to meeting",
        )

    key_points = st.text_area(
        "Key Details to Include",
        placeholder="e.g., Requesting 2 days leave.",
        height=100,
    )

    with st.expander("Optional Settings"):
        opt_col1, opt_col2 = st.columns(2)
        with opt_col1:
            length = st.selectbox("Length", ["Medium", "Short", "Detailed"])
        with opt_col2:
            language = st.selectbox("Language", ["English", "French", "Dutch"])

    if st.button("Generate Email", type="primary", use_container_width=True):
        with st.spinner("Generating email..."):
            system_prompt, user_prompt = build_email_prompt(
                purpose=purpose,
                tone=tone,
                recipient=recipient,
                key_points=key_points,
                length=length,
                language=language,
            )
            st.session_state.email_draft = f"[Debug Prompt Preview]\n\nSYSTEM:\n{system_prompt}\n\nUSER:\n{user_prompt}"
            llm = Model(model_choice, custom_model_url , custom_api_key)
            st.session_state.email = llm.inference(st.session_state.email_draft)

        if st.session_state.email:
            st.divider()
            st.caption("Click the copy icon in the top-right corner below:")
            st.code(st.session_state.email, language=None)


def main():
    if st.runtime.exists():
        run_app()
    else:
        sys.argv = ["streamlit", "run", __file__]
        sys.exit(cli.main())


if __name__ == "__main__":
    main()
