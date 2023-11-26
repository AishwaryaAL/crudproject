import os
import gtts

text = "wellcome to python"
t1 = gtts.gTTS(text =text, lang='en', slow=False)
#os.remove("wellcome1.mp3")

t1.save("wellcome1.mp3")