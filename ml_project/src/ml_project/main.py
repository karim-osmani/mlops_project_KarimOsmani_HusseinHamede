from ml_project.data_loader import load_data
from ml_project.config import load_config
def main():
 config = load_config()
 print("Loaded Configuration:")
 print(config)
# Use configuration in the pipeline
 data = load_data(config.data_loader.file_path)
 print("Loaded Data:")
 print(data)
if __name__ == "__main__":
 main()