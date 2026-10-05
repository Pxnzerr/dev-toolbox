import os
import tempfile
import unittest
from src.file_utils import format_bytes, load_json, save_json
from src.string_utils import (
    base64_decode,
    base64_encode,
    camel_to_snake,
    current_iso_utc,
    generate_id,
    hash_text,
    mask_string,
    slugify,
    snake_to_camel,
    truncate_words,
)
from src.validators import (
    is_valid_cnpj,
    is_valid_cpf,
    is_valid_email,
    is_valid_ipv4,
    is_valid_url,
    only_digits,
)


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

    def test_ipv4_validation(self):
        self.assertTrue(is_valid_ipv4("192.168.0.1"))
        self.assertTrue(is_valid_ipv4("127.0.0.1"))
        self.assertTrue(is_valid_ipv4("8.8.8.8"))
        self.assertFalse(is_valid_ipv4("256.1.2.3"))
        self.assertFalse(is_valid_ipv4("192.168.1"))
        self.assertFalse(is_valid_ipv4("invalid_ip"))

    def test_url_validation(self):
        self.assertTrue(is_valid_url("https://github.com/Pxnzerr/dev-toolbox"))
        self.assertTrue(is_valid_url("http://localhost:8080/api/v1"))
        self.assertFalse(is_valid_url("ftp://example.com"))
        self.assertFalse(is_valid_url("www.example.com"))
        self.assertFalse(is_valid_url("just-a-string"))

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

    def test_format_bytes(self):
        self.assertEqual(format_bytes(0), "0 B")
        self.assertEqual(format_bytes(512), "512 B")
        self.assertEqual(format_bytes(1024), "1.00 KB")
        self.assertEqual(format_bytes(1536, decimal_places=1), "1.5 KB")
        self.assertEqual(format_bytes(1048576), "1.00 MB")
        self.assertEqual(format_bytes(1073741824), "1.00 GB")
        with self.assertRaises(ValueError):
            format_bytes(-1)

    def test_hash_text(self):
        self.assertEqual(
            hash_text("admin", "sha256"),
            "8c6976e5b5410415bde908bd4dee15dfb167a9c873fc4bb8a81f6f2ab448a918",
        )
        self.assertEqual(hash_text("admin", "md5"), "21232f297a57a5a743894a0e4a801fc3")
        self.assertEqual(hash_text("admin", "sha1"), "d033e22ae348aeb5660fc2140aec35850c4da997")
        self.assertEqual(
            hash_text("", "sha256"),
            "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855",
        )
        with self.assertRaises(ValueError):
            hash_text("teste", "invalido_algo")

    def test_base64_encoding_and_decoding(self):
        original = "Hello World! Olá Mundo 2026"
        encoded = base64_encode(original)
        self.assertEqual(base64_decode(encoded), original)
        self.assertEqual(base64_encode("test"), "dGVzdA==")
        self.assertEqual(base64_decode("dGVzdA=="), "test")
        with self.assertRaises(ValueError):
            base64_decode("!!!nao_base64_valido!!!")


if __name__ == "__main__":
    unittest.main()

