import streamlit as st
import pandas as pd 
import numpy as np



# DB managament
import sqlite3
conn = sqlite3.connect('data/data3.sqlite')
c = conn.cursor()

# function to execute sql queries 
def sql_executor(raw_code):
    c.execute(raw_code)
    data = c.fetchall()
    return data

# function to format the sql console
def sql_console(unique_key):
    with st.container():
        with st.form(key=unique_key):
            raw_code = st.text_area("SQL code here")
            submit_code = st.form_submit_button("Execute query")
                
        with st.container():
            if submit_code:
                st.info("Query submitted")

                # results
                query_results = sql_executor(raw_code)
                # get the column names of returned query 
                cols = [column[0] for column in c.description]

                # create dataframe and pass column names
                query_df = pd.DataFrame(query_results, columns=cols)
                st.dataframe(query_df)

# dictionary 
authors = ['Name', 'Website', 'Bio']
country = ['Code,', 'Name,', 'Continent,', 'Region,', 'SurfaceArea,', 'IndepYear,', 'Population,', 'LifeExpectancy,', 'GNP,', 'GNPOld,', 'LocalName,', 'GovernmentForm,', 'HeadOfState,', 'Capital,', 'Code2']
countrylanguage = ['CountryCode,', 'Language,', 'IsOfficial,', 'Percentage']

# Main 
def main():

    menu = ["Home", "About"]
    choice = st.sidebar.selectbox("Menu", menu)

    if choice == "Home":

        # container
        with st.container():
            st.header("Story Setting")
            st.markdown("""
            When people turn 28, a temporary tattoo appears on their wrist for 48 hours with the name and last name of their soulmate. On Haven’s 28th birthday, they didn’t see a name, but a tattoo showing [clue].
            """)

            with st.expander("Click to reveal tattoo"):
                st.image("https://images.all-free-download.com/images/graphiclarge/flora_tattoo_template_black_white_handdrawn_3d_sketch_6843589.jpg")

            st.markdown("""
            Puzzled, Haven goes to the elders of the village to ask whether there is any precedent.
            
            The elders mention that if Haven received a clue, their soulmate also did. There is a way to understand based on the clue – but it will require some digging and to acquire a new skill to find the answer – Structured Query Language (a.k.a. SQL)! 
            They direct Haven to the library where they can find historical information of all soulmates who have been matched for the past 5 years in the entire country, which has been digitized and stored on a database.
            
            You have 48 hours to explore available data, and help Haven find their soulmate before it’s too late.
            
            The librarian hands Haven an entity relationship diagram (ERD), which serves as a “map” to understand the relationships between different tables, and how they connect to each other. Each table has a primary key and foreign key [explain]. 
            """)

            with st.expander("Click to reveal ERD"):
                st.image("https://www.guru99.com/images/1/100518_0621_ERDiagramTu1.png")

        st.header("Data Exploration")

        st.markdown("""Based on the ERD and available info, let's explore the data. Feel free to explore on your own by hiding guided questions and writing queries using the sql console, or follow the walkthrough below.""")

        hide_guidance = st.checkbox("Click here to hide guided questions.", value=False)

        if hide_guidance == True: 
            st.write("Use your SQL knowledge to figure it out!")
            sql_console("query_results0")    
            
        else: 
            # first 
            st.markdown("""
            Let's start with some questions to understand the data. 

            <h4>First, write a query below that shows how many rows are in the x table.</h4>
            """, unsafe_allow_html=True)

            sql_console("query_results1")

            with st.expander("See solution"):
                st.code("""select * from authors""")
            
            # second 
            st.markdown("""
            <h4>How many distinct values per column?</h4>
            """, unsafe_allow_html=True)

            sql_console("query_results2")

            with st.expander("See solution"):
                st.code("""select * from authors""")

            
            # expander
        #   with st.expander("Guided questions"):
                



    else:
        st.subheader("About")

if __name__ == '__main__':
    main()


