# Reconhecimento da fonte — Tabelas Processuais Unificadas (TPU)

> **Projeto:** MP1 — Coletor da TPU
> **Fonte:** Sistema de Gestão de Tabelas Processuais Unificadas (SGT) — CNJ
> **Versão da TPU no momento do levantamento:** 79 · 26/05/2026

---

## 1. Onde a TPU é publicada

Sistema de Gestão de Tabelas Processuais Unificadas (SGT), mantido pelo CNJ.

🔗 https://www.cnj.jus.br/sgt/versoes.php

O SGT oferece **três formas distintas de acesso** ao mesmo conteúdo:

| # | Forma de acesso | Descrição | Adotado neste projeto |
|---|---|---|---|
| 1 | **Download de planilha** | Arquivos `.xls` por tabela, ramo e grau | ✅ MP1 |
| 2 | **Scripts SQL** | Estrutura (DDL) e dados (INSERT), em dialeto MySQL e Oracle/Postgres, com temporariedade | ✅ MP2 |
| 3 | **WebService SOAP** | `https://www.cnj.jus.br/sgt/sgt_ws.php?wsdl` | ❌ descartado |

### Por que o WebService foi descartado

Nenhuma das funções expostas devolve a tabela completa. Elas operam item a item — filhos de um nó, pais de um nó, busca por nome ou código. Montar a árvore inteira exigiria percurso recursivo com uma requisição por nó, o que é desproporcional ao escopo do MP1.

Uma função do WebService, porém, permanece útil como referência futura:

```
getDataUltimaVersao()  →  retorna a data da última versão publicada
```

É o caminho para, mais adiante, detectar automaticamente a mudança de versão da TPU.

---

## 2. Formatos disponíveis

| Formato | Extensão | Observação |
|---|---|---|
| Planilha Excel | `.xls` | formato Excel **antigo**, não `.xlsx` |
| Script SQL — MySQL | `.sql` | estrutura e dados |
| Script SQL — Oracle/Postgres | `.sql` | estrutura e dados, inclui temporariedade |
| Referência da estrutura | `.doc` | documentação das tabelas |

> ⚠️ **Consequência técnica:** `.xls` é arquivo **binário**. Precisa ser tratado como bytes na coleta e exige biblioteca específica de leitura no Pandas.

---

## 3. Granularidade dos arquivos

Não existe arquivo único. A divisão é:

```
tabela  ×  ramo da justiça  ×  grau
```

**Tabelas:** Classes · Movimentos · Assuntos · Documentos Processuais

**Ramos:** Justiça Estadual · Justiça Federal · Justiça do Trabalho · Justiça Militar · Justiça Eleitoral · Tribunais Superiores

**Graus:** 1º Grau · 2º Grau · Juizado Especial · Turmas Recursais, entre outros, variando por ramo

---

## 4. Autenticação

**Não exige.** Acesso público, sem chave, token ou cadastro.

Verificado: a URL direta do arquivo baixa normalmente em aba anônima, sem passar pela página de origem. O download não depende de sessão.

---

## 5. Estabilidade da URL

**Parcialmente estável.** Estrutura observada:

```
https://www.cnj.jus.br/sgt/versoes_tabelas/planilhas/{versao}_Tabela_{tabela}_Justica_Estadual_{grau}_Grau.xls
```

| Componente | Comportamento | Exemplo |
|---|---|---|
| caminho base | fixo | `/sgt/versoes_tabelas/planilhas/` |
| `{versao}` | **varia a cada versão da TPU** | `79` (atual), `78` (anterior) |
| `{tabela}` | fixo por tabela | `Classes`, `Movimentos`, `Assuntos` |
| `{grau}` | fixo por grau | `1`, `2` |

### Como foi verificado

Acessando "Versões anteriores" e comparando as URLs geradas: o prefixo numérico passou de `79` para `78`, mantido todo o restante do caminho.


### Observação sobre o mecanismo da página

O download não é um link direto na página. Uma função JavaScript (`enviarJust`, em `versoes.js`) monta o endereço e redireciona para o arquivo estático. O arquivo em si, porém, está parado no servidor — **não há parâmetros de query, POST ou payload envolvidos**, o que torna a coleta direta viável.

---

## 6. Data da última atualização

**26/05/2026** — versão 79.

O SGT mantém histórico público de versões anteriores, com registros que remontam a 2010.

---

## 7. Recorte adotado no MP1

**Justiça Estadual, 1º e 2º grau, três tabelas — seis arquivos.**

| # | Tabela | Grau | URL |
|---|---|---|---|
| 1 | Classes | 1º | `.../79_Tabela_Classes_Justica_Estadual_1_Grau.xls` |
| 2 | Classes | 2º | `.../79_Tabela_Classes_Justica_Estadual_2_Grau.xls` |
| 3 | Movimentos | 1º | `.../79_Tabela_Movimentos_Justica_Estadual_1_Grau.xls` |
| 4 | Movimentos | 2º | `.../79_Tabela_Movimentos_Justica_Estadual_2_Grau.xls` |
| 5 | Assuntos | 1º | `.../79_Tabela_Assuntos_Justica_Estadual_1_Grau.xls` |
| 6 | Assuntos | 2º | `.../79_Tabela_Assuntos_Justica_Estadual_2_Grau.xls` |

