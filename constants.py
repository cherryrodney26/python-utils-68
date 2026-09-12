"""Common constants for general utility operations."""

# Time conversions in seconds
SEC_IN_MINUTE = 60
SEC_IN_HOUR = 3600
SEC_IN_DAY = 86400
SEC_IN_WEEK = 604800

# Common file size limits in bytes
KB_TO_BYTES = 1024
MB_TO_BYTES = 1024 * 1024
GB_TO_BYTES = 1024 * 1024 * 1024

# Datetime formatting strings
ISO_8601_FORMAT = "%Y-%m-%dT%H:%M:%SZ"
SIMPLE_DATE_FORMAT = "%Y-%m-%d"
HUMAN_DATETIME_FORMAT = "%B %d, %Y, %I:%M %p"

# Common regex validation patterns as strings
EMAIL_PATTERN = "^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+[.][a-zA-Z]{2,}$"
URL_PATTERN = "^https?://[a-zA-Z0-9.-]+[.][a-zA-Z]{2,}(/.*)?$"

# Common HTTP status codes
HTTP_OK =