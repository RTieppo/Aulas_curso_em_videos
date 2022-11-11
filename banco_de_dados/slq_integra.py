import mysql.connector as my

con = my.connect(host = 'localhost', database = 'cadastro', user = 'root', password = 'root')

if con.is_connected():
    info = con.get_server_info()
    print('Conectado ao servidor modelo:', info)

    cursor = con.cursor()
    cursor.execute("select database();")
    linha = cursor.fetchone()
    print('conectado ao bando de dados', linha)

if con.is_connected():
    cursor = con.cursor()

    cursor.execute("""select g.nome, c.nome from gafanhotos as g
    join garafanhoto_assiste_curso as a
    on g.id = a.idgafanhoto
    join cursos as c
    on c.idcurso = a.idcurso
    order by g.nome;""")

    linhas = cursor.fetchall()

    for c in linhas:
        print(c)

if con.is_connected():
    cursor.close()
    con.close()
    