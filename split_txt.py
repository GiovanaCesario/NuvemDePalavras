import os
import re

def split_txt(input_file, output_dir, fim_term, chapter_pattern):
    """
    Separa um arquivo de texto em partes com base em um padrão configurável.
    
    Parâmetros:
        input_file (str): Caminho do arquivo de texto de entrada.
        output_dir (str): Diretório onde as partes serão salvas.
        fim_term (str): Termo que indica o início da divisão final do conteúdo.
        chapter_pattern (str): Expressão regular que define o padrão para identificar seções.
    """
    # Cria o diretório de saída se ele não existir
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    # Lê todo o conteúdo do arquivo
    with open(input_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Usa a expressão regular fornecida para identificar divisões de seções
    pieces = re.split(chapter_pattern, content)
    
    # Remove espaços extras e descarta seções vazias
    sections = [piece.strip() for piece in pieces if piece.strip()]
    
    fim_index = None
    
    # Procura pelo termo que indica o início da divisão final
    for i, section in enumerate(sections):
        if fim_term in section:
            fim_index = i
            break
    
    # Se o termo foi encontrado, divide a seção correspondente
    if fim_index is not None:
        sec_anterior, sec_restante = sections[fim_index].split(fim_term, 1)
        sections[fim_index] = sec_anterior.strip()
        sec_restante = fim_term + sec_restante.strip()
        sections.insert(fim_index + 1, sec_restante)
    
    # Salva as seções em arquivos individuais
    for index, section in enumerate(sections, start=1):
        output_file = os.path.join(output_dir, f'section_{index}.txt')
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(section)
        print(f"Seção {index} salva em: {output_file}")
    
if __name__ == '__main__':
    # Definição dos arquivos de entrada e saída
    arquivo_entrada = 'Livro/A-Revolução-dos-Bichos-George-Orwell.txt'
    diretorio_saida = 'Capitulos'
    termo_fim = "Posfácio"  # Termo que marca a divisão final
    
    # Expressão regular padrão para identificar seções
    padrao_secao = r'(?<!\S)\*(?=\s*\d+\.)'
    
    # Executa a função de separação
    split_txt(arquivo_entrada, diretorio_saida, termo_fim, padrao_secao)
