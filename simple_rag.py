# simple_rag.py

from google import genai
from google.genai import types
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from langchain.prompts import PromptTemplate
import datetime

# Setting
# gemini api key を環境変数で設定
# Windows powershelllでは、$env:GEMINI_API_KEY="xxxx" 
db_name = 'vectorstore.db'
faiss_max_its = 5
system = "あなたは優秀な大学図書館員です"

# query input
print('your request > ', end="")
query = input()

# vectorstore search
embeddings = HuggingFaceEmbeddings(
    model_name = "intfloat/multilingual-e5-large"
)
db = FAISS.load_local(db_name, embeddings, allow_dangerous_deserialization=True)
documents = db.similarity_search(query, k=faiss_max_its)

# Make prompt
documents_string = ""
for document in documents:
    documents_string += f"""
----
{document.page_content}
"""

prompt = PromptTemplate(
    template="""
#指示
文書を元に自身の知識も使って、質問への回答文をフォーマットに沿って生成してください。

#文書:
{document}

#質問:
{query}

#フォーマット:
- 質問についてのMarkdown形式による回答
- タイトルは質問文とする
- 回答に適切な参考資料があれば提示
""",
    input_variables=["document", "query"]
)
contents = prompt.format(document=documents_string, query=query)

# Goole AI Studio 
client = genai.Client()
config = types.GenerateContentConfig(
    system_instruction=system,
)
response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents=contents,
    config=config,
)

# Display 
print(response.text)

# File output
now = datetime.datetime.now()
output_file = './answer_' + now.strftime('%Y%m%d%H%M%S') + '.md'
with open(output_file, 'w', encoding='utf-8') as file:
    file.write(response.text)
