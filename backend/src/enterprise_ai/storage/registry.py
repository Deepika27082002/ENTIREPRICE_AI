import json
from pathlib import Path


class DocumentRegistry:
    """
    Stores and manages indexed document hashes.
    """

    def __init__(self):

        self.hash_file = Path("metadata/hashes.json")

        if not self.hash_file.exists():
            self.hash_file.parent.mkdir(parents=True, exist_ok=True)
            self.hash_file.write_text("{}")

    def _load_hashes(self) -> dict:

        if not self.hash_file.exists():
            return {}

        try:
            with open(self.hash_file, "r") as f:
                return json.load(f)

        except json.JSONDecodeError:
            return {}

    def _save_hashes(self, hashes: dict):

        with open(self.hash_file, "w") as f:
            json.dump(hashes, f, indent=4)

    def document_exists(self, file_hash: str) -> bool:

        hashes = self._load_hashes()

        return file_hash in hashes

    def register_document(self, file_hash: str, filename: str):

        hashes = self._load_hashes()

        hashes[file_hash] = filename

        self._save_hashes(hashes)