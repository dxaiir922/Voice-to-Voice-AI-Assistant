import os
import cohere
from dotenv import load_dotenv

from RealtimeSTT import AudioToTextRecorder
from RealtimeTTS import TextToAudioStream, SystemEngine


def main():
   
    load_dotenv()

    api_key = os.getenv("COHERE_API_KEY")

    if not api_key:
        print("❌ لم يتم العثور على مفتاح Cohere")
        exit()

    co = cohere.Client(api_key)

    print("✅ Cohere Connected")


    engine = SystemEngine()
    stream = TextToAudioStream(engine)

    print("✅ TTS Ready")

    print("⏳ Creating Speech Recorder...")

    recorder = AudioToTextRecorder(
        model="small",
        language="ar"
    )

    print("✅ Recorder Ready")

    print("\n===================================")
    print("🎤 Voice AI Assistant Started")
    print("تحدث الآن...")
    print("===================================\n")

    while True:
        try:
            print("🎤 Listening...")

            text = recorder.text()

            if text.strip() == "":
                continue

            print(f"\n👤 You: {text}")

            response = co.chat(
                model="command-a-03-2025",
                message=text
            )

            reply = response.text

            print(f"\n Assistant: {reply}")

            stream.feed(reply)
            stream.play()

        except KeyboardInterrupt:
            print("تم إيقاف البرنامج")
            break

        except Exception as e:
            print("❌ Error:", e)


if __name__ == "__main__":
    main()
