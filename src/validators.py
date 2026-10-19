import ipaddress
import re
import uuid
from typing import Optional
from urllib.parse import urlparse


_NON_DIGITS_RE = re.compile(r"\D")
_EMAIL_RE = re.compile(r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$")
_CNPJ_WEIGHTS_1 = (5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2)
_CNPJ_WEIGHTS_2 = (6, 5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2)


def only_digits(value: str) -> str:
    """Remove todos os caracteres nao numericos de uma string."""
    if value.isdigit():
        return value
    return _NON_DIGITS_RE.sub("", value)


def is_valid_cpf(cpf: str) -> bool:
    """Valida se uma string contem um CPF matematicamente valido segundo modulo 11."""
    digits = only_digits(cpf)
    if len(digits) != 11 or digits == digits[0] * 11:
        return False

    nums = [ord(c) - 48 for c in digits]

    # Primeiro digito verificador (calculo aritmetico direto sem gerador)
    sum1 = (
        nums[0] * 10
        + nums[1] * 9
        + nums[2] * 8
        + nums[3] * 7
        + nums[4] * 6
        + nums[5] * 5
        + nums[6] * 4
        + nums[7] * 3
        + nums[8] * 2
    )
    d1 = (sum1 * 10 % 11) % 10
    if d1 != nums[9]:
        return False

    # Segundo digito verificador
    sum2 = (
        nums[0] * 11
        + nums[1] * 10
        + nums[2] * 9
        + nums[3] * 8
        + nums[4] * 7
        + nums[5] * 6
        + nums[6] * 5
        + nums[7] * 4
        + nums[8] * 3
        + nums[9] * 2
    )
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

    sum1 = (
        nums[0] * 5
        + nums[1] * 4
        + nums[2] * 3
        + nums[3] * 2
        + nums[4] * 9
        + nums[5] * 8
        + nums[6] * 7
        + nums[7] * 6
        + nums[8] * 5
        + nums[9] * 4
        + nums[10] * 3
        + nums[11] * 2
    )
    rest1 = sum1 % 11
    d1 = 0 if rest1 < 2 else 11 - rest1
    if d1 != nums[12]:
        return False

    sum2 = (
        nums[0] * 6
        + nums[1] * 5
        + nums[2] * 4
        + nums[3] * 3
        + nums[4] * 2
        + nums[5] * 9
        + nums[6] * 8
        + nums[7] * 7
        + nums[8] * 6
        + nums[9] * 5
        + nums[10] * 4
        + nums[11] * 3
        + nums[12] * 2
    )
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


def is_valid_ipv6(ip: str) -> bool:
    """Valida se uma string e um endereco IPv6 valido."""
    try:
        ipaddress.IPv6Address(ip.strip())
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


def is_valid_uuid(uuid_to_test: str, version: Optional[int] = None) -> bool:
    """Valida se uma string e um UUID valido, com verificacao opcional de versao."""
    try:
        val = uuid.UUID(str(uuid_to_test).strip())
        if version is not None:
            return val.version == version
        return True
    except (ValueError, AttributeError):
        return False

