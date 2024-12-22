import argparse
from ml_project.data_loader import load_data
from ml_project.config import load_config
parser = argparse.ArgumentParser(description="Run the ML data pipeline withspecified configuration.")
parser.add_argument("--config",type=str,required=True,help="Path to the configuration YAML file.")
def main():
 args = parser.parse_args()
 config = load_config(args.config)
 print("Loaded Configuration:")
 print(config)
# Use configuration in the pipeline
 data = load_data(config.data_loader.file_path)
 print("Loaded Data:")
 print(data)
if __name__ == "__main__":
 main()