
import torch
from torchvision.models import resnet18
from torchvision.transforms import functional as TF
from PIL import Image
import matplotlib.pyplot as plt

# Load pre-trained ResNet model
model = resnet18(pretrained=True)
model.eval()

def visualize_saliency(image_path):
    image = Image.open(image_path)
    input_tensor = TF.to_tensor(TF.resize(image, (224, 224))).unsqueeze(0)

    input_tensor.requires_grad_()
    output = model(input_tensor)
    score = output.max()
    score.backward()
    
    saliency, _ = torch.max(input_tensor.grad.data.abs(), dim=1)
    saliency = saliency[0].numpy()

    plt.imshow(saliency, cmap='hot')
    plt.colorbar()
    plt.title("Saliency Map - Explainability")
    plt.show()
