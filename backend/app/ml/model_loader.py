from pathlib import Path
import joblib

from app.core.config import get_settings


class ModelLoader:
    def __init__(self) -> None:
        self.settings = get_settings()
        self._model = None

    def load(self):
        if self._model is None:
            model_path = Path(self.settings.model_path)
            if not model_path.exists():
                raise FileNotFoundError(f"Model artifact not found at {model_path}")
            self._model = joblib.load(model_path)
        return self._model