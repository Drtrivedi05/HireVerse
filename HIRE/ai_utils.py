# ai_utils.py
import os
import json
from google import genai
from django.conf import settings


def generate_quiz_questions(topic, total_questions=10, difficulty="Medium"):
    """
    Generate aptitude quiz questions using Google Gemini API.

    Args:
        topic (str): The topic for quiz generation (e.g., "Quantitative Aptitude").
        total_questions (int): Number of questions to generate.
        difficulty (str): Difficulty level ("Easy", "Medium", "Hard").

    Returns:
        list[dict]: A list of question objects with 'question', 'options', and 'answer'.
    """
    # ✅ Fetch API key securely
    api_key = os.getenv("GOOGLE_API_KEY", getattr(settings, "GOOGLE_API_KEY", None))
    if not api_key:
        raise ValueError("❌ Gemini API key not found! Please set GOOGLE_API_KEY in environment or settings.py.")


    # ✅ Initialize Gemini client
    client = genai.Client(api_key=api_key)

    # ✅ Build the structured prompt
    prompt = (
        f"Generate {total_questions} multiple-choice aptitude questions "
        f"on the topic '{topic}' with {difficulty} difficulty. "
        f"Each question must include:\n"
        f"1. Question text\n"
        f"2. Four options (A, B, C, D)\n"
        f"3. The correct option label (A/B/C/D)\n"
        f"Format output strictly as a JSON list like:\n"
        f"[{{'question':'', 'options':{{'A':'','B':'','C':'','D':''}}, 'answer':'A'}}, ...]"
    )

    # ✅ Generate response
    response = client.models.generate_content(
        model="gemini-2.0-flash",
        contents=prompt,
    )

    result_text = response.text.strip()

    # ✅ Try to parse clean JSON output
    try:
        # Gemini sometimes uses single quotes; normalize to double quotes
        normalized_text = result_text.replace("'", '"')
        questions = json.loads(normalized_text)
    except json.JSONDecodeError:
        print("⚠️ Warning: Gemini response not valid JSON. Returning raw text.")
        questions = [{
            "question": result_text,
            "options": {"A": "", "B": "", "C": "", "D": ""},
            "answer": ""
        }]

    return questions
