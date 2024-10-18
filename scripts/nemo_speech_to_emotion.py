
import nemo.collections.asr as nemo_asr

asr_model = nemo_asr.models.ASRModel.from_pretrained('stt_en_conformer_ctc_large')

def transcribe_audio_and_detect_emotion(audio_file):
    transcription = asr_model.transcribe([audio_file])[0]
    print(f'Transcription: {transcription}')
