import secrets  # Corrigido: era secrets, não secrects
import string

def criar_senha(tamanho=16, usar_numeros=True, usar_simbolos=True):
    """Gera uma senha aleatória com base nas opções fornecidas."""
    caracteres = string.ascii_letters  # Letras maiúsculas e minúsculas
    
    if usar_numeros:
        caracteres += string.digits  # Adiciona números
        
    if usar_simbolos:
        caracteres += string.punctuation  # Adiciona símbolos (ex: !@#$)

    # Gera a senha usando uma combinação aleatória e segura
    # O módulo secrets é ideal para senhas pois é criptograficamente seguro
    senha = ''.join(secrets.choice(caracteres) for _ in range(tamanho))
    
    return senha