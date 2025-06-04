-- Consulta para acessar os dados de área colhida
SELECT * FROM OPENROWSET( BULK
'https://infrat3db.dfs.core.windows.net/db-dados/Area_Colhida.txt',
FORMAT='CSV', 
PARSER_VERSION='2.0', 
FIRSTROW=2 
) AS Area_Colhida;

-- Consulta para acessar os dados do PIB
SELECT * FROM OPENROWSET( BULK
'https://infrat3db.dfs.core.windows.net/db-dados/public.pib_municipios.txt',
FORMAT='CSV',
PARSER_VERSION='2.0',
FIRSTROW=2
) AS pib_municipios;
