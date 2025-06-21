import torch
import torchvision.models as models
from flask import Flask, render_template, request
from torchvision import transforms
from PIL import Image
import json
import os

app = Flask(__name__)
device = torch.device('cpu')


torch.serialization.add_safe_globals([models.resnet.ResNet])

model = torch.load('model/model.pth', map_location=device, weights_only=False)
model.eval()

with open('model/class_to_idx.json', 'r') as f:
    class_to_idx = json.load(f)

idx_to_class = {v: k for k, v in class_to_idx.items()}

transform = transforms.Compose([
    transforms.Resize((224, 224)),
    transforms.ToTensor(),
    transforms.Normalize(
        mean=[0.485, 0.456, 0.406],
        std=[0.229, 0.224, 0.225]
    )
])

@app.route('/', methods=['GET', 'POST'])
def index():
    label = None

    if request.method == 'POST':
        img = request.files['image']
        image = Image.open(img).convert('RGB')
        image = transform(image).unsqueeze(0).to(device)

        with torch.no_grad():
            outputs = model(image)
            _, predicted = torch.max(outputs, 1)
            label = idx_to_class[predicted.item()]

        return render_template('index.html', label=label)

    return render_template('index.html', label=label)

if __name__ == '__main__':
    app.run(debug=True)



