# Upload to Hugging Face

**Target repo:** `CMiller/kbmill-brick-retrieval`  
**Local package:** this directory (`hf_datasets/vf-brick-retrieval/`)

## Prerequisites

```bash
pip install -U "huggingface_hub[cli]" datasets
huggingface-cli login   # paste a write token from https://huggingface.co/settings/tokens
huggingface-cli whoami  # must show CMiller56 (or your org)
```

## Create repo (once)

```bash
huggingface-cli repo create vf-brick-retrieval --type dataset --private false
# or with full name:
# huggingface-cli repo create CMiller/kbmill-brick-retrieval --type dataset
```

## Push files

From **this directory**:

```bash
cd /home/cmiller/Desktop/vf-brick-library/hf_datasets/vf-brick-retrieval

huggingface-cli upload CMiller/kbmill-brick-retrieval . . \
  --repo-type dataset \
  --commit-message "Initial VF brick retrieval demos (ArduPilot 20q + Skylab 15q)"
```

Or use the Python API:

```python
from huggingface_hub import HfApi
api = HfApi()
api.create_repo("CMiller/kbmill-brick-retrieval", repo_type="dataset", exist_ok=True)
api.upload_folder(
    folder_path=".",
    repo_id="CMiller/kbmill-brick-retrieval",
    repo_type="dataset",
    commit_message="Initial VF brick retrieval demos",
)
```

## Verify

```python
from datasets import load_dataset
c = load_dataset("CMiller/kbmill-brick-retrieval", "ardupilot_plane", split="corpus")
q = load_dataset("CMiller/kbmill-brick-retrieval", "ardupilot_plane", split="queries")
print(len(c), len(q), q[0])
```

Qrels: download `ardupilot_plane/qrels/test.tsv` from the dataset files tab (or clone the dataset repo).

## Rebuild after brick/eval changes

```bash
cd /home/cmiller/Desktop/vf-brick-library
python3 scripts/build_hf_retrieval_dataset.py
# then re-upload
```

## Do not upload

- Full portable ZIPs (stay on GitHub `vf-brick-library`)
- `embeddings.npy` (re-derive with nomic-embed-text for fair model comparison)
- Secrets / HF tokens
