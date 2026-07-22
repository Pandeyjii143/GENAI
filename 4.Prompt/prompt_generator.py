from langchain_core.prompts import PromptTemplate


template = PromptTemplate(
    template="""
Please summarize the research paper titled "{paper_input}" with the following specifications.

Explanation style:
{style_input}

Explanation length:
{length_input}

1. Mathematical Details:
- Include relevant mathematical equations if present.
- Explain them in simple language.
- Include code snippets where applicable.

2. Analogies:
- Use relatable analogies to explain complex ideas.

If certain information is unavailable, respond with
"Insufficient information available" instead of guessing.
""",
    input_variables=["paper_input","style_input","length_input"]
)

template.save('template.json')