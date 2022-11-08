
select * from gafanhotos
where sexo = 'f'
order by nome;

select * from gafanhotos
where nascimento between '2000-01-01' and '2015-12-01'
order by nome;

select * from gafanhotos
where profissao = 'Programador' and sexo = 'M'
order by nome;



