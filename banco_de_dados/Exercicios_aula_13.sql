select profissao, count(*) from gafanhotos
group by profissao
order by profissao;

select sexo, count(*) from gafanhotos
where nascimento > '2005-01-01'
group by sexo
order by sexo;

select nacionalidade, count(*) from gafanhotos
group by nacionalidade
having count(nacionalidade) >= 3
order by nacionalidade;

select peso, altura, count(*) from gafanhotos
where peso > 100
group by altura
having altura> (select avg(altura) from gafanhotos);