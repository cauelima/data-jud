PIPELINE DE DADOS DO JUDICIÁRIO BRASILEIRO - DATAJUD - CNJ

Projeto que busca criar um pipeline dos dados abertos do judiciário brasileiro, possibilitando consultas e análises, como: qual vara julga mais? Quais varas com o mesmo acervo é mais rápida? A Vara x está dentro da média de julgamento ou acervo?
Foi escolhido o primeiro e segundo grau da justiça comum e do juizado, ambos cíveis, por serem as áreas de maiores abrangências e com maior quantidade de processos, além de ter mais impacto prático por julgarem temas comuns ao cidadão médio.

## Status

🚧 Em construção. Etapa atual: **MP1 — Coletor da TPU**.

O projeto é entregue em sete etapas. Cada uma tem sua pasta e seu próprio texto explicativo.

| # | Etapa | Status |
|---|---|---|
| MP1 | Coletor das Tabelas Processuais Unificadas | 🚧 em andamento |
| MP2 | Modelagem relacional da taxonomia | ⬜ |
| MP3 | Coletor do DataJud | ⬜ |
| MP4 | Normalização MongoDB → PostgreSQL | ⬜ |
| MP5 | Consultas analíticas em SQL | ⬜ |
| MP6 | Exploração e visualização | ⬜ |
| MP7 | Dicionário de dados | ⬜ |

---

## Fontes de dados

### Tabelas Processuais Unificadas (TPU)

Taxonomia oficial do Judiciário brasileiro, mantida pelo CNJ no Sistema de Gestão de Tabelas Processuais Unificadas (SGT). Define os códigos e rótulos padronizados de **classes**, **assuntos** e **movimentos** processuais.

- **Origem:** https://www.cnj.jus.br/sgt/versoes.php
- **Versão utilizada:** 79 (26/05/2026)
- **Formato coletado:** `.xls`
- **Autenticação:** não exigida


#### Arquivos coletados

Prefixo comum: `https://www.cnj.jus.br/sgt/versoes_tabelas/planilhas/`

| Tabela | Grau | Arquivo |
|---|---|---|
| Classes | 1º | `79_Tabela_Classes_Justica_Estadual_1_Grau.xls` |
| Classes | 2º | `79_Tabela_Classes_Justica_Estadual_2_Grau.xls` |
| Movimentos | 1º | `79_Tabela_Movimentos_Justica_Estadual_1_Grau.xls` |
| Movimentos | 2º | `79_Tabela_Movimentos_Justica_Estadual_2_Grau.xls` |
| Assuntos | 1º | `79_Tabela_Assuntos_Justica_Estadual_1_Grau.xls` |
| Assuntos | 2º | `79_Tabela_Assuntos_Justica_Estadual_2_Grau.xls` |

⚠️ **O prefixo numérico é o número da versão da TPU.** Quando o CNJ publicar a versão 80, estas URLs deixarão de responder. O levantamento completo da fonte, incluindo como isso foi verificado, está em [`notas_fonte.md`](notas_fonte.md).



## Documentação

| Documento | Conteúdo |
|---|---|
| [`notas_fonte.md`](notas_fonte.md) | levantamento completo das fontes: formas de acesso, formatos, estabilidade das URLs e decisões |

---


## Autor

Cauê Lima, analista de dados e jurista.