"""

The `routes` module defines the API routes that enable interaction with the machine learning model.
This module contains endpoints for initiating model training and making predictions on new data.

Endpoints:
    - POST /train-model: This endpoint is responsible for triggering the model training process.
    - POST /predict: This endpoint is responsible for generating predictions using the trained model.


Features:
    - API endpoints for model training and prediction.
    - Flexible and easy-to-extend with additional routes.
    - Integration with the model training pipeline and prediction modules.
    - Handles input validation and error responses for robustness.
"""
