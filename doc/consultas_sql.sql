-- Questão 1

SELECT 
    v.Produto
    , v.Categoria
    , SUM(v.Quantidade * v.Preço) AS 'Total de Vendas' -- Calculo do total de vendas
FROM vendas v
GROUP BY v.Produto -- Agrupamento por Produto
ORDER BY 3 DESC; -- Ordenamento por Total de Vendas decrescente

-- Questão 2
/* Obs. Como na geração dos dados foram 
solicitados dados do ano de 2023
estou considerando Jun/2023 e não 2024 como no e-mail */

SELECT
    '2023-06' AS 'Mês' -- Flag do mês
    , v.Produto
    , SUM(v.Quantidade) AS 'Quantidade' -- Calculo da quantidade vendida
FROM vendas v
WHERE v.Data BETWEEN '2023-06-01' AND '2023-06-30' -- Filtro de vendas no período
GROUP BY v.Produto -- Agrupamento por Produto
ORDER BY 3 ASC; -- Odernamento do menor para o maior