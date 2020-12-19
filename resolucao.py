import json


def ler_arquivo(local: str) -> list:
    """
    Essa função serve para ler um arquivo JSON e devolver um dicionário
    :param local: str, local onde se encontra o arquivo JSON
    :return: list, lista de dicionário com os dados do arquivo JSON
    """
    with open(local, encoding='UTF-8') as arquivo:
        return json.loads(arquivo.read())


def corrigir_nomes(database: list) -> None:
    """
    Essa função serve para percorrer os produtos dentro do database
    e corrigir os nomes corrompidos
    :param database: list, lista de dicionários dos produtos carregados do JSON
    :return: None
    """
    mapa = {'æ': 'a', '¢': 'c', 'ø': 'o', 'ß': 'b'}
    for produto in database:
        corrigido = ''
        for letra in produto['name']:
            if letra in mapa:
                letra = mapa[letra]
            corrigido += letra
        produto['name'] = corrigido


def corrigir_precos(database: list) -> None:
    """
    Essa função serve para percorrer os produtos dentro do database
    e modificar os preços de str para float
    :param database: list, lista de dicionários dos produtos carregados do JSON
    :return: None
    """
    for produto in database:
        produto['price'] = float(produto['price'])


def corrigir_quantidade(database: list) -> None:
    """
    Essa função serve para percorrer os produtos dentro do database
    e adicionar as quantidades aos produtos que não tiverem o campo de quantidade (quantity)
    :param database: list, lista de dicionários dos produtos carregados do JSON
    :return: None
    """
    for produto in database:
        if 'quantity' not in produto:
            produto['quantity'] = 0


def exportar_json(database: list) -> None:
    """
    Essa função serve para exportar um dicionário para um arquivo JSON
    :param database: list, lista de dicionários dos produtos carregados do JSON
    :return: None
    """
    with open('saida.json', 'w') as arquivo:
        arquivo.write(json.dumps(database, indent=2, ensure_ascii=False))


def imprimir_produtos(database: list) -> None:
    """
    Essa função serve para imprimir a lista com todos os nomes dos produtos, ordenados
    primeiro por categoria em ordem alfabética e ordenados por id em ordem crescente
    :param database: list, lista de dicionários dos produtos carregados do JSON
    :return: None
    """
    categorias = {}
    for produto in database:
        if produto['category'] not in categorias:
            categorias[produto['category']] = []
        categorias[produto['category']].append(produto)
    print('-=' * 40)
    print('Lista de produtos ordenados por Categoria e ID'.center(80))
    print('-=' * 40)
    for k, v in sorted(categorias.items()):
        for produto in sorted(v, key=lambda x: x['id']):
            print(produto['name'])
    print()


def calcular_estoque(database: list) -> None:
    """
    Essa função serve para calcular o valor total do estoque por categoria e imprimir os resultados
    :param database: list, lista de dicionários dos produtos carregados do JSON
    :return: None
    """
    categorias = {}
    for produto in database:
        if produto['category'] not in categorias:
            categorias[produto['category']] = 0
        categorias[produto['category']] += produto['price'] * produto['quantity']
    print('-=' * 18)
    print('Valor total do Estoque por Categoria')
    print('-=' * 18)
    print(f'{"Categorias".ljust(20)} | Valor total')
    print('-' * 36)
    for k, v in categorias.items():
        print(f'{str(k).ljust(20)} | R$ {v:.2f}')
    print('-' * 36)


if __name__ == '__main__':
    dados = ler_arquivo('broken-database.json')
    corrigir_nomes(dados)
    corrigir_precos(dados)
    corrigir_quantidade(dados)
    exportar_json(dados)
    imprimir_produtos(dados)
    calcular_estoque(dados)
