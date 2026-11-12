class ApexAPIError(Exception):
    """Base exception for Apex API client errors."""

class ApexAPIConnectionError(ApexAPIError):
    """Raised when the API server cannot be reached."""

class ApexAPITimeoutError(ApexAPIError):
    """Raised when an API request exceeds its timeout."""

class ApexAPIRequestError(ApexAPIError):
     """Raised for other HTTP client request failures."""

