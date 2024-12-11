__version__ = "0.0.1"

"""
This project is a Data Science application built with FastAPI, designed to facilitate model training, prediction, and data processing. The application uses Poetry for dependency management and follows modular design principles to ensure scalability and maintainability.

Modules:
    configuration: Contains configuration settings for the application, including environment variables, paths, and system-specific configurations.
    component: Includes reusable components and helper classes for various processes, such as data manipulation and interaction with external services.
    constant: Defines constant values, enumerations, and other static data used throughout the application.
    utils: Contains utility functions that perform common tasks such as reading and writing files, processing images, and other system operations.
    pipeline: Implements the core stages of the data science pipeline, including data ingestion, validation, transformation, model training, and evaluation.
    routes: Defines the FastAPI routes for triggering model training, making predictions, and providing health checks for the application.

Features:
    - Model training and prediction workflows via FastAPI.
    - Modular and extensible design to add new features.
    - Dependency management with Poetry.
    - Built for data scientists and developers working with machine learning models in production environments.

This application is designed to help automate and streamline the workflow of training machine learning models and making predictions via an API interface, with easy-to-understand routes and clear separation of concerns between different modules.
"""
