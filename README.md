# Proposta de Atividade Avaliativa Parcial
Repositório criado pelo **GRUPO 06** como Proposta de Atividade Avaliativa Parcial da Disciplina de Programação Funcional (N704) do Curso de Análise e Desenvolvimento de Sistemas da UNIFOR.

| Discente                  | Matrícula |
|-------------------------|-----------|
| Antonio Anastacio de Sousa Silva | 2315382 |
| Raimundo Bruno Gomes Santiago | 2315382 |
| Lucas Cavalcante dos Santos | 2315382 |
| Fernando Ricardo Rodrigues da Costa | 2315382 |

# Lista de Tarefas (To-Do List)

Este projeto é uma aplicação simples de **Lista de Tarefas (To-Do List)** desenvolvida em Python. Ele permite adicionar, remover, visualizar e filtrar tarefas, além de contar com construções funcionais como **função lambda, list comprehension, closure e função de alta ordem**.

## 🚀 Funcionalidades
- 📌 **Adicionar Tarefas**
- 🗑 **Remover Tarefas**
- 📋 **Exibir Todas as Tarefas**
- 🔍 **Filtrar Tarefas** usando **função lambda** e **list comprehension**
- 📊 **Contar o Número de Tarefas**
- 🎯 **Buscar Tarefa Específica** com uma **closure**

## 📂 Estrutura do Código

O código é composto por uma classe `ToDoList` que gerencia a lista de tarefas e uma função `main()` que executa a aplicação.

### 📜 Classe `ToDoList`

| Método                  | Descrição |
|-------------------------|-----------|
| `add_task(task)`        | Adiciona uma nova tarefa à lista. |
| `remove_task(task)`     | Remove uma tarefa da lista, se existir. |
| `show_tasks()`          | Exibe todas as tarefas armazenadas. |
| `filter_tasks(condition)` | Filtra tarefas com base em uma condição usando **função de alta ordem**. |
| `count_tasks()`         | Retorna o número total de tarefas na lista. |
| `create_task_printer()` | Retorna uma **closure** para imprimir tarefas específicas. |

### 🖥 Exemplo de Uso
```python
# Criando a lista de tarefas
todo_list = ToDoList()

# Adicionando tarefas
todo_list.add_task("Estudar Python")
todo_list.add_task("Fazer compras")
todo_list.add_task("Ler um livro")

# Exibindo tarefas
todo_list.show_tasks()

# Filtrando tarefas com 'Estudar'
filtered_tasks = todo_list.filter_tasks(lambda task: "Estudar" in task)
print("Tarefas filtradas:", filtered_tasks)

# Usando a closure para verificar tarefas
task_printer = todo_list.create_task_printer()
task_printer("Estudar Python")
```

## 🛠 Tecnologias Utilizadas
- **Python 3.x**

## 🎯 Construções Funcionais Utilizadas

| Construção Funcional  | Implementação |
|----------------------|---------------|
| **Função Lambda** | Usada para filtrar tarefas dentro de `filter_tasks()`. |
| **List Comprehension** | Implementada para substituir o `filter()`, tornando o código mais eficiente. |
| **Closure** | A função `create_task_printer()` mantém o acesso à lista de tarefas após ser criada. |
| **Função de Alta Ordem** | `filter_tasks()` recebe outra função como argumento e aplica sobre a lista. |

## ▶ Como Executar o Código
1. **Baixe o arquivo** `todo_list.py`.
2. **Execute o código** com o seguinte comando:
   ```bash
   python todo_list.py
   ```
3. O programa exibirá as tarefas adicionadas, removidas e filtradas no terminal.

## 📌 Conclusão
Este projeto demonstra conceitos essenciais de programação funcional em Python dentro de uma aplicação prática de Lista de Tarefas. Ele pode ser expandido para incluir **persistência de dados**, **interface gráfica** ou **integração com bancos de dados**.

---
📌 *Desenvolvido para fins educacionais e aprendizado de conceitos avançados em Python.* 🚀