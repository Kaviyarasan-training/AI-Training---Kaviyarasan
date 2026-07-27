import streamlit as st

from app import DEFAULT_MODEL, generate_reply, load_demo_dataset

st.set_page_config(page_title="Email Reply Assistant", page_icon="✉️", layout="centered")

st.title("Email Reply Assistant")
st.write("Generate polished email replies locally with an open-source Ollama model.")

with st.sidebar:
    st.header("Settings")
    model_name = st.text_input("Ollama model", value=DEFAULT_MODEL)
    strategy = st.selectbox(
        "Prompt strategy",
        ["zero-shot", "few-shot", "chain-of-thought"],
        index=0,
    )

    st.caption("Make sure Ollama is running and the model is installed locally.")

sample_dataset = load_demo_dataset("data/synthetic_emails.json")

email_input = st.text_area(
    "Email to reply to",
    height=220,
    placeholder="Type the email you want to respond to here...",
)

col1, col2 = st.columns([1, 1])
with col1:
    generate_button = st.button("Generate reply", use_container_width=True)
with col2:
    if st.button("Load sample", use_container_width=True):
        st.session_state["email_input"] = sample_dataset[0]["email"]

if "email_input" in st.session_state:
    email_input = st.session_state["email_input"]

if generate_button:
    if not email_input.strip():
        st.warning("Please enter an email before generating a reply.")
    else:
        with st.spinner("Generating a response..."):
            try:
                reply = generate_reply(email_input, strategy=strategy, model=model_name)
            except Exception as exc:
                st.error(f"Generation failed: {exc}")
            else:
                st.subheader("Suggested reply")
                st.write(reply)

st.markdown("---")
st.subheader("Sample emails")
for item in sample_dataset:
    with st.expander(item["topic"]):
        st.write(item["email"])
