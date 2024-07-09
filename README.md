# CAIA
Classification AI Art

Prerequisites
-------------  
- `CUDA 12.4`
- `Python 3.12`

Environment
-------------  
Run code here
```
pip3 install torch torchvision torchaudio
pip install -r requirements.txt
```

Preparing data for training   
-------------  
Setup Huggingface key 
```
export HF_TOKEN=<your_api_key>
```


Run code here to download data  
```
python -m src.utils.download_dataset --repo_id <repo_id> --name_dataset <name_dataset>
```

Our models are trained on CAIA dataset. See [here](https://huggingface.co/datasets/congdc/CAIA-dataset) for a few suggestions regarding training on other datasets. If want to use this dataset, set `repo_id` is `"congdc/CAIA-dataset"`  

Train
-------------  
Setup Wandb api key  

```
export WANDB_API_KEY=<your_api_key>
```
You can train with `notebooks/train.ipynb` 

Getting the weights  
-------------  

Download model from here

| Model  | Description |  Link to the model | 
| :-------------: | :---------------: | :---------------: |
| CAIA_b  | Base model | [Link](https://huggingface.co/congdc/CAIA-model)  |