import database.dados_conexao as dc
from api.acesso_cep import BuscaEndereco as be


def cadastrar_produto(id, nome_produto, preco, quantidade):
    comando = f"""insert into bd_loja.vendas values({id},'{nome_produto}',{preco},{quantidade})"""
    dc.cursor.execute(comando)
    dc.conn.commit()
    print('Produto cadastrado com sucesso')


def cadastrar_fornecedor(id, nome_fornecedor, cep):
    valida_cep = be(cep)
    comando = f"""insert into bd_loja.fornecedor values({id},'{nome_fornecedor}','{valida_cep}')"""
    dc.cursor.execute(comando)
    dc.conn.commit()
    print('Fornecedor cadastrado com sucesso')


def remover_produto(id):
    comando = f"""delete from bd_loja.vendas where id = {id}"""
    dc.cursor.execute(comando)
    dc.conn.commit()
    print('Produto deletado com sucesso')


def remover_fornecedor(id):
    comando = f"""delete from bd_loja.fornecedor where id = {id}"""
    dc.cursor.execute(comando)
    dc.conn.commit()
    print('Fornecedor deletado com sucesso')


def listar_produto():
    comando = f"""select * from bd_loja.vendas"""
    dc.cursor.execute(comando)
    for linha in dc.cursor:
        print(linha)
    return 'Produto(s) listados com sucesso'


def listar_fornecedor():
    comando = f"""select * from bd_loja.fornecedor"""
    dc.cursor.execute(comando)
    for linha in dc.cursor:
        print(linha)
    return 'Fornecedor(es) listados com sucesso'
