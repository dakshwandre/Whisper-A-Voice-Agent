# Whisper : A VoiceAgent

Personal AI voice assistant running entirely locally with LLM function-calling.

## Features
- 🎤 Voice commands via Whisper STT
- 🧠 Local LLM reasoning (Ollama + Qwen 2.5)
- 🛠️ Tool execution (open apps, search web, manage notes)
- 🔒 Privacy-first: no cloud, all processing local
- 🎨 Clean architecture with extensible tool registry

## Architecture
[Simple ASCII diagram]

## Quick Start
```bash
pip install -r requirements.txt
ollama pull qwen2.5:7b
python main.py
```

## Supported Commands
- "Open YouTube"
- "Search web for weather"
- "Add a note: meeting at 3pm"
- "Set reminder to call mom at 6pm"

## Tech Stack
Python | Ollama | Whisper | pyttsx3 | LLM function-calling

## Challenges & Solutions
- GPU/CUDA initialization → Fallback to CPU-only mode
- Tool-calling reliability → Benchmarked models, chose Qwen 2.5
- STT accuracy → Upgraded from tiny.en to small.en

## Roadmap
- [ ] Wake word detection ("Hey Assistant")
- [ ] Conversation memory persistence
- [ ] Google Calendar integration
- [ ] Smart home control (Home Assistant)
- [ ] Background service with system tray

## License
MIT
