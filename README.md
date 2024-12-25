Here's the updated `README.md` with the link to the app included:

---

# **Company Domain and Social Media Link Finder**

This project is a Streamlit-based web application that helps users find the best domain and social media links for companies based on their names and cities. It combines search results from **DuckDuckGo** and **Bing** to provide accurate and comprehensive results.

### **Live App**
You can access the app here: [Company Domain and Social Media Link Finder](https://companyname2domain.streamlit.app/)

---

## **Features**

- Upload a CSV file containing company names and cities.
- Input single or multiple company names directly into the app.
- Progress bar to track processing in real-time.
- Combines results from DuckDuckGo and Bing for better accuracy.
- Extracts:
  - Best-matching domain.
  - Social media links (Facebook, Instagram, LinkedIn, etc.).
- Download processed results as a CSV file.

---

## **How It Works**

1. **Search Engines**: The app searches DuckDuckGo and Bing for company-related links.
2. **Domain Extraction**: Extracts unique domains from search results and matches them with the company name.
3. **Social Media Links**: Identifies relevant social media links for platforms like Facebook, Instagram, LinkedIn, BBB, etc.
4. **Interactive Interface**: Users can upload files or input company names manually and view/download results.

---

## **Setup and Installation**

### Prerequisites
- Python 3.7 or higher
- pip (Python package manager)

### Clone the Repository
```bash
git clone https://github.com/yourusername/company-link-finder.git
cd company-link-finder
```

### Install Dependencies
Use the `requirements.txt` file to install all required packages:
```bash
pip install -r requirements.txt
```

### Start the Application
Run the Streamlit app:
```bash
streamlit run app.py
```

---

## **Project Structure**

```
.
├── app.py                # Streamlit frontend
├── main.py               # Backend logic for processing companies
├── search_engines.py     # Functions for DuckDuckGo and Bing search
├── domain_extraction.py  # Extract domains and match them with companies
├── platform_links.py     # Extract relevant social media links
├── preprocessing.py      # Preprocess company and city names
├── requirements.txt      # Required Python packages
├── README.md             # Project documentation
```

---

## **Usage**

### 1. **Upload File**
- Navigate to the **Upload File** section in the app.
- Upload a CSV file with the following columns:
  - `Company Name`
  - `City`
- Click **Process File** to generate results.

### 2. **Input Companies**
- Navigate to the **Input Companies** section in the app.
- Enter one or more company names, each on a new line. Optionally, add a city (e.g., `Company Name, City`).
- Click **Process Input** to generate results.

### Output
- The app will display a table with processed results, including:
  - `Best Domain`
  - Links for platforms like Facebook, Instagram, LinkedIn, etc.
- Use the **Download Processed File** button to save the results as a CSV.

---

## **Technologies Used**

- **Python**: Backend processing and logic.
- **Streamlit**: Interactive web application.
- **BeautifulSoup**: Parsing Bing search results.
- **DuckDuckGo Search API**: Fetching DuckDuckGo search results.
- **FuzzyWuzzy**: Matching company names with domains and social media links.
- **tqdm**: Progress bar for processing status.

---

## **Contributing**

1. Fork the repository.
2. Create a new branch:
   ```bash
   git checkout -b feature-name
   ```
3. Commit your changes:
   ```bash
   git commit -m "Add new feature"
   ```
4. Push to the branch:
   ```bash
   git push origin feature-name
   ```
5. Open a pull request.

---

## **License**

This project is licensed under the MIT License. See the `LICENSE` file for details.

---

## **Future Enhancements**
- Add more search engines like Google and Yahoo.
- Support for additional social media platforms (e.g., TikTok, Pinterest).
- Advanced NLP-based domain relevance scoring.

---

### **Contact**
For any questions or suggestions, feel free to reach out at **your.email@example.com**.

--- 

With the live app link, users can directly access and test the application without setting it up locally. Make sure the app remains live and accessible for users!
