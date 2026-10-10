# Fashion Product Recommender

A GenAI product recommender for apparel retail that supports contextual, natural-language queries such as *"Suggest apparels I can wear for a wedding in Jaipur"* — rather than keyword matching alone.

## Motivation

High return rates are a costly problem for apparel retailers, affecting revenue, customer satisfaction and sustainability. The average return rate for online apparel orders in the US is **24.4%**, against an estimated **$155.8 billion** online apparel and footwear market in 2023.

The two leading causes of returns are:

| Reason | Share of respondents |
|---|---|
| Size / fit | 53% |
| Colour | 16% |

Better recommendations at the point of discovery reduce the mismatch between what a customer expects and what arrives.

## How it works

Product descriptions are embedded into vectors and stored in a vector database, so retrieval becomes a nearest-neighbour search in semantic space instead of a literal text match.

**Text similarity** uses **cosine similarity** — the cosine of the angle between two vectors. Because it measures direction rather than magnitude, two descriptions are judged similar based on meaning, independent of how long the text is.

| File | Role |
|---|---|
| `embedding.py` | Generates embeddings with `HuggingFaceEmbedding` (`BAAI/bge-small-en-v1.5`) via LlamaIndex |
| `astradbvector.py` | Vector store operations against DataStax AstraDB |
| `createtables.py` | Schema / table setup |
| `styles.csv` | Product catalogue metadata |
| `AstraDB Vector data.xlsx`, `AstradB.xlsx` | Vector and catalogue data exports |

Archived components are included as zips: `Python Code`, `Front End` and `Vector Database`.

## Stack

- **Python**
- **LlamaIndex** — embedding interface
- **Hugging Face** — `BAAI/bge-small-en-v1.5` text embeddings, and image-similarity models
- **DataStax AstraDB** — vector storage and similarity search

## Running it

```bash
pip install llama-index llama-index-embeddings-huggingface
python embedding.py
```

AstraDB access requires your own database credentials and an application token; configure these before running `astradbvector.py` or `createtables.py`.

## Notes

- `bge-small-en-v1.5` is a compact English embedding model — a good speed/quality trade-off, but it will not handle non-English product text well.
- `embedding.py` currently runs against a short hardcoded list of product descriptions as a demonstration; point it at `styles.csv` to embed the full catalogue.
- Several components are committed as zip archives rather than extracted source, so they are not browsable or diffable on GitHub.
