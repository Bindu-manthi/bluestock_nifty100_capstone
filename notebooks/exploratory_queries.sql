-- 1. Total companies
SELECT COUNT(*) AS total_companies
FROM companies;

-- 2. Top 10 companies by ROE
SELECT company_name, roe_percentage
FROM companies
ORDER BY roe_percentage DESC
LIMIT 10;

-- 3. Top 10 companies by ROCE
SELECT company_name, roce_percentage
FROM companies
ORDER BY roce_percentage DESC
LIMIT 10;

-- 4. Company count by sector
SELECT broad_sector, COUNT(*) AS company_count
FROM sectors
GROUP BY broad_sector
ORDER BY company_count DESC;

-- 5. Average ROE
SELECT AVG(roe_percentage) AS avg_roe
FROM companies;

-- 6. Average ROCE
SELECT AVG(roce_percentage) AS avg_roce
FROM companies;

-- 7. Top 10 companies by index weight
SELECT company_id, index_weight_pct
FROM sectors
ORDER BY index_weight_pct DESC
LIMIT 10;

-- 8. Stock price records per company
SELECT company_id, COUNT(*) AS price_records
FROM stock_prices
GROUP BY company_id
ORDER BY price_records DESC;

-- 9. Companies with highest sales
SELECT company_id, MAX(sales) AS max_sales
FROM profitandloss
GROUP BY company_id
ORDER BY max_sales DESC
LIMIT 10;

-- 10. Companies with highest net profit
SELECT company_id, MAX(net_profit) AS max_profit
FROM profitandloss
GROUP BY company_id
ORDER BY max_profit DESC
LIMIT 10;
