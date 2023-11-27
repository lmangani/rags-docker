"""Configuration."""
import streamlit as st
import os

### DEFINE BUILDER_LLM #####
## Uncomment the LLM you want to use to construct the meta agent

## OpenAI
from llama_index.llms import OpenAI

# set OpenAI Key - use Streamlit secrets
os.environ["OPENAI_API_BASE"] = "http://localhost:1337/v1"
#os.environ["OPENAI_API_KEY"] = st.secrets.openai_key
# load LLM
BUILDER_LLM = OpenAI(model="gpt-3.5-turbo")
