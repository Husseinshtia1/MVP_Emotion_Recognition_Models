
import torch
from torchvision.models import resnet18
from torchvision.transforms import functional as TF
from PIL import Image

# Enable GPU inference if available
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model = resnet18(pretrained=True).to(device).eval()

def infer_on_image(image_path):
    image = Image.open(image_path)
    input_tensor = TF.to_tensor(TF.resize(image, (224, 224))).unsqueeze(0).to(device)
    with torch.no_grad():
        output = model(input_tensor)
    _, predicted = torch.max(output, 1)
    return "Deepfake Detected" if predicted.item() == 1 else "Authentic Video"
