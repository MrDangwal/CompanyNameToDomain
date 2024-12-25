import requests
from bs4 import BeautifulSoup
from duckduckgo_search import DDGS

def duckduckgo_search(query, max_results=50):
    """
    Searches DuckDuckGo for the query and retrieves links.
    Includes fallback logic for refinement.
    """
    ddgs = DDGS()
    links = []
    try:
        results = ddgs.text(query, max_results=max_results)
        links = [result['href'] for result in results if 'href' in result]
        print(f"Found {len(links)} links from DuckDuckGo.")
    except Exception as e:
        print(f"DuckDuckGo search failed: {e}")
    
    # Fallback if no results are found
    if not links:
        fallback_query = f"{query} contact information"
        try:
            results = ddgs.text(fallback_query, max_results=max_results)
            links = [result['href'] for result in results if 'href' in result]
            print(f"Fallback search found {len(links)} links from DuckDuckGo.")
        except Exception as e:
            print(f"Fallback DuckDuckGo search failed: {e}")
    
    return links

def bing_search(query, max_results=50):
    """
    Searches Bing for the query and retrieves links.
    Includes fallback logic for refinement.
    """
    search_url = "https://www.bing.com/search"
    params = {"q": query, "count": max_results}
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36"}
    links = []
    
    try:
        response = requests.get(search_url, params=params, headers=headers)
        response.raise_for_status()  # Raise an HTTPError for bad responses (4xx and 5xx)
        soup = BeautifulSoup(response.text, "html.parser")
        
        # Extract links from search results
        for a_tag in soup.find_all("a", href=True):
            href = a_tag["href"]
            if "http" in href and "bing" not in href:  # Exclude Bing's internal links
                links.append(href)
        
        # Deduplicate links
        links = list(set(links))[:max_results]
        print(f"Found {len(links)} links from Bing.")
    except Exception as e:
        print(f"Bing search failed: {e}")
    
    # Fallback if no results are found
    if not links:
        fallback_query = f"{query} contact information"
        params["q"] = fallback_query
        try:
            response = requests.get(search_url, params=params, headers=headers)
            response.raise_for_status()
            soup = BeautifulSoup(response.text, "html.parser")
            for a_tag in soup.find_all("a", href=True):
                href = a_tag["href"]
                if "http" in href and "bing" not in href:
                    links.append(href)
            links = list(set(links))[:max_results]
            print(f"Fallback search found {len(links)} links from Bing.")
        except Exception as e:
            print(f"Fallback Bing search failed: {e}")
    
    return links

def combined_search(query, max_results=50):
    """
    Combines search results from DuckDuckGo and Bing.
    """
    duckduckgo_links = duckduckgo_search(query, max_results=max_results)
    bing_links = bing_search(query, max_results=max_results)
    
    # Merge and deduplicate results
    all_links = list(set(duckduckgo_links + bing_links))
    print(f"Total unique links from both search engines: {len(all_links)}")
    return all_links
