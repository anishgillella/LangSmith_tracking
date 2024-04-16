from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Set necessary environment variables
os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")
os.environ["LANGCHAIN_TRACKING_V2"] = "true"  # Enabling tracking for all LLM operations
os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY")

# Creating a prompt with a predefined format
prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful assistant. Please respond to the user request only based on the given context."),
    ("user", "Question: {question}\nContext: {context}")
])

# Setting up the model and output parser
model = ChatOpenAI(model="gpt-3.5-turbo")
output_parser = StrOutputParser()

# Creating a processing chain
chain = prompt | model | output_parser

# Question and context for the model
question = "Can you summarize the speech?"
context = """
Five areas in combination have been identified based on India's core competence; natural resources and talented manpower for integrated action to double the growth rate of GDP and realize the Vision of Developed India. These are (1) Agriculture and food processing - with a target of doubling the present production of food and agricultural products by 2020. Agro food processing industry would lead to the prosperity of rural people, food security and speed up the economic growth (2) Infrastructure with reliable and quality electric power including solar farming for all parts of the country, Providing Urban amenities in Rural Areas (PURA) and Interlinking of Rivers (3) Education and Healthcare - to provide social security and eradication of illiteracy and health for all (4) Information and Communication Technology(ICT) - this is one of our core competencies and wealth generator. ICT can be used for Tele-Education, Tele-Medicine and E-Governance to promote education in remote areas, healthcare and also transparency in the administration. (5) Critical technologies and Strategic industries witnessed the growth in nuclear technology, space technology and defence technology. These five areas are closely inter-related. Since the theme of the IITF this year is "Tourism" and "Small and medium scale industries", which can be derived from the above areas, I would like to dwell on the role, these sectors can reinforce the national development in particular the rural development.

Tourism

The vast civilisational heritage of our country, ranging from the Himalayas to Kanyakumari, J&K, Central India, North Eastern states, Bihar, Western States, the large coastal line, Andaman Nicobar and Lakshadeep Islands, have a lot to attract the tourists. In spite of this vast potential, Indian tourism appears to have a very small market share of 0.38% with total arrivals of 2.64 million in the overall global scenario. This can certainly be increased keeping in mind India's unique positioning as a multi-dimensional country with many tourist attractions.

After my visit to almost all the regions of the country, I have realised that the tourism industry has a tremendous prospect for wealth generation and should operate as a mission with higher targets. To succeed in this mission tourism has to be developed and promoted as a common endeavour by all concerned Government as well as private sector agencies. A constructive partnership between the private and public sectors has to be established and sustained for growth. We need to establish innovative products and world-class infrastructure. Thrust is required to be given for inland water navigation, hotels, communication, entertainment and tourist promotion. The private sector and the State and Central Government agencies have to work together to create the right environment and act as proactive facilitators and catalysts to promote sustainable tourism. Tourist management leaders should be trained to create a people friendly approach among the tourists so that he/she becomes a promoter of business through word of mouth and experience sharing. The places of tourist interest have to be maintained and kept neat and tidy to provide a harmonious atmosphere to the tourists. The people of the region have to have moral strength to welcome the tourist with happiness. We have to start a "Welcome Tourist" movement. The Indianness has to be packaged from the time the tourist enters into the country till he departs in all aspects of his life during the stay.
"""

# Correctly passing the question and context into a single dictionary
result = chain.invoke({"question": question, "context": context})

# Printing the result
print(result)
