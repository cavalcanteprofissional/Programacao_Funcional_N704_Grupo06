class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        """Adiciona uma nova tarefa à lista."""
        self.tasks.append(task)
        print(f"Tarefa adicionada: {task}")

    def remove_task(self, task):
        """Remove uma tarefa da lista, se existir."""
        try:
            self.tasks.remove(task)
            print(f"Tarefa removida: {task}")
        except ValueError:
            print(f"Tarefa não encontrada: {task}")

    def show_tasks(self):
        """Exibe todas as tarefas na lista."""
        if not self.tasks:
            print("Nenhuma tarefa na lista.")
        else:
            print("Tarefas:")
            for idx, task in enumerate(self.tasks, start=1):
                print(f"{idx}. {task}")

    def filter_tasks(self, condition):
        """Filtra as tarefas com base em uma condição (função de alta ordem)."""
        return [task for task in self.tasks if condition(task)]

    def count_tasks(self):
        """Retorna o número total de tarefas."""
        return len(self.tasks)

    def create_task_printer(self):
        """Closure que cria uma função para imprimir tarefas específicas."""
        def task_printer(task):
            if task in self.tasks:
                print(f"Tarefa encontrada: {task}")
            else:
                print(f"Tarefa não encontrada: {task}")
        return task_printer

# Função principal para executar a aplicação
def main():
    todo_list = ToDoList()

    # Adicionando algumas tarefas
    todo_list.add_task("Estudar Python")
    todo_list.add_task("Fazer compras")
    todo_list.add_task("Ler um livro")

    # Exibindo tarefas
    todo_list.show_tasks()

    # Removendo uma tarefa
    todo_list.remove_task("Fazer compras")
    todo_list.show_tasks()

    # Usando uma função lambda para filtrar tarefas que contêm a palavra "Estudar"
    filtered_tasks = todo_list.filter_tasks(lambda task: "Estudar" in task)
    print("Tarefas filtradas:", filtered_tasks)

    # Contando tarefas
    print("Número total de tarefas:", todo_list.count_tasks())

    # Usando a closure para imprimir uma tarefa específica
    task_printer = todo_list.create_task_printer()
    task_printer("Estudar Python")
    task_printer("Fazer compras")

if __name__ == "__main__":
    main()