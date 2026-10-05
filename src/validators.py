import ipaddress
import re
from urllib.parse import urlparse


def only_digits(value: str) -> str:
    """Remove todos os caracteres nao numericos de uma string."""
    return re.sub(r"\D", "", value)


def is_valid_cpf(cpf: str) -> bool:
    """Valida se uma string contem um CPF matematicamente valido segundo modulo 11."""
    digits = only_digits(cpf)
    if len(digits) != 11 or len(set(digits)) == 1:
        return False

    # Primeiro digito verificador
    sum1 = sum(int(digits[i]) * (10 - i) for i in range(9))
    d1 = (sum1 * 10 % 11) % 10
    if d1 != int(digits[9]):
        return False

    # Segundo digito verificador
    sum2 = sum(int(digits[i]) * (11 - i) for i in range(10))
    d2 = (sum2 * 10 % 11) % 10
    return d2 == int(digits[10])


def is_valid_email(email: str) -> bool:
    """Valida se o formato do e-mail e sintaticamente valido."""
    pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
    return bool(re.match(pattern, email.strip()))


def is_valid_cnpj(cnpj: str) -> bool:
    """Valida se uma string contem um CNPJ matematicamente valido segundo modulo 11."""
    digits = only_digits(cnpj)
    if len(digits) != 14 or len(set(digits)) == 1:
        return False

    weights1 = [5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]
    sum1 = sum(int(digits[i]) * weights1[i] for i in range(12))
    rest1 = sum1 % 11
    d1 = 0 if rest1 < 2 else 11 - rest1
    if d1 != int(digits[12]):
        return False

    weights2 = [6, 5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]
    sum2 = sum(int(digits[i]) * weights2[i] for i in range(13))
    rest2 = sum2 % 11
    d2 = 0 if rest2 < 2 else 11 - rest2
    return d2 == int(digits[13])


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

