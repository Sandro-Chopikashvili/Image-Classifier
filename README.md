# 🍓 Fruit Image Classifier

🎥 **Demo Video:**  
![Demo Video](Recording%202025-06-21%20133459.gif)

This is a multi-class image classification project that identifies different types of fruits using a pre-trained ResNet-18 model. The model is wrapped in a simple web interface built using **Flask**, with HTML and CSS used for front-end design.

## 🧠 Model Details

- **Model Architecture**: ResNet-18 (pre-trained on ImageNet)
- **Transfer Learning**: Final layer was fine-tuned on a custom fruits dataset.
- **Task**: Multi-class image classification (e.g., apple, banana, orange, etc.)
- **Dataset**: [Fruits-360](https://www.kaggle.com/moltean/fruits) or a custom fruit dataset

## 🌐 Web Interface

- **Backend**: Flask
- **Frontend**: HTML + CSS
- **Usage**: Upload a fruit image → get real-time prediction

## 🚀 How to Run

### 1. Clone the Repo
```bash
git clone https://github.com/yourusername/fruit-image-classifier.git
cd fruit-image-classifier
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Run the Flask App
```bash
python app.py
```

### 4. Open in Browser
Go to `http://127.0.0.1:5000` and upload a fruit image.

## 🖼️ Demo Screenshot

![Demo Screenshot](demo.png)  
*A simple interface to test your fruit classification model.*

## ⚙️ Technologies Used

- **PyTorch** - model training & inference
- **Torchvision** - pre-trained ResNet-18
- **Flask** - web framework
- **HTML/CSS** - user interface

## ✨ Future Improvements

- Show model confidence scores
- Add drag-and-drop support
- Deploy online via Render/Heroku

---

Feel free to customize the demo video, GitHub repo link, or deployment instructions!
