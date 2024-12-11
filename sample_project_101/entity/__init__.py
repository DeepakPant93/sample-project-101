"""

This module defines the core entities and data structures used throughout the
data science pipeline. Entities are designed to represent the inputs, outputs,
and intermediate states of the model training and prediction processes, ensuring
consistency and validation across the project.

Modules:
    data_schema: Contains definitions for input data schemas, ensuring validation and compatibility with the pipeline.
    model_params: Defines structures for storing model parameters, hyperparameters, and configuration settings.
    prediction_result: Provides entities for representing and managing prediction outputs, including probabilities and metadata.

Usage:
    Import and use the required entities in your data science pipeline:

    Example:
        ```python
        from entity.data_schema import InputSchema
        from entity.model_params import ModelConfig
        from entity.prediction_result import PredictionOutput
        ```

Features:
    - Defines standardized data structures for inputs, outputs, and parameters.
    - Ensures validation and consistency in data passed through the pipeline.
    - Promotes maintainability and readability by using clear, reusable entities.

Purpose:
    - Serves as a single source of truth for defining data structures in the pipeline.
    - Facilitates seamless integration between different stages of the pipeline,
      such as data ingestion, validation, model training, and prediction.
    - Improves error handling by validating data early in the process.

Examples:
    - **Data Schema**: Define the expected input structure for data preprocessing.
    - **Model Parameters**: Store configurations like learning rate, batch size,
      and optimizer type.
    - **Prediction Results**: Represent the model's outputs in a structured format,
      including predicted classes, probabilities, and confidence scores.
"""
