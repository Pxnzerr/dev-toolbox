import argparse
from src.string_utils import current_iso_utc, generate_id, mask_string, slugify
from src.validators import is_valid_cnpj, is_valid_cpf, is_valid_email, only_digits


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

    # validate
    p_val = subparsers.add_parser("validate", help="Valida formatos comuns (cpf, email, cnpj)")
    p_val.add_argument("type", choices=["cpf", "email", "cnpj"], help="Tipo de validacao")
    p_val.add_argument("value", help="Valor a ser validado")

    # digits
    p_dig = subparsers.add_parser("digits", help="Extrai apenas os digitos de um texto")
    p_dig.add_argument("text", help="Texto com formatacoes ou caracteres especiais")

    args = parser.parse_args()

    if args.command == "slug":
        print(slugify(args.text))
    elif args.command == "id":
        print(generate_id(args.prefix))
    elif args.command == "now":
        print(current_iso_utc())
    elif args.command == "mask":
        print(mask_string(args.text, args.start, args.end, args.char))
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
    else:
        parser.print_help()



if __name__ == "__main__":
    main()
