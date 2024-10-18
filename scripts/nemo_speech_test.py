
import nemo.collections.asr as nemo_asr

asr_model = nemo_asr.models.ASRModel.from_pretrained('stt_en_conformer_ctc_large')

def test_speech_to_emotion(audio_path):
    try:
        transcription = asr_model.transcribe([audio_path])[0]
        print(f'Transcription: {transcription}')
    except Exception as e:
        print(f"Error during audio transcription: {e}")
