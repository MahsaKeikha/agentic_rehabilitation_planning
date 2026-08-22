# F60 Held-Out Reproducibility Results

Gold Standard validation was executed from a clean GitHub Actions checkout.

- Evidence run: `32564209392`
- Head: `56b128dbaaefd51eb6660afcd771ca77fc70d404`
- Python: 3.10, 3.11, 3.12 all green
- Held-out rehabilitation planning scenarios: 8/8 passed
- Pass rate: 1.0
- Artifact: `f60-heldout-results`
- Artifact digest: `sha256:cc7524551af45d041b911dc4971e7aeb0034fbcaa415920d143225d71dbdcb71`

The suite validates fail-closed handling for identity gaps, contraindication review, acute red flags, unsafe autonomous progression, new-treatment requests, assistive-device safety gaps, and missing qualified human approval. L3 denotes a reproducible reference implementation and does not grant autonomous clinical authority.
