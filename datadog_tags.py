import json
import os
from pathlib import Path

# Set the datadog.json's path
datadog_submodule_path = "src/datadog/datadog.json"

# Convert the path to os-compatible
json_file_path = Path(datadog_submodule_path)

try:
    # Load JSON data
    with open(json_file_path, "r") as file:
        DatadogTags = json.load(file)
except Exception as e:
    DatadogTag = {
                    "STATUS": {
                        "INFO": "info",
                        "WARNING": "warning",
                        "ERROR": "error"
                    },
                    "SOURCES": {
                        "FRONTEND": "Frontend",
                        "BACKEND": "Backend",
                        "LAMBDA": "Lambda",
                        "SUMMARY_API": "Summary API"
                    },
                    "ENVIRONMENT": {
                        "PRODUCTION": "Production",
                        "STAGING": "Staging",
                        "DEVELOPMENT": "Development",
                        "LOCALHOST": "Localhost",
                        "LEXITAS_PRODUCTION": "Lexitas Production",
                        "LEXITAS_DEVELOPMENT": "Lexitas Development"
                    },
                    "SERVICES": {
                        "SUMMARY_API": {
                        "SUMMARY": "Summary / Summary API",
                        "ADMISSIONS": "Admissions / Summary API",
                        "CONTRADICTIONS": "Contradictions / Summary API",
                        "UNAMED": "Unamed / Summary API"
                        },

                        "LAMBDA": {
                        "DATA_INPUT": "Data Input / Lambda",
                        "PARSE_TRANSACTION": "Parse Transaction / Lambda",
                        "CONVERT_PDF_TO_TXT": "Convert PDF to TXT / Lambda",
                        "CONVERT_MDB_TO_TXT": "Convert MDB to TXT / Lambda",
                        "GENERATE_PDF": "Generate PDF / Lambda",
                        "UNAMED": "Unamed / Lambda"
                        },

                        "FRONTEND": {
                        "APOLLO_CLIENT": "Apollo Client / Frontend",
                        "NEXT_AUTH": "Next Auth / Frontend",
                        "UNAMED": "Unamed / Frontend"
                        },

                        "BACKEND": {
                        "RESTFUL_API": "Restful API / Backend",
                        "GRAPHQL_API": "GraphQL API / Backend",
                        "AUTH": "Auth / Backend",
                        "CASE": "Case / Backend",
                        "COMPANY": "Company / Backend",
                        "DELETE_REQUEST": "Delete Request / Backend",
                        "DEPO": "Depo / Backend",
                        "INVITATION": "Invitation / Backend",
                        "LABEL": "Label / Backend",
                        "MEDICAL": "Medical / Backend",
                        "USER": "User / Backend",
                        "UNAMED": "Unamed / Backend"
                        }
                    }
                }
