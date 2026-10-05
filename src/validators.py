import ipaddress
import re
from urllib.parse import urlparse


_NON_DIGITS_RE = re.compile(r"\D")
_EMAIL_RE = re.compile(r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$")
_CNPJ_WEIGHTS_1 = (5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2)
_CNPJ_WEIGHTS_2 = (6, 5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2)


def only_digits(value: str) -> str:
    """Remove todos os caracteres nao numericos de uma string."""
    return _NON_DIGITS_RE.sub("", value)


def is_valid_cpf(cpf: str) -> bool:
    """Valida se uma string contem um CPF matematicamente valido segundo modulo 11."""
    digits = only_digits(cpf)
    if len(digits) != 11 or digits == digits[0] * 11:
        return False

    nums = [ord(c) - 48 for c in digits]

    # Primeiro digito verificador
    sum1 = sum(nums[i] * (10 - i) for i in range(9))
    d1 = (sum1 * 10 % 11) % 10
    if d1 != nums[9]:
        return False

    # Segundo digito verificador
    sum2 = sum(nums[i] * (11 - i) for i in range(10))
    d2 = (sum2 * 10 % 11) % 10
    return d2 == nums[10]


def is_valid_email(email: str) -> bool:
    """Valida se o formato do e-mail e sintaticamente valido."""
    return bool(_EMAIL_RE.match(email.strip()))


def is_valid_cnpj(cnpj: str) -> bool:
    """Valida se uma string contem um CNPJ matematicamente valido segundo modulo 11."""
    digits = only_digits(cnpj)
    if len(digits) != 14 or digits == digits[0] * 14:
        return False

    nums = [ord(c) - 48 for c in digits]

    sum1 = sum(nums[i] * _CNPJ_WEIGHTS_1[i] for i in range(12))
    rest1 = sum1 % 11
    d1 = 0 if rest1 < 2 else 11 - rest1
    if d1 != nums[12]:
        return False

    sum2 = sum(nums[i] * _CNPJ_WEIGHTS_2[i] for i in range(13))
    rest2 = sum2 % 11
    d2 = 0 if rest2 < 2 else 11 - rest2
    return d2 == nums[13]


def is_valid_ipv4(ip: str) -> bool:
    """Valida se uma string e um endereco IPv4 valido."""
    try:
        ipaddress.IPv4Address(ip.strip())
        return True
    except (ipaddress.AddressValueError, ValueError):
        return False


def is_valid_url(url: str) -> bool:
    """Valida se uma string e uma URL valida com esquema http ou https."""
    try:
        parsed = urlparse(url.strip())
        return bool(parsed.scheme in ("http", "https") and parsed.netloc)
    except Exception:
        return False

