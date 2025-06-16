import json
import os
from pathlib import Path

# Get the directory of the current script
current_dir = Path(__file__).parent

# Set the datadog.json's path relative to the current script
json_file_path = current_dir / "datadog.json"

try:
    # Load JSON data
    with open(json_file_path, "r") as file:
        DatadogTags = json.load(file)
except Exception as e:
    # Fallback definition if JSON loading fails
    DatadogTags = {
                    "STATUS": {
                        "INFO": "info",
                        "WARNING": "warning",
                        "ERROR": "error"
                    },
                    "SOURCES": {
                        "FRONTEND": "Frontend",
                        "BACKEND": "Backend",
                        "LAMBDA": "Lambda",
                        "SUMMARY_API": "Summary API",
                        "MULTIDEPO_API": "MultiDepo API"
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
                        "MULTIDEPO_API": {
                        "GENERATE_ANSWER": "Generate Answer / MultiDepo API",
                        "COMPARE_ANSWERS": "Compare Answers / MultiDepo API",
                        "UNAMED": "Unamed / MultiDepo API"
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
                        "MULTIDEPO": "MultiDepo / Backend",
                        "INVITATION": "Invitation / Backend",
                        "LABEL": "Label / Backend",
                        "MEDICAL": "Medical / Backend",
                        "USER": "User / Backend",
                        "NOTIFICATION": "Notification / Backend",
                        "ELASTICSEARCH": "Elasticsearch / Backend",
                        "CHANGESTREAM": "ChangeStream / Backend",
                        "USER_LOG": "User Log / Backend",
                        "UNAMED": "Unamed / Backend",
                        "ANNOTATION": "Annotation / Backend",
                        "TRACKER": "Tracker / Backend"
                        }
                    }
                }
