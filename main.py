import pyttsx3
import argparse


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("text", type=str, nargs="+")
    args = parser.parse_args()
    engine = pyttsx3.init()  # object creation

    """ RATE"""
    rate = engine.getProperty("rate")  # getting details of current speaking rate
    print(f"rate: {rate}")  # printing current voice rate
    engine.setProperty("rate", 125)  # setting up new voice rate

    """VOLUME"""
    volume = engine.getProperty(
        "volume"
    )  # getting to know current volume level (min=0 and max=1)
    print(f"volume: {volume}")  # printing current volume level
    engine.setProperty("volume", 1.0)  # setting up volume level  between 0 and 1

    """VOICE"""
    voices = engine.getProperty("voices")  # getting details of current voice
    # engine.setProperty('voice', voices[0].id)  #changing index, changes voices. o for male
    engine.setProperty(
        "voice", voices[1].id
    )  # changing index, changes voices. 1 for female

    print(args.text)
    engine.say(args.text)
    engine.runAndWait()
    engine.stop()


if __name__ == "__main__":
    main()
