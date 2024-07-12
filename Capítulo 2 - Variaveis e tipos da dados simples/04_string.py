""" 
Uma string é uma série de caracteres

"""
name = "ada lovelace"
print(name.title()) # Altera a primeira letra de cada palavra para maiúscula
print(name.upper()) # Altera todos as letras para maiúsculo
print(name.lower()) # Altera todas as letras para minúsculo

""" 
OBS, método lower() é muito útil para armazenas dados. via de regra, não podemos confiar nas letras maiúsculas e minúsculas fornecidas pelos usuários.
"""

first_name = 'ada'
last_name = 'locelace'
full_name = f"{first_name} {last_name}" # F-string, o f é de formato, o Python formata a string substituindo o nome de qualquer variavel entre chaves pelo valor correspondente
print(full_name)
mensagem = f"Hello, {full_name.title()}"
print(mensagem)

"""
Adicionando tabulação
"""
#sem tabulação
print("Python")
#com tabulação 
print("\tPython")

"""
Adicionado quebra de Linha
"""
#Sem quebra de linha
print("Linguagens: Python C JavaScript")
#Com quebra de linha
print("Linguagens: \nPython\nC\nJavaScript")

#Tabulaçao e quebra de linha
print("Linguagens: \n\tPython\n\tC\n\tJavaScript")

"""
Removendo espaços em brando com o strip()
É essencial considerar espaços em branco pois muitas vezes queremos comparar duas strings para determinar se são iguais
"""
favorite_language = '        Python          '
print(favorite_language)
# removendo espaços a Direita
print(favorite_language.rstrip())

#associar de forma definitiva a remoção dos caracteres em branco é necessario reatribuir à variavel
favorite_language = favorite_language.rstrip()
# Remover espaço em branco do lado esquerdo da string
favorite_language = favorite_language.lstrip()
#Remover espaço em branco em ambas as direções
favorite_language = favorite_language.strip()


""" 
Removendo prefixos
"""
nostarch_url = 'https://nostarch.com'
print(nostarch_url)
#remover prefixo 'https://'
nostarch_url = nostarch_url.removeprefix('https://')
print(nostarch_url)


"""
Evitando erros de sintaxe
"""
# Em casos de apostrofo em alguma palavra, utilize aspas duplas na string
apostrofo = " One of Python's strengths is its diverse"
print(apostrofo)
# Erro de sintaxe com string
#apostrofo_erro = 'One of Python's strengths is its diverse'
#print(apostrofo_erro)
""" 
PS C:\Dev\Curso_Intensivo_Python> & C:/Users/rafae/AppData/Local/Programs/Python/Python312/python.exe "c:/Dev/Curso_Intensivo_Python/Capítulo 2 - Variaveis e tipos da dados simples/04_string.py"
  File "c:\Dev\Curso_Intensivo_Python\Capítulo 2 - Variaveis e tipos da dados simples\04_string.py", line 74
    apostrofo_erro = 'One of Python's strengths is its diverse'
                                                              ^
SyntaxError: unterminated string literal (detected at line 74)
"""

""" 
Faça você mesmo
2.3 Mensagem pessoal: Use uma variável para representar o nome de uma pessoa e exiba uma mensagem para essa pessoa. 
Sua mensagem deve ser simples, como “Olá Eric, gostaria de aprender um pouco de Python hoje?”
""" 
nome_pessoa = 'Rafael Antonio Rodrigues da Rosa'
print(f'Olá {nome_pessoa}, gostaria de aprender um pouco de Python hoje?')
""" 
2.4 Maiúsculas e minúsculas: Use uma variável para representar o nome de uma pessoa e, em seguida, exiba o nome dessa pessoa em letras minúsculas, maiúsculas e as primeiras letras maiúsculas.
"""
#Em letra minúscula
print(nome_pessoa.lower())
#Em letra maiúscula
print(nome_pessoa.upper())
#Primeira letra em maúsculo
print(nome_pessoa.title())

"""
2.5 Citação famosa: Encontre uma citação de uma pessoa famosa que você admira. 
Exiba a citação e o nome do autor. 
Sua saída deve se parecer com a seguinte, incluindo as aspas. 
Exemplo -  “Albert Einstein disse uma vez: ‘Uma pessoa que nunca cometeu um erro nunca tentou nada de novo’.”
"""
citacao = "Stallone cobra disse uma vez: 'Você é um cocô... e eu vou matar você'"
print(citacao)
"""
2.6 Citação famosa 2: Repita o Exercício 2.5, mas desta vez represente o nome da pessoa famosa usando uma variável chamada famous_person. 
Depois, escreva sua mensagem e represente com uma nova variável chamada message. 
Imprima sua mensagem
"""
famous_person = 'Stallone Cobra'
mensagem = "'Você é um cocô... e eu vou matar você'"

print(f'{famous_person} disse uma vez: {mensagem}')
"""
2.7 Removendo nomes: Use métodos de string para representar o nome de uma pessoa, incluindo alguns caracteres em espaço em branco no início e no final do nome. Lembre-se de usar cada uma das combinações de “l”, “r” e “n”, pelo menos em alguma das partes da string. Mostre o nome sem espaço extra no começo ou fim usando as funções strip(), rstrip() e lstrip(). Imprima o nome usando cada um dos três métodos de remoção.

2.8 Extensões de arquivos: O Python tem um método removesulfiix() que funciona exatamente como removeprefix(). Atribua o valor 'python_notes.txt' a uma variavel chamada filename. Depois,
utilize o método removesuffix() para extrair o nome do arquivo sem a extensão do arquivo, como alguns navegadores de arquivos fazem.
"""