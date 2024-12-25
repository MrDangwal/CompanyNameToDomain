from urllib.parse import urlparse
from fuzzywuzzy import fuzz
from preprocessing import preprocess_company_name

def extract_relevant_links(company_name, links, platforms):
    """
    Extracts links for specific platforms relevant to the company name.
    """
    company_name_clean = preprocess_company_name(company_name)
    relevant_links = {}

    for platform in platforms:
        platform_links = [link for link in links if platform in link.lower()]
        best_link = None
        highest_score = 0
        
        for link in platform_links:
            # Match company name with the path or subdomain
            link_path = urlparse(link).path.lower()
            link_domain = urlparse(link).netloc.lower()
            score = fuzz.partial_ratio(company_name_clean, link_path + link_domain)
            
            if score > highest_score:
                highest_score = score
                best_link = link
        
        if best_link:
            relevant_links[platform] = best_link

    return relevant_links
