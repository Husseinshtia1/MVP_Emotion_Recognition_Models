
import torch
import torchvision.transforms as transforms
from PIL import Image
import cv2
from facenet_pytorch import InceptionResnetV1

# Load the model
model = InceptionResnetV1(pretrained='vggface2').eval()

def detect_deepfake(image):
    """Detects deepfake on a single image."""
    preprocess = transforms.Compose([
        transforms.Resize((224, 224)),
        transforms.ToTensor(),
        transforms.Normalize([0.5, 0.5, 0.5], [0.5, 0.5, 0.5])
    ])
    img_tensor = preprocess(image).unsqueeze(0)
    output = model(img_tensor)
    _, predicted = torch.max(output, 1)
    return "Deepfake Detected" if predicted.item() == 1 else "Authentic Video"

def detect_deepfake_in_video(video_path):
    """Performs frame-by-frame deepfake detection on a video."""
    cap = cv2.VideoCapture(video_path)
    frame_count = 0
    fake_frames = 0

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        # Convert frame to PIL Image and run detection
        image = Image.fromarray(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
        result = detect_deepfake(image)

        frame_count += 1
        if result == "Deepfake Detected":
            fake_frames += 1

    cap.release()
    fake_percentage = (fake_frames / frame_count) * 100
    return f"Fake content: {fake_percentage:.2f}% of the video."

def visualize_saliency(image_path):
    """Generates a saliency map for explainable AI."""
    image = Image.open(image_path).convert('RGB')
    input_tensor = transforms.ToTensor()(image).unsqueeze(0).requires_grad_(True)

    output = model(input_tensor)
    score = output.max()
    score.backward()

    saliency, _ = torch.max(input_tensor.grad.data.abs(), dim=1)
    saliency = saliency[0].numpy()

    # Display the saliency map
    cv2.imshow("Saliency Map", saliency)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
