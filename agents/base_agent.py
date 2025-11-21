import json
import google.generativeai as genai
from typing import Optional, Dict, Any
import os

class BaseAgent:
    """Base agent with Gemini communication + JSON-safe parsing."""

    def __init__(self, model=None):
        # autodetect model
        if model is None:
            model_name = "models/gemini-2.5-flash"
            api_key = os.environ.get("GOOGLE_API_KEY")
            if api_key:
                genai.configure(api_key=api_key)
                self.model = genai.GenerativeModel(model_name)
            else:
                self.model = None
        else:
            self.model = model

    def _call_model(self, prompt: str) -> Optional[str]:
        if self.model is None:
            return None
        try:
            response = self.model.generate_content(prompt)
            return response.text
        except Exception as e:
            print(f"[Agent Warning] Gemini call failed: {e}")
            return None

    def _json_from_response(self, raw: Optional[str]) -> Optional[Dict[str, Any]]:
        if not raw:
            return None
        try:
            return json.loads(raw)
        except Exception:
            try:
                start = raw.index("{")
                end = raw.rindex("}") + 1
                return json.loads(raw[start:end])
            except:
                return None
