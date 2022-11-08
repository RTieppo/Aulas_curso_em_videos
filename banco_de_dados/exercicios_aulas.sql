
select * from gafanhotos
where sexo = 'f'
order by nome;

select * from gafanhotos
where nascimento between '2000-01-01' and '2015-12-01'
order by nome;

select * from gafanhotos
where profissao = 'Programador' and sexo = 'M'
order by nome;

select * from gafanhotos
where nacionalidade = 'Brasil' and sexo = 'F' and nome like 'j%'
order by nome;

select nome, nacionalidade from gafanhotos
where nome like '%silva' and nacionalidade <> 'Brasil' and peso < '100'
order by nome;

select max(altura) from gafanhotos where nacionalidade = 'Brasil' and sexo = 'M'; 

select avg(peso) from gafanhotos;

select nome, min(peso), nascimento, sexo from gafanhotos
where nascimento between '1990-01-01' and '2000-12-31' and sexo = 'F'
order by nome;

select count(altura) from gafanhotos
where altura > '1.9';