#how to make a speech to  text in python?

from pygsr import Pygsr
speech = Pygsr()
# duration in seconds
speech.record(3)
# select the language
phrase, complete_response = speech.speech_to_text('en_US')

print (phrase)


