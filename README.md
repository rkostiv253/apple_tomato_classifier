# Apple_tomato_classifier

A simple deep learning web application that classifies images as apple (0) or tomato (1) 
using a pretrained MobileNetV2 model and deploys it via Flask.

## Tech stack

- **Backend**: Python, Flask, Tensorflow
- **Frontend**: HTML, CSS

```
apple_tomato_classifier/
│
├── app.py
├── apple_tomato_classifier.keras
├── requirements.txt
│
├── templates/
│   ├── index.html
│   ├── apple.html
│   └── tomato.html
│
└── static/
    ├── apple.png
    └── tomato.png
```