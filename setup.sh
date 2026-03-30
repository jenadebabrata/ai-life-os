#!/bin/bash

echo "🚀 Setting up AI Life OS..."

cd backend

pip install -r requirements.txt

echo "📥 Pulling model..."
ollama pull llama3

echo "✅ Setup complete!"
echo "Run: uvicorn main:app --reload"
