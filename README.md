# CompostGuru

**DSCP Capstone Project Group 1**

CompostGuru is an end-to-end composting assistant built as part of the Ngee Ann Polytechnic Data Science Capstone Project. It integrates real-time sensor monitoring, machine-learning predictions, and AI-driven guidance to help urban farmers and gardeners optimize their composting process.

## Key Features

- **Real-time Sensor Dashboard**  
  Collects and displays moisture, pH, and EC readings from your compost pile.

- **Maturity Prediction API**  
  A FastAPI-powered `/predict` endpoint that uses a pre-trained model to estimate compost maturity from your latest sensor data.

- **Interactive CompostBot**  
  A Telegram bot built with python-telegram-bot that:
  - Displays current compost conditions  
  - Provides data-driven maturity forecasts  
  - Offers best-practice tips  
  - Engages in AI-powered composting Q&A via Replicate’s Llama-3 model

- **Automated CI/CD**  
  GitHub Actions pipelines for continuous integration (linting, testing) and future deployment workflows.

## Tech Stack

- **Backend & API**: FastAPI, Uvicorn  
- **Machine Learning**: scikit-learn (pickled `compost_model.pkl`), NumPy  
- **Chatbot**: python-telegram-bot v22, Replicate Llama-3  
- **DevOps**: GitHub Actions (CI), placeholder for AWS Elastic Beanstalk/ECS/Lambda  
- **Language**: Python 3.11
