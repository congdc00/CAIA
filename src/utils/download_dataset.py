from huggingface_hub import snapshot_download
from huggingface_hub import HfApi
import os 
import argparse
import zipfile
from glob import glob

HF_TOKEN = os.environ.get("HF_TOKEN")
DATA_PATH = "data"

if __name__ == "__main__":
    
    parser = argparse.ArgumentParser(description='Download dataset from huggingface')
    parser.add_argument('--repo_id', type=str, required=True, help='Repo id of dataset on huggingface')
    parser.add_argument('--name_dataset', type=str, required=True, help='Name of dataset on local')
    args = parser.parse_args()
    
    api = HfApi(endpoint="https://huggingface.co", # Can be a Private Hub endpoint.
        token=HF_TOKEN)
    api.snapshot_download(repo_id=args.repo_id, local_dir=DATA_PATH, repo_type="dataset")

    data_path = os.path.join(DATA_PATH, args.name_dataset)
    list_files = glob(f"{data_path}/*")
    for file in list_files:
        if file.endswith(".zip"):
            extract_to_path = file.replace(".zip", "")
            with zipfile.ZipFile(file, 'r') as zip_ref:
                zip_ref.extractall(data_path)
        os.remove(file)