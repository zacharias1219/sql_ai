import streamlit as st
import google.generativeai as genai
from apikey import gemini_api_key

genai.configure(api_key=gemini_api_key)
model = genai.GenerativeModel('gemini-pro')

def main():
    st.set_page_config(page_title="SQL Query Generator", page_icon="🧠")
    st.markdown(
        """
            <div style = "text-align: center;">
                <h1> SQL Query Generator </h1>
                <h3> AI Assistant </h3>
                <p> This AI Assistant is designed to help you generate SQL queries. </p>
            </div>
        """,
            unsafe_allow_html=True
    )
    text_input = st.text_area("Enter your query here:")

    

    

    submit = st.button("Generate Query")
    if submit:
        with st.spinner("Generating your query..."):
            template = """
            Create a SQL query sinppet using the below text:
            ```
            {}
            ```
            Provide a sample tabular response with no explanation
            """.format(text_input)
            formatted_template = template.format(text_input)
            st.write(formatted_template)
            response = model.generate_content(formatted_template)
            sql_query = response.text
            st.write(sql_query)
    
main()