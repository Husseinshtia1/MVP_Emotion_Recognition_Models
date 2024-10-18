
import torch
from transformers import ViTModel, ViTFeatureExtractor
from PIL import Image

model = ViTModel.from_pretrained('google/vit-base-patch16-224-in21k')
feature_extractor = ViTFeatureExtractor.from_pretrained('google/vit-base-patch16-224-in21k')

def analyze_multiframe_video(frames):
    inputs = feature_extractor(images=frames, return_tensors='pt')
    outputs = model(**inputs)
    return outputs.last_hidden_state
