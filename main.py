import os
from gtts import gTTS
import argparse

parser = argparse.ArgumentParser(description='text')
parser.add_argument('text',type=str)
args = parser.parse_args()

mytext = args.text

language="en"

myobj = gTTS(text=mytext, lang=language, slow=False)

myobj.save("./tmp.mp3")

os.system("./tmp.mp3")
