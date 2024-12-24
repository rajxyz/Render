import subprocess

try:
    subprocess.check_call(["python", "-m", "spacy", "download", "en_core_web_sm"])
    print("spaCy model installed successfully!")
except subprocess.CalledProcessError as e:
    print(f"Error installing spaCy model: {e}")