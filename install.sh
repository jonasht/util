echo "create env python"
python -m venv .env

echo "activate env"
source .env/bin/activate 

echo "installing libs..."
pip install -r requirements.txt

echo "finished"