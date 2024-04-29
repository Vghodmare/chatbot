import streamlit as st
from langchain import HuggingFaceHub , PromptTemplate , LLMChain
import os

os.environ['API_KEY']='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'

st.set_page_config(page_title='Book Recommendation App')
st.title('Book Recommendation App')
txt_input = st.text_area('Enter Topic:','',height=20)
def generate_response(input):
    # write a code to generate response from LLM chain
    falcon_llm = HuggingFaceHub(huggingfacehub_api_token=os.environ['API_KEY'],
                           repo_id='tiiuae/falcon-7b-instruct',
                           model_kwargs={'temperature':0.6,'max_new_tokens':500})
    
    template = ''' I want to learn or read {queston} , please recommand me some books'''
    prompt =PromptTemplate(template=template, input_variables=['question'])
    falcon_chain = LLMChain(prompt=prompt , llm=falcon_llm , verbose=True)
    output = falcon_chain.run(input)
    return output


# form to accept user's text input for summarization
result = []
with st.form('summarize_form', clear_on_submit=True):
    submitted = st.form_submit_button('Submit')
    if submitted :
        with st.spinner('AI is Thinking ...'):
            response = generate_response(txt_input)
            result.append(response)
if len(result):
    st.info(response)