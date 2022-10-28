select * from cursos
where nome like 'P%';

select * from cursos
where nome like '%a';

select * from cursos
where nome like '%a%';

select * from cursos
where nome like 'ph%p%';

select * from gafanhotos
where nome like '%_silva%';

select distinct nacionalidade from gafanhotos
order by nacionalidade;

select count(*) from cursos;

select count(*) from cursos where carga > 40;

select max(carga) from cursos;

select max(totaulas) from cursos where ano = '2016';

select nome, min(totaulas) from cursos where ano = '2016';

select sum(totaulas) from cursos;

select avg(totaulas) from cursos;