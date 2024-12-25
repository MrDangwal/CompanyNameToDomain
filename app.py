import streamlit as st
import pandas as pd
from main import process_companies, process_single_company
from tqdm import tqdm

# Define platforms
PLATFORMS = ['facebook', 'instagram', 'linkedin', 'bbb', 'twitter', 'yelp']

st.title("Company Domain and Social Media Link Finder")

# Sidebar for navigation
st.sidebar.title("Navigation")
option = st.sidebar.selectbox("Choose a mode:", ["Upload File", "Input Companies"])

def process_with_progress(df, platforms):
    """
    Process companies with a progress bar in Streamlit.
    """
    results = []
    progress_bar = st.progress(0)  # Initialize the progress bar
    total = len(df)

    for idx, row in enumerate(df.iterrows()):
        _, row_data = row
        company_name = row_data['Company Name']
        city = row_data['City']
        
        try:
            best_domain, relevant_links = process_single_company(company_name, city, platforms)
            results.append({
                'Company Name': company_name,
                'City': city,
                'Best Domain': best_domain,
                **{f'{platform.capitalize()} Link': relevant_links.get(platform, None) for platform in platforms}
            })
        except Exception as e:
            results.append({
                'Company Name': company_name,
                'City': city,
                'Best Domain': None,
                **{f'{platform.capitalize()} Link': None for platform in platforms},
                'Error': str(e)
            })
        
        # Update progress bar
        progress = int((idx + 1) / total * 100)
        progress_bar.progress(progress)
    
    progress_bar.empty()  # Remove the progress bar when done
    return pd.DataFrame(results)

if option == "Upload File":
    st.header("Upload a CSV File")
    uploaded_file = st.file_uploader("Upload your CSV file here (must have 'Company Name' and 'City' columns):", type=["csv"])
    
    if uploaded_file is not None:
        df = pd.read_csv(uploaded_file)
        st.write("Uploaded File Preview:")
        st.write(df.head())

        if st.button("Process File"):
            st.write("Processing...")
            processed_df = process_with_progress(df, PLATFORMS)
            st.write("Processed Results:")
            st.dataframe(processed_df)
            
            # Option to download the results
            csv = processed_df.to_csv(index=False).encode('utf-8')
            st.download_button("Download Processed File", data=csv, file_name="processed_companies.csv", mime="text/csv")

elif option == "Input Companies":
    st.header("Input Company Details")
    company_input = st.text_area("Enter company names (one per line) and optionally a city in the format 'Company Name, City':")

    if st.button("Process Input"):
        if company_input.strip():
            # Split the input into lines and create a DataFrame
            lines = company_input.strip().split("\n")
            data = []
            for line in lines:
                if "," in line:
                    company, city = map(str.strip, line.split(",", 1))
                else:
                    company, city = line.strip(), ""
                data.append({"Company Name": company, "City": city})
            df = pd.DataFrame(data)

            st.write("Processing the following companies:")
            st.dataframe(df)

            processed_df = process_with_progress(df, PLATFORMS)
            st.write("Processed Results:")
            st.dataframe(processed_df)
            
            # Option to download the results
            csv = processed_df.to_csv(index=False).encode('utf-8')
            st.download_button("Download Processed Results", data=csv, file_name="processed_companies.csv", mime="text/csv")
        else:
            st.warning("Please enter at least one company name.")
