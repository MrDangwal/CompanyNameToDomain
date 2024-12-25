import re
from urllib.parse import urlparse
from fuzzywuzzy import fuzz
from preprocessing import preprocess_company_name

def extract_unique_domains(links):
    """
    Extracts unique domains from links, removing duplicates.
    """
    domains = set()
    for link in links:
        try:
            domain = urlparse(link).netloc
            if domain:
                domains.add(domain.lower())
        except Exception:
            continue
    return list(domains)

def get_most_similar_domain(company_name, domains):
    """
    Finds the domain with the highest similarity score to the company name.
    """
    company_name_clean = preprocess_company_name(company_name)
    best_match = None
    highest_score = 0
    
    for domain in domains:
        # Remove 'www.' and evaluate similarity
        domain_clean = re.sub(r'^www\.', '', domain)
        score = fuzz.partial_ratio(company_name_clean, domain_clean)
        
        # Boost score for exact or substring matches
        if company_name_clean in domain_clean:
            score += 50

        if score > highest_score:
            highest_score = score
            best_match = domain

    return best_match if highest_score > 50 else None  # Return None if no reliable match is found
