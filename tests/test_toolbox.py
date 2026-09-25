import os
import tempfile
import unittest
from src.file_utils import load_json, save_json
from src.string_utils import (
    camel_to_snake,
    current_iso_utc,
    generate_id,
    mask_string,
    slugify,
    snake_to_camel,
    truncate_words,
)
from src.validators import is_valid_cnpj, is_valid_cpf, is_valid_email, only_digits


class TestDevToolbox(unittest.TestCase):

    def test_slugify(self):
        self.assertEqual(slugify("Olá Mundo! 2026"), "ola-mundo-2026")
        self.assertEqual(slugify("   Espaços   múltiplos  "), "espacos-multiplos")

    def test_truncate_words(self):
        text = "O rato roeu a roupa do rei"
        self.assertEqual(truncate_words(text, 3), "O rato roeu...")
        self.assertEqual(truncate_words(text, 10), text)

    def test_case_conversions(self):
        self.assertEqual(camel_to_snake("UserProfileModel"), "user_profile_model")
        self.assertEqual(camel_to_snake("getUserById"), "get_user_by_id")
        self.assertEqual(snake_to_camel("get_user_by_id"), "getUserById")
        self.assertEqual(snake_to_camel("user_profile_model", pascal=True), "UserProfileModel")
        self.assertEqual(snake_to_camel(""), "")


    def test_generate_id(self):
        uid = generate_id("prod")
        self.assertTrue(uid.startswith("prod_"))
        self.assertEqual(len(uid), 5 + 12)

    def test_mask_string(self):
        self.assertEqual(mask_string("1234567890", 2, 2), "12******90")
        self.assertEqual(mask_string("abc", 2, 2), "***")
        self.assertEqual(mask_string("senha123", 1, 1, "#"), "s######3")

    def test_only_digits(self):
        self.assertEqual(only_digits("abc-123.456/78"), "12345678")

    def test_email_validation(self):
        self.assertTrue(is_valid_email("dev@arthur.dev"))
        self.assertFalse(is_valid_email("email-invalido@"))

    def test_cpf_validation(self):
        self.assertTrue(is_valid_cpf("529.982.247-25"))
        self.assertTrue(is_valid_cpf("52998224725"))
        # CPFs com todos os digitos iguais sao invalidos
        self.assertFalse(is_valid_cpf("111.111.111-11"))
        self.assertFalse(is_valid_cpf("123"))

    def test_cnpj_validation(self):
        self.assertTrue(is_valid_cnpj("00.000.000/0001-91"))
        self.assertTrue(is_valid_cnpj("11.222.333/0001-81"))
        self.assertFalse(is_valid_cnpj("11.111.111/1111-11"))
        self.assertFalse(is_valid_cnpj("00.000.000/0001-00"))


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

