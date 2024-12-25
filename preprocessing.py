import re

def preprocess_company_name(company_name):
    """
    Preprocesses the company name by removing common suffixes, extra spaces, and special characters.
    """
    if not company_name:
        return ""
    
    # Remove common suffixes
    company_name = re.sub(r'\b(LLC|Inc|Co|Corp|Ltd|Pvt|Limited)\b', '', company_name, flags=re.IGNORECASE)
    
    # Remove special characters and extra spaces
    company_name = re.sub(r'[^a-zA-Z0-9\s]', '', company_name).strip()
    company_name = re.sub(r'\s+', ' ', company_name)
    
    return company_name.lower()

def preprocess_city(city):
    """
    Preprocesses city names by normalizing case and removing special characters.
    """
    if not city:
        return ""
    return re.sub(r'[^a-zA-Z0-9\s]', '', city).strip().lower()
