
import torch
from torchvision import models, transforms
from PIL import Image

# Pre-trained ResNet model for demonstration purposes
model = models.resnet18(pretrained=True)
model.eval()

def detect_deepfake(image_path):
    img = Image.open(image_path)
    preprocess = transforms.Compose([
        transforms.Resize((224, 224)),
        transforms.ToTensor()
    ])
    img_tensor = preprocess(img).unsqueeze(0)
    output = model(img_tensor)
    _, predicted = torch.max(output, 1)
    return "Deepfake Detected" if predicted.item() == 1 else "Authentic Video"
