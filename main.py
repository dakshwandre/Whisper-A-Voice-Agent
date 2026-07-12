"""
Entry point for the voice agent (v1: push-to-talk).
Press Enter, speak your command, and the agent will act on it and reply.

Type 'text' instead of pressing Enter to switch to keyboard input for testing
without a mic, or 'quit' to exit.
"""
from stt import listen_and_transcribe
from tts import speak
from agent_core import VoiceAgent


def main():
    agent = VoiceAgent()
    speak("Voice agent ready. Press Enter to talk.")

    while True:
        user_input = input("\nPress Enter to speak (or type 'text'/'quit'): ").strip().lower()

        if user_input == "quit":
            speak("Goodbye.")
            break
        elif user_input == "text":
            command = input("Type your command: ").strip()
        else:
            command = listen_and_transcribe()

        if not command:
            print("Didn't catch that, try again.")
            continue
        
        speak("Got it one moment")
        reply = agent.handle_command(command)
        speak(reply)


if __name__ == "__main__":
    main()
