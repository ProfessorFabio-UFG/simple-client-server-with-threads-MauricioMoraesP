# 📞 Sistema de Agenda Telefônica - TCP Socket

## 📝 Descrição

Este projeto implementa uma **agenda telefônica distribuída** usando **sockets TCP**. Um servidor central mantém uma lista de contatos, enquanto múltiplos clientes podem se conectar simultaneamente para realizar operações como adicionar, atualizar ou listar contatos.

---

## ⚙️ Funcionalidades

* ➕ **Adicionar contatos**: Cadastra novos nomes e números.
* ✏️ **Atualizar contatos**: Altera o número de um contato existente.
* 📋 **Listar contatos**: Exibe todos os contatos salvos no servidor.

---

## 🚀 Como Executar

### 1. Inicie o servidor:

```bash
python servidor.py
```

### 2. Conecte um ou mais clientes (em terminais separados):

```bash
python cliente.py
```

---

## 💬 Comandos disponíveis

| Comando  | Formato                       | Descrição                                 |
| -------- | ----------------------------- | ----------------------------------------- |
| `ADD`    | `ADD <nome> <número>`         | Adiciona um novo contato                  |
| `UPDATE` | `UPDATE <nome> <novo_número>` | Atualiza o número de um contato existente |
| `LIST`   | `LIST`                        | Lista todos os contatos cadastrados       |

---

## 📌 Exemplos de Uso

```bash
ADD João 11987654321
UPDATE João 11999999999
LIST
```

