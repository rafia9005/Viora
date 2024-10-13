import os
import subprocess

def download_model():
    model_name = "TheBloke/zephyr-7B-beta-GGUF"
    output_file = "../models/models.gguf" 
    
    os.makedirs("../models", exist_ok=True) 
    
    command = [
        "huggingface-cli", 
        "download", 
        model_name, 
        "zephyr-7b-beta.Q4_K_M.gguf", 
        "--local-dir", 
        ".", 
        "--local-dir-use-symlinks", 
        "False"
    ]

    try:
        subprocess.run(command, check=True)
        os.rename("zephyr-7b-beta.Q4_K_M.gguf", output_file)
        print(f"Model downloaded and saved to {output_file}")
    except subprocess.CalledProcessError as e:
        print(f"Error downloading model: {e}")

if __name__ == "__main__":
    download_model()
