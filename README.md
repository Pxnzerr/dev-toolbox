# Dev Toolbox 🛠️

Coleção de utilitários rápidos e scripts CLI para aumentar a produtividade no desenvolvimento diário (manipulação de texto, geração de IDs, validações e parsing).

---

## 📁 Estrutura do Projeto

```text
dev-toolbox/
├── src/
│   ├── __init__.py
│   ├── file_utils.py      # Operações resilientes de I/O em JSON e formatação de bytes
│   ├── string_utils.py    # Slugify, case naming (snake/camel/pascal), máscara, IDs, UTC e hashing
│   └── validators.py      # Validação de CPF e CNPJ (módulo 11), e-mail e sanitização
├── tests/
│   └── test_toolbox.py    # Suíte de testes unitários
├── cli.py                 # Interface interativa de linha de comando
├── .gitignore
└── README.md
```

---

## 🚀 Como Executar a CLI

A CLI utiliza apenas a biblioteca padrão do Python (sem dependências externas necessárias):

### 1. Gerar Slug
```bash
python cli.py slug "Meu Novo Artigo & Projeto 2026!"
# Saída: meu-novo-artigo-projeto-2026
```

### 2. Gerar ID curto com prefixo
```bash
python cli.py id -p order
# Saída: order_a1b2c3d4e5f6
```

### 3. Timestamp UTC atual
```bash
python cli.py now
# Saída: 2026-09-04T13:05:46.123456+00:00
```

### 4. Extrair apenas dígitos
```bash
python cli.py digits "TEL: (11) 98765-4321"
# Saída: 11987654321
```

### 5. Mascarar dados sensíveis
```bash
python cli.py mask "4532112233445566" --start 4 --end 4
# Saída: 4532********5566
```

### 6. Validar formato (CPF, CNPJ, E-mail)
```bash
python cli.py validate email "contato@empresa.com"
# Saída: E-mail: Valido

python cli.py validate cnpj "00.000.000/0001-91"
# Saída: CNPJ: Valido
```

### 7. Conversão de Nomenclatura (Case)
```bash
python cli.py case "UserProfileModel" --to snake
# Saída: user_profile_model

python cli.py case "get_user_by_id" --to camel
# Saída: getUserById

python cli.py case "user_account" --to pascal
# Saída: UserAccount
```

### 8. Formatar bytes em tamanho legível
```bash
python cli.py bytes 1048576
# Saída: 1.00 MB

python cli.py bytes 1536 -p 1
# Saída: 1.5 KB
```

### 9. Gerar Hash Criptográfico
```bash
python cli.py hash "minha-string-secreta"
# Saída: cbaeba1245dac8e86abd5c7d7afe4ec0864e7d7aa26ed7503b839f60d9f65144

python cli.py hash "admin" --algo md5
# Saída: 21232f297a57a5a743894a0e4a801fc3

python cli.py hash "admin" -a sha1
# Saída: d033e22ae348aeb5660fc2140aec35850c4da997
```

---

## 🧪 Rodando os Testes

Para executar toda a suíte de testes unitários:

```bash
python -m unittest discover tests
```
