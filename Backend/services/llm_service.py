from langchain_google_genai import ChatGoogleGenerativeAI
from flask import jsonify

llm=ChatGoogleGenerativeAI(
    model="gemini-3-flash-preview",
    temperature=0.3
)

def generate_answer (question,relevant_docs):
    context="\n\n".join([
        doc.page_content for doc in relevant_docs
    ])

    prompt=f"""
    Answer the question only using the provided context.
    If the answer is not found in the context,
    say: "I could not find the answer in the document."

    Context:
    {context}

    Question:
    {question}
    """

    response=llm.invoke(prompt)

    return response.content[0]["text"]