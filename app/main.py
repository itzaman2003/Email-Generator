import streamlit as st
from langchain_community.document_loaders import WebBaseLoader
from chains import Chain
from portfolio import Portfolio
from utils import clean_text

def create_streamlit_app(llm, portfolio, clean_text):
    # Center the title using HTML
    st.markdown("<h1 style='text-align: center;'>📧 Mail Generator</h1>", unsafe_allow_html=True)
    
    # Input field for URL
    url_input = st.text_input("Enter a URL:", value="Enter the URL of the job posting")
    
    # Button to submit
    submit_button = st.button("Submit")
    
    if submit_button:
        try:
            # Load the web data
            loader = WebBaseLoader([url_input])
            data = clean_text(loader.load().pop().page_content)
            
            # Shorten the extracted data after user hits Enter
            shortened_data = data[:500]  # Adjust the length as necessary
            
            portfolio.load_portfolio()
            jobs = llm.extract_jobs(shortened_data)
            
            # Loop through jobs and generate email
            for job in jobs:
                skills = job.get('skills', [])
                links = portfolio.query_links(skills)
                email = llm.write_mail(job, links)
                
                # Display the generated email
                st.code(email, language='markdown')
        except Exception as e:
            st.error(f"An Error Occurred: {e}")

if __name__ == "__main__":
    chain = Chain()
    portfolio = Portfolio()
    
    # Set Streamlit page configuration
    st.set_page_config(layout="wide", page_title="Cold Email Generator", page_icon="📧")
    
    # Run the Streamlit app
    create_streamlit_app(chain, portfolio, clean_text)
