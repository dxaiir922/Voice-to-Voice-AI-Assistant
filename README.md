# Voice-to-Voice-AI-Assistant


## Project Overview

This project implements a Voice-to-Voice AI Assistant using Python. The assistant listens to the user's voice, converts it into text, sends the text to a Large Language Model (LLM) using the Cohere API
generates an intelligent response, and finally converts the response back into speech.

The project demonstrates the complete Voice-to-Voice interaction pipeline.

---

## Features

- Speech-to-Text (STT)
- AI Response Generation using Cohere
- Text-to-Speech (TTS)
- Real-time voice interaction
- Continuous conversation



## Technologies Used

- Python 3
- Cohere API
- RealtimeSTT
- RealtimeTTS
- python-dotenv

---

## Project Workflow

```text
User Speech
     │
     ▼
Speech-to-Text
     │
     ▼
Recognized Text
     │
     ▼
Cohere Large Language Model
     │
     ▼
Generated Response
     │
     ▼
Text-to-Speech
     │
     ▼
Voice Output
```

---

## Project Structure

Voice-AI-Assistant/
│
├──app.py
├── requirements.txt
├── README.md
├── .env.example
 output png



## Installation

### 1. Install the required packages

pip install -r requirements.txt

### 2. Create a `.env` file

Add your Cohere API key:

COHERE_API_KEY=YOUR_API_KEY


### 3. Run the project

python main.py

## How It Works

### Step 1: Speech-to-Text

The assistant listens through the microphone using the RealtimeSTT library. The user's speech is converted into text.

### Step 2: LLM Processing

The recognized text is sent to the Cohere API, where the Large Language Model generates an intelligent response.

### Step 3: Text-to-Speech

The generated response is converted into speech using RealtimeTTS, allowing the assistant to speak back to the user.

## Requirements

- Python 3.10 or later
- Microphone
- Internet connection
- Cohere API Key
