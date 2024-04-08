

# Llama2 Medical Bot using Langchain    

The LLM based Medical Bot is a sophisticated tool engineered to deliver medical information by responding to user inquiries using advanced language models and vector stores. The Bot is made using Llama2 along with langchain and additional necessary components.



## Installation

1. Clone this repository to your local machine.

    ```bash
    git clone https://github.com/Atharva-Shetty/Medical-Chatbot-using-Langchain-and-LLama2.git
    cd Medical\ Chatbot\ using\ LLM\(Llama2\)/

    ```

2. Create a Python virtual environment (optional but recommended):

    ```bash
    pip install virtualenvwrapper
    virtualenv chatbot-env
    source chatbot-env/bin/activate  
    ```

3. Install the required Python packages:

    ```bash
    pip install -r requirements.txt
    ```

4. Obtain the necessary language models and data by following the guidelines provided in the Langchain documentation. Additionally, configure the paths and settings within your project, including the 'DATABASE_FAISS_PATH' variable, to suit your requirements.

## Getting Started

Follow the Steps to run the project:

1. Make sure your install required necessities according to [Langchain documentation](https://python.langchain.com/docs/integrations/vectorstores/faiss/).

2. Customize your project by adjusting the DATABASE_FAISS_PATH variable and any other specific configurations within the code.


3. Prepare the Langchain model according to documentation. 

4. You can train the bot using the injest.py file provided and changed the feeded PDF according.

5. Now to run the project

    ```bash
    streamlit run model.py
    ```

## Usage

1. The chatbot is proficient in responding to medical-related inquiries based on its training.

2. The training data can be provided in the form of a PDF document.

3. The chatbot's training data can be modified to tailor its responses to different topics, such as sports-related queries.

4. In cases where the chatbot is uncertain about an answer, it will refrain from providing false information and will only respond to queries it is confident about.



## Screenshots



## Technology Used

Langchain

Streamlit

Python

**LLM Model** : LLAMA2


 
