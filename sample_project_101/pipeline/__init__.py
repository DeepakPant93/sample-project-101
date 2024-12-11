"""

The `pipeline` module orchestrates the end-to-end flow of the data science process, from raw data ingestion to final predictions.
It consists of multiple submodules, each responsible for a specific stage in the pipeline. This modular structure ensures
scalability, reusability, and ease of maintenance. The pipeline is designed to handle data preprocessing, model training,
evaluation, and predictions in a systematic and automated manner.

Modules:
    Data-Ingestion: Collects and ingests raw data from various sources, performs basic checks, and stores it in a structured format.

    Data-Validation: Validates ingested data for correctness, completeness, and consistency, ensuring it meets predefined quality standards.

    Data-Transformation: Transforms validated data into a format suitable for model training, including feature engineering, scaling, encoding, and preprocessing.

    Model-Training: Trains machine learning models using transformed data, supports hyperparameter tuning, saving trained models, and logging metrics.

    Model-Evaluation: Evaluates trained models on a validation or test dataset, providing detailed performance metrics and insights.

    Prediction: Uses trained models to make predictions on new or unseen data, including batch or real-time inference and post-processing of predictions.

Features:
    - Modular architecture for each pipeline stage, ensuring maintainability and reusability.
    - Support for extensive logging and error handling at each stage.
    - Flexibility to customize and extend pipeline stages as needed.
    - Compatibility with various data formats and storage systems.

Usage:
    Import and use specific pipeline stages or run the entire pipeline end-to-end:

    Example:
        ```python
        from pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
        from pipeline.stage_04_model_trainer import ModelTrainingPipeline

        # Perform data ingestion
        data_ingestion = DataIngestionTrainingPipeline(config)
        raw_data = data_ingestion.run()

        # Train the model
        model_trainer = ModelTrainingPipeline(config, raw_data)
        trained_model = model_trainer.run()
        ```

Purpose:
    - To streamline the execution of a data science workflow, reducing manual intervention.
    - To ensure consistency and traceability of processes across multiple runs.
    - To provide reusable components for different machine learning projects.

"""
