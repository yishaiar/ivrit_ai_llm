from pathlib import Path
from dotenv import load_dotenv

base_dir = Path(__file__).parents[1]
data_dir = Path(__file__).parents[2] / 'data'
golden_data_dir = Path(__file__).parents[2] / 'golden_data'


env_dir = Path(__file__).parent /'params.env'
load_dotenv(dotenv_path=env_dir)
