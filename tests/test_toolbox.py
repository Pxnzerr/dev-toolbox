import os
import tempfile
import unittest
from src.file_utils import load_json, save_json
from src.string_utils import current_iso_utc, generate_id, slugify, truncate_words
from src.validators import is_valid_cpf, is_valid_email, only_digits


class TestDevToolbox(unittest.TestCase):

    def test_slugify(self):
        self.assertEqual(slugify("Olá Mundo! 2026"), "ola-mundo-2026")
        self.assertEqual(slugify("   Espaços   múltiplos  "), "espacos-multiplos")

    def test_truncate_words(self):
        text = "O rato roeu a roupa do rei"
        self.assertEqual(truncate_words(text, 3), "O rato roeu...")
        self.assertEqual(truncate_words(text, 10), text)

    def test_generate_id(self):
        uid = generate_id("prod")
        self.assertTrue(uid.startswith("prod_"))
        self.assertEqual(len(uid), 5 + 12)

    def test_only_digits(self):
        self.assertEqual(only_digits("abc-123.456/78"), "12345678")

    def test_email_validation(self):
        self.assertTrue(is_valid_email("dev@arthur.dev"))
        self.assertFalse(is_valid_email("email-invalido@"))

    def test_cpf_validation(self):
        # CPFs com todos os digitos iguais sao invalidos
        self.assertFalse(is_valid_cpf("111.111.111-11"))
        self.assertFalse(is_valid_cpf("123"))

    def test_current_iso_utc(self):
        ts = current_iso_utc()
        self.assertIn("+00:00", ts)

    def test_json_file_utils(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            filepath = os.path.join(tmpdir, "subdir", "config.json")
            data = {"name": "dev-toolbox", "active": True}
            save_json(filepath, data)
            loaded = load_json(filepath)
            self.assertEqual(loaded, data)

            missing = load_json(os.path.join(tmpdir, "missing.json"), default={"fallback": True})
            self.assertEqual(missing, {"fallback": True})


if __name__ == "__main__":
    unittest.main()

