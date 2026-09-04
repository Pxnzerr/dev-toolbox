import unittest
from src.string_utils import slugify, truncate_words, generate_id
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


if __name__ == "__main__":
    unittest.main()
