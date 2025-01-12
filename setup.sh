# Change directory to project directory
cd /Users/lampaturle/Desktop/SWITCH_PROJECT/Datascientest/examen-dvc

# Create new virtual environnement
mamba create -n dsdvcexam python=3.9

# Activate virtual environnement
mamba activate dsdvcexam

# Install dvc
pip install dvc

# Initialize dvc
dvc init -f

# Install AWS s3
pip install "dvc[s3]"

# Add DagsHub DVC remote
dvc remote add origin s3://dvc
dvc remote modify origin endpointurl https://dagshub.com/LamPaturle-AI/examen-dvc.s3

# Setup credentials
dvc remote modify origin --local access_key_id 8a08ba4d3a9988a7f9c1664a9c97b2354641694d
dvc remote modify origin --local secret_access_key 8a08ba4d3a9988a7f9c1664a9c97b2354641694d

# Setup default origin
dvc remote default origin

# Add stage 1
dvc stage add -n split \
              -d src/data/data_split.py \
              -d data/raw/raw.csv \
              -o data/processed/X_train.csv \
              -o data/processed/X_test.csv \
              -o data/processed/y_train.csv \
              -o data/processed/y_test.csv \
              -p split.test_size \
              -p split.random_state \
              python src/data/data_split.py
dvc repro

# Track new files on git
git add data/processed/.gitignore dvc.yaml
git add dvc.lock

# Add stage 2
dvc stage add -n normalize \
              -d src/data/normalize.py \
              -d data/processed/X_train.csv \
              -d data/processed/X_test.csv \
              -o data/processed/X_train_scaled.csv \
              -o data/processed/X_test_scaled.csv \
              python src/data/normalize.py
dvc repro

# Add stage 3
dvc stage add -n gridsearch \
              -d src/models/grid_search.py \
              -d data/processed/X_train_scaled.csv \
              -d data/processed/y_train.csv \
              -o models/best_params.pkl \
              -p model.n_estimators \
              -p model.max_depth \
              -p model.learning_rate\
              python src/models/grid_search.py
dvc repro

# Track new files on git
git add models/.gitignore

# Add stage 4
dvc stage add -n train \
              -d src/models/training.py \
              -d data/processed/X_train_scaled.csv \
              -d data/processed/y_train.csv \
              -d models/best_params.pkl \
              -o models/gbr_model.pkl \
              python src/models/training.py
dvc repro

# Add stage 5
dvc stage add -n evaluate \
    -d src/data/evaluate.py \
    -d data/processed/X_test_scaled.csv \
    -d data/processed/y_test.csv \
    -d models/gbr_model.pkl \
    -o data/processed/prediction.csv \
    -m metrics/scores.json \
    python src/data/evaluate.py
dvc repro

# Track new files on git
git add metrics/.gitignore

# Add params.yaml file
touch params.yaml

# Track new file on Git
git add params.yaml

# Commit file to Git
git commit -m "Add params.yaml for DVC"

# Check everything works
dvc repro

# Push to DVC
dvc push

# Install libraries
pip install pandas
pip install sklearn

# Install pipreqs
pip install pipreqs 

# Generate minimal requirements.txt
pipreqs .

# Remove virtual environment
mamba remove -n dsdvcexam --all
