import requests

primeiro_grau_classes="https://www.cnj.jus.br/sgt/versoes_tabelas/planilhas/79_Tabela_Classes_Justica_Estadual_1_Grau.xls"
segundo_grau_classes="https://www.cnj.jus.br/sgt/versoes_tabelas/planilhas/79_Tabela_Classes_Justica_Estadual_2_Grau.xls"
primeiro_grau_assuntos="https://www.cnj.jus.br/sgt/versoes_tabelas/planilhas/79_Tabela_Assuntos_Justica_Estadual_1_Grau.xls"
segundo_grau_assuntos="https://www.cnj.jus.br/sgt/versoes_tabelas/planilhas/79_Tabela_Assuntos_Justica_Estadual_2_Grau.xls"
primeiro_grau_movimentos="https://www.cnj.jus.br/sgt/versoes_tabelas/planilhas/79_Tabela_Movimentos_Justica_Estadual_1_Grau.xls"
segundo_grau_movimentos="https://www.cnj.jus.br/sgt/versoes_tabelas/planilhas/79_Tabela_Movimentos_Justica_Estadual_2_Grau.xls"

resposta = requests.get(segundo_grau_assuntos)


status = resposta.status_code
if status == 200:
    print("Requisição bem-sucedida!")
else:
    print("Falha na requisição.")

print (f"Status: {status}")

tipo_conteudo = resposta.headers['Content-Type']
print(f"Tipo de conteúdo: {tipo_conteudo}")

print(f"Tamanho do conteúdo: {len(resposta.content)} bytes")

conteudo = resposta.text[:500]
print(f"Conteúdo da resposta: {conteudo}")