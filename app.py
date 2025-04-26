import os
import google.generativeai as genai
from flask import Flask, request, jsonify
from flask_cors import CORS

# Initialize Flask App
app = Flask(__name__)
CORS(app)

# Load API Key from Environment Variable
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
if not GEMINI_API_KEY:
    raise ValueError("🚨 Missing Gemini API Key! Set it in your environment variables.")

# Configure the Gemini AI API
genai.configure(api_key=GEMINI_API_KEY)

# Your Name for Personalized Responses
YOUR_NAME = "Suryank Batham"  # Change this to your name

@app.route("/", methods=["GET"])
def home():
    return "🚀 Gemini AI Chatbot Server is Running!"

@app.route("/chat", methods=["POST"])
def chat():
    try:
        data = request.json
        user_message = data.get("message", "").strip()

        if not user_message:
            return jsonify({"error": "No message provided"}), 400

        # Add custom logic for specific questions
        if "who made you" in user_message.lower():
            bot_reply = f"I was created by {YOUR_NAME}."
        elif "who is your trainer" in user_message.lower():
            bot_reply = f"My trainer is {YOUR_NAME}."
        elif "what is your name" in user_message.lower():
            bot_reply = f"My name is Suryank AI Bot"
        elif "who is your master" in user_message.lower():
            bot_reply= f"My master is Master Suryank."
        else:
            # Update this to the correct model name based on the API documentation
            model_name = "gemini-default"  # Replace this with the correct model name you found
            model = genai.GenerativeModel('gemini-2.0-flash')  # Use the correct model here based on your API
            response = model.generate_content(user_message)

            if not response.text:
                raise ValueError("No content returned from the Gemini API.")
            
            bot_reply = response.text

        return jsonify({"response": bot_reply})

    except Exception as e:
        # Print the error in the terminal for easier debugging
        print(f"Error: {str(e)}")
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    print("🚀 Gemini Chatbot Server Running on http://127.0.0.1:5000/")
    app.run(host="0.0.0.0", port=5000, debug=True)
