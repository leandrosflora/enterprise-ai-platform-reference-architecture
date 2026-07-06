# Knowledge Service

## Visão Geral

O Knowledge Service é responsável pela ingestão, preparação, indexação e recuperação de conhecimento corporativo para uso em fluxos RAG.

## Responsabilidades

- Receber documentos e fontes de conhecimento
- Extrair texto e metadados
- Aplicar chunking
- Gerar embeddings
- Indexar conteúdo no mecanismo vetorial
- Executar busca semântica e híbrida
- Retornar trechos com metadados e citações

## Pipeline de Ingestão

```text
Source
  ↓
Extraction
  ↓
Chunking
  ↓
Embedding
  ↓
Indexing
  ↓
Retrieval
```

## APIs

### Ingestão

```http
POST /knowledge-bases/{knowledgeBaseId}/documents
```

### Busca

```http
POST /knowledge-bases/{knowledgeBaseId}/search
```

### Request de Busca

```json
{
  "query": "política de crédito para pessoa jurídica",
  "topK": 5,
  "filters": {
    "domain": "credit",
    "classification": "internal"
  }
}
```

### Response de Busca

```json
{
  "results": [
    {
      "documentId": "doc-123",
      "chunkId": "chunk-456",
      "score": 0.91,
      "text": "Trecho recuperado...",
      "metadata": {
        "source": "policy-repository",
        "classification": "internal"
      }
    }
  ]
}
```

## Dependências

| Dependência | Uso |
|---|---|
| OpenSearch | Busca vetorial e híbrida |
| PostgreSQL | Metadados de knowledge bases e documentos |
| Foundation Models | Geração de embeddings |
| Kafka | Publicação de eventos de ingestão |
| Object Storage | Armazenamento de documentos originais |

## Eventos Publicados

- `knowledge.ingested`
- `embedding.generated`
- `document.indexed`

## Requisitos Não Funcionais

| Requisito | Diretriz |
|---|---|
| Segurança | Respeitar classificação da informação |
| LGPD | Evitar exposição indevida de dados pessoais |
| Rastreabilidade | Manter origem, versão e metadados do documento |
| Qualidade | Suportar reindexação e avaliação de retrieval |
| Escalabilidade | Processamento assíncrono de grandes volumes |

## Decisões Relacionadas

- [ADR-002 Vector Database Selection](../adr/ADR-002-vector-database-selection.md)
- [ADR-005 Evaluation Framework](../adr/ADR-005-evaluation-framework.md)
