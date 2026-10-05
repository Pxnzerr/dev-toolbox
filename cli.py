import argparse
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
)
from src.file_utils import format_bytes
from src.validators import (
    is_valid_cnpj,
    is_valid_cpf,
    is_valid_email,
    is_valid_ipv4,
    is_valid_url,
    only_digits,
)


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Dev Toolbox CLI - Ferramentas de apoio e produtividade para desenvolvedores"
    )
    subparsers = parser.add_subparsers(dest="command", help="Comandos disponiveis")

    # slug
    p_slug = subparsers.add_parser("slug", help="Converte texto em slug amigavel para URLs")
    p_slug.add_argument("text", help="Texto de entrada")

    # gen-id
    p_id = subparsers.add_parser("id", help="Gera um ID curto unico")
    p_id.add_argument("--prefix", "-p", default="", help="Prefixo opcional do ID")

    # now
    subparsers.add_parser("now", help="Exibe o timestamp UTC atual em ISO 8601")

    # mask
    p_mask = subparsers.add_parser("mask", help="Ofusca informacoes sensiveis em um texto")
    p_mask.add_argument("text", help="Texto a ser mascarado")
    p_mask.add_argument("--start", "-s", type=int, default=2, help="Caracteres visiveis no inicio")
    p_mask.add_argument("--end", "-e", type=int, default=2, help="Caracteres visiveis no final")
    p_mask.add_argument("--char", "-c", default="*", help="Caractere de ofuscamento")

    # case
    p_case = subparsers.add_parser("case", help="Converte nomenclatura de codigo (snake, camel, pascal)")
    p_case.add_argument("text", help="Identificador a ser convertido")
    p_case.add_argument(
        "--to",
        choices=["snake", "camel", "pascal"],
        default="snake",
        help="Formato de destino (padrao: snake)",
    )

    # validate
    p_val = subparsers.add_parser("validate", help="Valida formatos comuns (cpf, email, cnpj, ip, url)")
    p_val.add_argument("type", choices=["cpf", "email", "cnpj", "ip", "url"], help="Tipo de validacao")
    p_val.add_argument("value", help="Valor a ser validado")

    # digits
    p_dig = subparsers.add_parser("digits", help="Extrai apenas os digitos de um texto")
    p_dig.add_argument("text", help="Texto com formatacoes ou caracteres especiais")

    # bytes
    p_bytes = subparsers.add_parser("bytes", help="Formata quantidade de bytes em representacao legivel (KB, MB, GB)")
    p_bytes.add_argument("size", type=int, help="Quantidade em bytes")
    p_bytes.add_argument("--precision", "-p", type=int, default=2, help="Casas decimais (padrao: 2)")

    # hash
    p_hash = subparsers.add_parser("hash", help="Gera hash criptografico de um texto (sha256, md5, sha1, sha512)")
    p_hash.add_argument("text", help="Texto de entrada para calculo do hash")
    p_hash.add_argument(
        "--algo",
        "-a",
        default="sha256",
        choices=["sha256", "md5", "sha1", "sha512"],
        help="Algoritmo de hash (padrao: sha256)",
    )

    # b64
    p_b64 = subparsers.add_parser("b64", help="Codifica ou decodifica strings em Base64")
    p_b64.add_argument("text", help="Texto de entrada")
    p_b64.add_argument(
        "--decode",
        "-d",
        action="store_true",
        help="Decodifica string Base64 para texto original",
    )

    args = parser.parse_args()

    if args.command == "slug":
        print(slugify(args.text))
    elif args.command == "id":
        print(generate_id(args.prefix))
    elif args.command == "now":
        print(current_iso_utc())
    elif args.command == "mask":
        print(mask_string(args.text, args.start, args.end, args.char))
    elif args.command == "case":
        if args.to == "snake":
            print(camel_to_snake(args.text))
        elif args.to == "camel":
            print(snake_to_camel(args.text, pascal=False))
        elif args.to == "pascal":
            print(snake_to_camel(args.text, pascal=True))
    elif args.command == "digits":
        print(only_digits(args.text))
    elif args.command == "validate":
        if args.type == "cpf":
            valid = is_valid_cpf(args.value)
            status = "Valido" if valid else "Invalido"
            print(f"CPF: {status}")
        elif args.type == "cnpj":
            valid = is_valid_cnpj(args.value)
            status = "Valido" if valid else "Invalido"
            print(f"CNPJ: {status}")
        elif args.type == "email":
            valid = is_valid_email(args.value)
            status = "Valido" if valid else "Invalido"
            print(f"E-mail: {status}")
        elif args.type == "ip":
            valid = is_valid_ipv4(args.value)
            status = "Valido" if valid else "Invalido"
            print(f"IPv4: {status}")
        elif args.type == "url":
            valid = is_valid_url(args.value)
            status = "Valido" if valid else "Invalido"
            print(f"URL: {status}")
    elif args.command == "bytes":
        print(format_bytes(args.size, decimal_places=args.precision))
    elif args.command == "hash":
        print(hash_text(args.text, algorithm=args.algo))
    elif args.command == "b64":
        if args.decode:
            try:
                print(base64_decode(args.text))
            except ValueError as err:
                print(f"Erro: {err}")
        else:
            print(base64_encode(args.text))
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
