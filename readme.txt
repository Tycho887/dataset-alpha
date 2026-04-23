┌─────────────────┐
│  Stage 1: Load  │  ← File discovery + raw text extraction
└────────┬────────┘
         ▼
┌─────────────────────────┐
│  Stage 2: Heuristic     │  ← Fast rules (extensions, size, encoding)
│  Pre-Filter             │
└────────┬────────────────┘
         ▼
┌─────────────────────────┐
│  Stage 3: Zero-Shot     │  ← ML relevance classifier
│  Relevance Filter       │
└────────┬────────────────┘
         ▼
┌─────────────────────────┐
│  Stage 4: Data Cleaning │  ← NEW: Normalization, boilerplate removal,
│                         │      metadata extraction, language detection
└────────┬────────────────┘
         ▼
┌─────────────────────────┐
│  Stage 5: Smart Chunking│  ← Hierarchical + semantic chunking
│  + Deduplication        │      with heading context preservation
└────────┬────────────────┘
         ▼
┌─────────────────────────┐
│  Stage 6: Importance    │  ← NEW: Score chunks by information density
│  Scoring & Routing      │      Route "important" chunks to dual processing
└────────┬────────────────┘
         ▼
    ┌────┴────┐
    ▼         ▼
┌────────┐  ┌─────────────────────────┐
│Standard│  │  Stage 7: Dual-Process  │  ← Important chunks processed
│ Batch  │  │  (Independent + Group)  │      both solo AND in thematic groups
└───┬────┘  └────────────┬────────────┘
    │                    │
    └────────┬───────────┘
             ▼
    ┌─────────────────┐
    │  Stage 8: Async │  ← Concurrent API calls with quality filtering
    │  LLM Distillation│
    └─────────────────┘