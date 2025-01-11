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

# Add a DagsHub DVC remote
dvc remote add origin s3://dvc
dvc remote modify origin endpointurl https://dagshub.com/LamPaturle-AI/examen-dvc.s3

# Setup credentials
dvc remote modify origin --local access_key_id 8a08ba4d3a9988a7f9c1664a9c97b2354641694d
dvc remote modify origin --local secret_access_key 8a08ba4d3a9988a7f9c1664a9c97b2354641694d

# Setup default origin
dvc remote default origin




# Install pipreqs
pip install pipreqs 

# Generate minimal requirements.txt
pipreqs /examen-dvc --force
