-- Questão 1

SELECT 
    v.Produto
    , v.Categoria
    , SUM(v.Quantidade * v.Preço) AS 'Total de Vendas'
FROM vendas v
GROUP BY v.Produto
ORDER BY 2, 3 DESC;

-- Questão 2
/* Obs. Como na geração dos dados foram 
solicitados dados do ano de 2023
estou considerando Jun/2023 e não 2024 como no e-mail */

SELECT
    '2023-06' AS 'Mês'
    , v.Produto
    , SUM(v.Quantidade) AS 'Quantidade'
FROM vendas v
WHERE v.Data BETWEEN '2023-06-01' AND '2023-06-30'
GROUP BY v.Produto
ORDER BY 3 ASC;