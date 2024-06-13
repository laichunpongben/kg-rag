# rag/settings.py
import os

from llama_index.core import Settings
from llama_index.embeddings.huggingface import HuggingFaceEmbedding
from llama_index.llms.gemini import Gemini

from google.generativeai.types import HarmCategory, HarmBlockThreshold

from .configs.secret import GOOGLE_API_KEY

os.environ["GOOGLE_API_KEY"] = GOOGLE_API_KEY

Settings.embed_model = HuggingFaceEmbedding(
    model_name="intfloat/multilingual-e5-large-instruct"
)
Settings.llm = Gemini(
    model="models/gemini-1.5-flash-latest",
    request_timeout=360.0,
    safety_settings={
        HarmCategory.HARM_CATEGORY_SEXUALLY_EXPLICIT: HarmBlockThreshold.BLOCK_ONLY_HIGH,
        HarmCategory.HARM_CATEGORY_HATE_SPEECH: HarmBlockThreshold.BLOCK_ONLY_HIGH,
        HarmCategory.HARM_CATEGORY_HARASSMENT: HarmBlockThreshold.BLOCK_ONLY_HIGH,
        HarmCategory.HARM_CATEGORY_DANGEROUS_CONTENT: HarmBlockThreshold.BLOCK_ONLY_HIGH,
    },
)
Settings.chunk_size = 512
Settings.chunk_overlap = 10
