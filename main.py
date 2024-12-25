import pandas as pd
from search_engines import combined_search
from domain_extraction import extract_unique_domains, get_most_similar_domain
from platform_links import extract_relevant_links
from preprocessing import preprocess_company_name, preprocess_city

def process_single_company(company_name, city, platforms, max_results=20):
    """
    Processes a single company, extracting the best domain and platform links.
    """
    query = f'official website for {company_name} in {city}'
    links = combined_search(query, max_results=max_results)
    unique_domains = extract_unique_domains(links)
    best_domain = get_most_similar_domain(company_name, unique_domains)
    relevant_links = extract_relevant_links(company_name, links, platforms)
    return best_domain, relevant_links

def process_companies(df, platforms, max_results=20):
    """
    Processes a DataFrame, returning a DataFrame with the best domain and platform links.
    """
    results = []
    for _, row in df.iterrows():
        company_name = preprocess_company_name(row['Company Name'])
        city = preprocess_city(row['City'])
        
        try:
            best_domain, relevant_links = process_single_company(
                company_name, city, platforms, max_results=max_results
            )
            results.append({
                'Company Name': row['Company Name'],
                'City': row['City'],
                'Best Domain': best_domain,
                **{f'{platform.capitalize()} Link': relevant_links.get(platform, None) for platform in platforms}
            })
        except Exception as e:
            results.append({
                'Company Name': row['Company Name'],
                'City': row['City'],
                'Best Domain': None,
                **{f'{platform.capitalize()} Link': None for platform in platforms},
                'Error': str(e)
            })
    
    return pd.DataFrame(results)
