import asyncio
import os
from lightrag import LightRAG
from lightrag.llm.ollama import ollama_model_complete, ollama_embed
from lightrag.utils import EmbeddingFunc

WORKING_DIR = "./lightrag_workspace"
CORPUS_DIR = "./subset_corpus"
OLLAMA_HOST = "http://localhost:11434"

os.makedirs(WORKING_DIR, exist_ok=True)

async def build_rag():
    rag = LightRAG(
        working_dir=WORKING_DIR,
        llm_model_func=ollama_model_complete,
        llm_model_name="qwen2.5:7b",
        llm_model_max_async=1,
        llm_model_kwargs={
            "host": OLLAMA_HOST,
            "options": {"num_ctx": 32768},
            "timeout": 900,
        },
        embedding_func=EmbeddingFunc(
            embedding_dim=1024,
            max_token_size=8192,
            func=lambda texts: ollama_embed.func(
                texts,
                embed_model="mxbai-embed-large",
                host=OLLAMA_HOST,
                timeout=300,
            ),
        ),
    )
    await rag.initialize_storages()
    return rag

async def index_corpus(rag):
    files = [f for f in os.listdir(CORPUS_DIR) if f.endswith("_corpus.txt")][:5]
    print(f"Found {len(files)} corpus files to index")

    for i, filename in enumerate(files):
        path = os.path.join(CORPUS_DIR, filename)
        with open(path, "r", encoding="utf-8") as f:
            text = f.read()
        await rag.ainsert(text)
        print(f"[{i+1}/{len(files)}] Indexed {filename}")

    print("Indexing complete.")

async def main():
    rag = await build_rag()
    await index_corpus(rag)

if __name__ == "__main__":
    asyncio.run(main())    return rag

async def index_corpus(rag):
    files = [f for f in os.listdir(CORPUS_DIR) if f.endswith("_corpus.txt")][:5]
    print(f"Found {len(files)} corpus files to index")

    for i, filename in enumerate(files):
        path = os.path.join(CORPUS_DIR, filename)
        with open(path, "r", encoding="utf-8") as f:
            text = f.read()
        await rag.ainsert(text)
        print(f"[{i+1}/{len(files)}] Indexed {filename}")

    print("Indexing complete.")

async def main():
    rag = await build_rag()
    await index_corpus(rag)

if __name__ == "__main__":
    asyncio.run(main())
