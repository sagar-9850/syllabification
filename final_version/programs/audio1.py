from pydub import AudioSegment
from pydub.playback import play

audiofile = 'sagar.wav'
start_ms = 1.5*1000#start of clip in milliseconds
end_ms = 2*1000#end of clip in milliseconds

sound = AudioSegment.from_file(audiofile, format="wav")
splice = sound[start_ms:end_ms]
play(splice)