*Prefixo comum a todas:* `https://www.cnj.jus.br/sgt/versoes_tabelas/planilhas/`

### Justificativa do recorte

 Os Juizados Especiais entram na etapa dos scripts SQL, quando a estrutura relacional já estiver montada.

### Nota sobre acentuação

Os nomes de arquivo usam grafia **sem acento**: `Justica`, não `Justiça`. A grafia deve ser reproduzida exatamente — divergência produz erro 404.

---

## 8. Decisões registradas

| Decisão | Motivo |
|---|---|
| `.xls` no MP1, `.sql` a partir do MP2 | o MP1 tem por objetivo exercitar coleta HTTP, camada RAW e Pandas; o `.sql` é o caminho direto para a modelagem |
| WebService SOAP descartado | não devolve a tabela completa; exigiria percurso recursivo |
| Escopo restrito à Justiça Estadual | alinhado ao domínio do projeto |
| Versão registrada no nome do arquivo bruto | a TPU é versionada; sem isso não há como saber qual versão originou cada análise |

---

## Fontes consultadas

| O que | Endereço |
|---|---|
| Página de versões do SGT | https://www.cnj.jus.br/sgt/versoes.php |
| WSDL do WebService | https://www.cnj.jus.br/sgt/sgt_ws.php?wsdl |
| Diretório das planilhas | https://www.cnj.jus.br/sgt/versoes_tabelas/planilhas/ |
| Glossário da API do DataJud *(referência cruzada — MP3)* | https://datajud-wiki.cnj.jus.br/api-publica/glossario/ |

---

*Levantamento realizado em 07/09/2026 · TPU versão 79*

---
Continuação em 12/09/2026

## 9. Natureza real do arquivo servido

### O que o servidor declara

| Cabeçalho | Valor |
|---|---|
| `Content-Type` | `application/vnd.ms-excel` |
| `Content-Length` | `6406489` (≈ 6,4 MB) |
| `Last-Modified` | `Tue, 26 May 2026 18:37:05 GMT` |
| `Accept-Ranges` | `bytes` |

### O que o conteúdo é de fato

**HTML**, não Excel binário. Os primeiros caracteres da resposta:

```html
<table border=1><tr><td colspan=5 style='font-size:14pt;width: 150px'>
<b>Assuntos processuais do 2º Grau da Justiça Estadual</b></td>
<td align=center><b>Código</b><td align=center><b>Cód. Pai</b>...
```

Não há `<html>`, `<head>` ou `<body>`. É um **fragmento de tabela HTML** servido com cabeçalho MIME de Excel — prática antiga, que funciona porque o Excel abre tabela HTML sem reclamar.

### Como foi verificado

Requisição GET com inspeção de `resposta.headers` e dos 500 primeiros caracteres de `resposta.text`.

---

## 10. Codificação de caracteres

Os acentos chegam corrompidos quando o conteúdo é lido como texto sem declaração explícita de codificação:

| Recebido | Esperado |
|---|---|
| `2ş Grau` | `2º Grau` |
| `Alteraçőes` | `Alterações` |
| `Data de Publicaçăo` | `Data de Publicação` |

**Causa provável.** O servidor não declara `charset` no `Content-Type`. Sem essa informação, a codificação é inferida — e a inferência erra.

---

## 11. Estrutura das colunas

Colunas identificadas no cabeçalho da tabela de Assuntos:

| Coluna | Observação |
|---|---|
| Código | identificador do item |
| **Cód. Pai** | **referência hierárquica — é o que sustenta o MP2** |
| Dispositivo legal | |
| Artigo | |
| Alterações | |
| Glossário | |
| Objetivo de Desenvolvimento Sustentável | |
| Data de Publicação | |
| Data de Alteração | |

O arquivo se autoidentifica na primeira célula: *"Assuntos processuais do 2º Grau da Justiça Estadual"*. 

---

## 12. Volume

Cerca de **6,4 MB** por arquivo (medido em Assuntos 2º grau).

Implicações registradas:

- o `timeout` da coleta precisa acomodar download desse porte — valores de poucos segundos tendem a produzir falha falsa
- seis arquivos de porte semelhante somam volume relevante, o que reforça a decisão de manter a camada bruta fora do repositório

---

## Resumo dos achados

| # | Achado | Afeta |
|---|---|---|
| 1 | conteúdo é HTML apesar do `.xls` e do MIME de Excel | leitura no Pandas |
| 2 | acentuação corrompida por codificação não declarada | leitura e tradução de rótulos |
| 3 | coluna `Cód. Pai` presente no arquivo | modelagem hierárquica (MP2) |
| 4 | ~6,4 MB por arquivo | `timeout` e política de versionamento dos dados |
