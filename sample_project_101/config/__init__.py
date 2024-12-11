"""

This module centralizes all configuration settings for the project, ensuring
consistent and maintainable configuration management. It provides access to
environment variables, default settings, and other configurations required
across different parts of the application.

Modules:
    env_config: Handles environment-specific configurations, such as development, testing, and production settings.
    app_config: Contains application-wide constants, such as API keys, logging settings, and feature flags.
    db_config: Stores database connection settings, including connection strings and timeout durations.

Usage:
    Import the required configuration settings as needed:

    Example:
        ```python
        from config.env_config import ENVIRONMENT, DEBUG_MODE
        from config.db_config import DATABASE_URL
        ```

Features:
    - Simplifies access to configuration values across the project.
    - Ensures separation of environment-specific settings from the codebase.
    - Supports overriding default settings via environment variables.

Purpose:
    - Provides a centralized location for all project settings to improve maintainability.
    - Makes it easier to adapt the application to different environments or deployment scenarios.
"""
