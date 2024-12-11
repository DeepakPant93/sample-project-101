# sample-project-101

[![Release](https://img.shields.io/github/v/release/DeepakPant93/sample-project-101)](https://img.shields.io/github/v/release/DeepakPant93/sample-project-101)
[![Build status](https://img.shields.io/github/actions/workflow/status/DeepakPant93/sample-project-101/main.yml?branch=main)](https://github.com/DeepakPant93/sample-project-101/actions/workflows/main.yml?query=branch%3Amain)
[![Commit activity](https://img.shields.io/github/commit-activity/m/DeepakPant93/sample-project-101)](https://img.shields.io/github/commit-activity/m/DeepakPant93/sample-project-101)
[![License](https://img.shields.io/github/license/DeepakPant93/sample-project-101)](https://img.shields.io/github/license/DeepakPant93/sample-project-101)

A simple project with the DVC integration
This repository contains a sample Data Science application built with FastAPI, designed to streamline model training and prediction processes via RESTful APIs. The application leverages **Poetry** for dependency management, ensuring a robust and scalable development environment.

---

## Features

### FastAPI Endpoints:

-   `/train-model`: API endpoint to initiate model training with provided data and configurations.
-   `/predict`: API endpoint for generating predictions using the trained model.

### Poetry for Dependency Management:

-   Simplifies package installation and management.
-   Ensures compatibility and reproducibility of the project environment.

### Scalable Architecture:

-   Modular design with clear separation of concerns.
-   Easy integration of new features or pipelines.

---

## Prerequisites

-   Python >= 3.12
-   Poetry installed (`pip install poetry`)

---

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/DeepakPant93/sample-project-101.git
    cd sample-project-101
    ```

2. Install dependencies using Poetry:

    ```bash
    poetry install
    ```

3. Activate the virtual environment:

    ```bash
    poetry shell
    ```

4. Run the FastAPI server:

    ```bash
    uvicorn src.main:app --reload
    ```

---

## API Endpoints

### `/train-model`

-   **Method**: POST
-   **Description**: Triggers the model training process using provided training data and configuration.
-   **Input**: JSON object containing training data and optional hyperparameters.
-   **Output**: Success or error message indicating the status of training.

### `/predict`

-   **Method**: POST
-   **Description**: Generates predictions for new data using the trained model.
-   **Input**: JSON object containing features for prediction.
-   **Output**: Prediction results, including probabilities or class labels.

---

## Project Structure

```plaintext
src/
├── config/          # Configuration files and settings
├── components/      # Reusable components for the application
├── constants/       # Static constants and enumerations
├── entity/          # Definitions of data models and schemas
├── exception/       # Custom exception classes for error handling
├── logger/         # Logging setup for the application
├── pipeline/        # Data science pipeline modules (ingestion, validation, training, etc.)
├── routes/          # API route definitions
├── utils/           # Utility functions (e.g., file handling, data encoding)
└── main.py          # Entry point for the FastAPI application
```

---

Enjoy building with this Data Science FastAPI application! 🚀
