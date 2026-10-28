# Dev Toolbox 🛠️

Coleção de utilitários rápidos e scripts CLI para aumentar a produtividade no desenvolvimento diário (manipulação de texto, geração de IDs, validações, hashing e Base64).

---

## 📁 Estrutura do Projeto

```text
dev-toolbox/
├── src/
│   ├── __init__.py
│   ├── file_utils.py      # Operações resilientes de I/O em JSON e formatação de bytes
│   ├── string_utils.py    # Slugify, case naming, máscara, IDs, UTC, hashing e Base64
│   └── validators.py      # Validação de CPF, CNPJ, e-mail, IPv4, IPv6, MAC, URLs e sanitização
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

### 2. Remover Acentos
```bash
python cli.py unaccent "Olá Mundo, você está bem?"
# Saída: Ola Mundo, voce esta bem?
```

### 3. Estatísticas e Métricas de Texto
```bash
python cli.py stats "Python é incrível.\nSimples e direto."
# Saída:
# Estatisticas do Texto:
#   Caracteres (total):       36
#   Caracteres (sem espacos): 31
#   Palavras:                 5
#   Linhas:                   2
#   Tamanho medio de palavra: 6.2 chars
#   Tempo estimado de leitura: 1.5s
```

### 4. Gerar ID curto com prefixo
```bash
python cli.py id -p order
# Saída: order_a1b2c3d4e5f6
```

### 5. Gerar Senha Segura
```bash
python cli.py password --length 20
# Saída: xK8#mQ2$pL9@vR4!wT7&

python cli.py password -l 16 --no-symbols --clean
# Saída: 2k7H9mP4wR8xN3bE
```

### 6. Timestamp UTC atual
```bash
python cli.py now
# Saída: 2026-09-04T13:05:46.123456+00:00
```

### 7. Extrair apenas dígitos
```bash
python cli.py digits "TEL: (11) 98765-4321"
# Saída: 11987654321
```

### 8. Mascarar dados sensíveis
```bash
python cli.py mask "4532112233445566" --start 4 --end 4
# Saída: 4532********5566
```

### 9. Validar formato (CPF, CNPJ, E-mail, IPv4, IPv6, MAC, URL, UUID)
```bash
python cli.py validate email "contato@empresa.com"
# Saída: E-mail: Valido

python cli.py validate cnpj "00.000.000/0001-91"
# Saída: CNPJ: Valido

python cli.py validate ip "192.168.1.1"
# Saída: IPv4: Valido

python cli.py validate ipv6 "2001:db8::1"
# Saída: IPv6: Valido

python cli.py validate mac "00:1A:2B:3C:4D:5E"
# Saída: MAC: Valido

python cli.py validate url "https://github.com/Pxnzerr"
# Saída: URL: Valido

python cli.py validate uuid "c9a646d3-9c61-4cd9-bc19-470277872fa1"
# Saída: UUID: Valido
```

### 10. Conversão de Nomenclatura (Case)
```bash
python cli.py case "UserProfileModel" --to snake
# Saída: user_profile_model

python cli.py case "get_user_by_id" --to camel
# Saída: getUserById

python cli.py case "user_account" --to pascal
# Saída: UserAccount
```

### 11. Formatar bytes em tamanho legível
```bash
python cli.py bytes 1048576
# Saída: 1.00 MB

python cli.py bytes 1536 -p 1
# Saída: 1.5 KB
```

### 12. Gerar Hash Criptográfico
```bash
python cli.py hash "minha-string-secreta"
# Saída: cbaeba1245dac8e86abd5c7d7afe4ec0864e7d7aa26ed7503b839f60d9f65144

python cli.py hash "admin" --algo md5
# Saída: 21232f297a57a5a743894a0e4a801fc3

python cli.py hash "admin" -a sha1
# Saída: d033e22ae348aeb5660fc2140aec35850c4da997
```

### 13. Codificação e Decodificação Base64
```bash
# Codificar
python cli.py b64 "Dev Toolbox"
# Saída: RGV2IFRvb2xib3g=

# Decodificar
python cli.py b64 "RGV2IFRvb2xib3g=" --decode
# Saída: Dev Toolbox
```

### 14. Calcular Hash / Checksum de Arquivo
```bash
python cli.py checksum "caminho/do/arquivo.zip" --algo sha256
# Saída: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
```

---

## 🧪 Rodando os Testes

Para executar toda a suíte de testes unitários:

```bash
python -m unittest discover tests
```
