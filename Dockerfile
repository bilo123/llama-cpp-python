FROM python:3.10-slim

# تثبيت curl والمتطلبات الأساسية
RUN apt-get update && apt-get install -y git build-essential cmake curl && \
    pip install --no-cache-dir llama-cpp-python flask

# إنشاء مجلد العمل
WORKDIR /app

# نسخ ملفات المشروع
COPY . .

# تحميل النموذج TinyLlama بصيغة GGUF Q4_0
RUN mkdir -p /models && curl -L -o /models/model.gguf https://huggingface.co/QuantFactory/Llama-3.2-3B-GGUF/resolve/main/Llama-3.2-3B.Q2_K.gguf

# بدء التطبيق
CMD ["python", "app.py"]
