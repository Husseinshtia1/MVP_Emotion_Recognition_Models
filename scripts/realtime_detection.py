
import asyncio
import websockets
import torch
from torchvision import models, transforms
from PIL import Image

# Load a pre-trained ResNet model for demo purposes
model = models.resnet18(pretrained=True)
model.eval()

async def detect_deepfake_realtime(websocket, path):
    async for message in websocket:
        image = Image.open(message).convert('RGB')
        preprocess = transforms.Compose([
            transforms.Resize((224, 224)),
            transforms.ToTensor()
        ])
        img_tensor = preprocess(image).unsqueeze(0)
        output = model(img_tensor)
        _, predicted = torch.max(output, 1)
        result = "Deepfake Detected" if predicted.item() == 1 else "Authentic Video"
        await websocket.send(result)

start_server = websockets.serve(detect_deepfake_realtime, "localhost", 6789)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
