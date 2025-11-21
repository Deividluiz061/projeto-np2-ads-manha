# tree_logic.py — você edita APENAS este arquivo nesta atividade.

class Node:
    def __init__(self, question, yes=None, no=None):
        """
        Se 'yes' e 'no' forem None, este nó é uma FOLHA e 'question' guarda a decisão final (string).
        Caso contrário, 'question' é o texto da pergunta e 'yes'/'no' são seus filhos.
        """
        self.question = question
        self.yes = yes
        self.no = no

def is_leaf(node):
    return node is not None and node.yes is None and node.no is None

def navigate_tree(node, answers):
    
    current_node = node
    
    while not is_leaf(current_node):
        if not answers:
            raise ValueError("Faltam respostas para concluir a decisão.")
        
        # Pega a próxima resposta, normaliza para minúsculas, trata 'nao' como 'não'
        answer = answers.pop(0).lower()
        if answer == 'nao':
            answer = 'não'
        
        # Se "sim": vá para node.yes; se "não": vá para node.no; senão levante ValueError
        if answer == 'sim':
            current_node = current_node.yes
        elif answer == 'não':
            current_node = current_node.no
        else:
            raise ValueError(f"Resposta inválida: '{answer}'. Use 'sim' ou 'não'.")
    
    # Ao chegar numa folha, retorne node.question (a decisão final)
    return current_node.question