# # def build_prompt(question, contexts):

# #     context_text = "\n\n".join([c["text"] for c in contexts])

# #     prompt = f"""
# # You are a helpful campus assistant.

# # Use ONLY the provided context to answer the question.

# # If the answer is clearly present in the context, provide the exact answer.

# # If the answer is NOT present in the context, say:
# # "I do not have enough information in the provided knowledge base to answer that."

# # Context:
# # {context_text}

# # Question:
# # {question}

# # Answer:
# # """

# #     return prompt
# def build_prompt(question, contexts):

#     context_text = "\n\n".join([c["text"] for c in contexts])

#     print("\n========= CONTEXT SENT TO LLM =========\n")
#     print(context_text)
#     print("\n=======================================\n")

#     prompt = f"""
# You are a campus assistant.

# Answer the question ONLY using the provided context.

# If the answer exists in the context, return it.

# If not, say:
# "I do not have enough information in the provided knowledge base to answer that."

# Context:
# {context_text}

# Question:
# {question}

# Answer:
# """

#     return prompt
def build_prompt(question, contexts):

    context_text = "\n\n".join([c["text"] for c in contexts])

    prompt = f"""
You are a helpful campus assistant.

Use ONLY the provided context to answer the question.

If the answer exists in the context, return it.

If the answer is NOT present in the context, say:
"I do not have enough information in the provided knowledge base to answer that."

Context:
{context_text}

Question:
{question}

Answer:
"""

    return prompt