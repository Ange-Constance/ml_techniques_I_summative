# Video Link: https://drive.google.com/file/d/1vM1VAtNFONBEh0unUnYTnotHmHlnSQIZ/view?usp=sharing
# Ezza — AI Agricultural Advisory Assistant

**Ezza** is a fine-tuned Large Language Model specialized in providing agricultural advisory support for farmers, agronomists, and agricultural stakeholders. It delivers actionable, climate-smart, and environmentally responsible recommendations on crop management, soil health, irrigation, fertilization, and pest control.

Ezza is built by fine-tuning **TinyLlama-1.1B-Chat** using **QLoRA (4-bit quantization)** on a custom high-quality agricultural dataset with over **5,000+ expert-style examples**.

---

# Project Overview

This project demonstrates end-to-end development of a domain-specialized AI assistant:

* ✅ Custom dataset generation (5,460+ examples)
* ✅ Fine-tuning TinyLlama using QLoRA (efficient low-VRAM training)
* ✅ Model evaluation using Perplexity, BLEU, and ROUGE metrics
* ✅ Deployment using Gradio interactive web interface
* ✅ Production-ready modular codebase

---

# Model Information

| Attribute          | Value                                                  |
| ------------------ | ------------------------------------------------------ |
| Base Model         | TinyLlama-1.1B-Chat                                    |
| Fine-tuning Method | QLoRA (4-bit quantization)                             |
| Training Framework | HuggingFace Transformers + PEFT                        |
| Dataset Size       | 5,460+ examples                                        |
| Domain             | Agriculture                                            |
| Specialization     | Crop management, soil health, pest control, irrigation |
| Deployment         | Gradio Web Interface                                   |

---

# Training Results

**Final Training Metrics:**

* Training Loss: **0.25**
* Perplexity: **2.65** (lower is better ✅)
* ROUGE-1: **0.31**
* ROUGE-L: **0.15**

These results indicate strong domain adaptation and coherent agricultural advisory responses.

---

# 📁 Project Structure

```
ezza-ai-assistant/
│
├── dataset/
│   └── ezza_dataset.json
│
├── training/
│   ├── train.py
│   ├── evaluate.py
│   └── qlora_config.py
│
├── inference/
│   ├── generate.py
│   └── load_model.py
│
├── app/
│   └── gradio_app.py
│
├── outputs/
│   └── ezza-final-model/
│
├── requirements.txt
└── README.md
```

---

# Installation

## 1. Clone repository

```bash
git clone https://github.com/yourusername/ezza-ai-assistant.git
cd ezza-ai-assistant
```

## 2. Create virtual environment

```bash
python -m venv ezza-env
source ezza-env/bin/activate
```

## 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

# Running Inference

```bash
python inference/generate.py
```

Example prompt:

```
My maize leaves are turning yellow. What should I do?
```

---

# Launch Web Interface (Gradio)

```bash
python app/gradio_app.py
```

Then open in browser:

```
http://localhost:7860
```

---

# Example Output

**User:**

> My cassava leaves have brown spots.

**Ezza:**

> Brown spots on cassava leaves may indicate fungal disease or nutrient deficiency.
>
> Recommended actions:
>
> 1. Remove infected leaves
> 2. Improve drainage
> 3. Apply balanced fertilizer
> 4. Monitor for pest activity
>
> Climate-smart tip: Use crop rotation to reduce disease pressure.

---

# Technologies Used

* Python 
* HuggingFace Transformers
* PEFT (QLoRA)
* BitsAndBytes (4-bit quantization)
* PyTorch
* Gradio
* JSON dataset

---

# Key Features

* Domain-specialized agricultural intelligence 
* Efficient fine-tuning using QLoRA 
* Low VRAM training capability 
* Interactive web interface 
* Production-ready structure 

---

# Author

**Ange Constance**

AI Engineer | Frontend Developer | Agricultural AI Researcher

