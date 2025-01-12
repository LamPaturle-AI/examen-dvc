# Change directory to project directory
cd /Users/lampaturle/Desktop/SWITCH_PROJECT/Datascientest/examen-dvc

# Create new virtual environnement
mamba create -n dsdvcexam python=3.9

# Activate virtual environnement
mamba activate dsdvcexam

# Install dvc
pip install dvc

# Initialize dvc
dvc init

# Install AWS s3
pip install "dvc[s3]"

# Add a DagsHub DVC remote
dvc remote add origin s3://dvc
dvc remote modify origin endpointurl https://dagshub.com/LamPaturle-AI/examen-dvc.s3

# Setup credentials
dvc remote modify origin --local access_key_id 8a08ba4d3a9988a7f9c1664a9c97b2354641694d
dvc remote modify origin --local secret_access_key 8a08ba4d3a9988a7f9c1664a9c97b2354641694d

# Setup default origin
dvc remote default origin

# Add data/raw/raw.csv to dvc
dvc add data/raw/raw.csv

# Track the changes with git
git add data/raw/raw.csv.dvc data/raw/.gitignore

# Push to DVC
dvc push

# Add stage 1
dvc stage add -n split \
              -d src/data/data_split.py -d data/raw \
              -o data/processed \
              python src/data/data_split.py
dvc repro

# Track new files on git
git add dvc.yaml
git add dvc.lock

# Add data/processed to dvc
dvc add data/raw

# Track the changes with git
git add data/raw.dvc data/.gitignore

# Push to DVC
dvc push

# Add stage 2
dvc stage add -n normalize \
              -d src/data/normalize.py -d data/processed \
              -o data/processed \
              python src/data/normalize.py
dvc repro

# Add stage 3
dvc stage add -n grid_search \
              -d src/models/grid_search.py -d data/processed \
              -o models \
              python src/models/grid_search.py
dvc repro

# Add stage 4
dvc stage add -n train \
              -d src/models/training.py -d data/processed \
              -o models \
              python src/models/training.py
dvc repro

# Add stage 5
dvc stage add -n evaluate \
              -d src/data/evaluate.py -d data/processed -d models \
              -o processed -o metrics \
              python src/data/evaluate.py
dvc repro

# Install libraries
pip install pandas
pip install sklearn

# Install pipreqs
pip install pipreqs 

# Generate minimal requirements.txt
pipreqs /examen-dvc --force

# Remove virtual environment
mamba remove -n dsdvcexam --all
