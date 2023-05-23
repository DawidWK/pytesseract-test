### INSTALLATION

1. Install Terrasect ocr `https://tesseract-ocr.github.io/tessdoc/Installation.html`

ubuntu:

`
sudo apt install tesseract-ocr
sudo apt install libtesseract-dev
`

2. Create virtual env
`
python -m venv venv
`

3. Activate venv 
`
source venv/bin/activate
`

4. Install requirements
`
pip install -r requirements.txt
`

4. Run app
`
python app.py "sciezka/do/pliku.png"
`
