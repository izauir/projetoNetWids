CREATE DATABASE netwids;
USE netwids;

CREATE TABLE responsavel(
	cpf int primary key not null,
    nome varchar(100) not null,
    edereco varchar(100),
    login varchar(50),
    senha varchar(50)
);

CREATE TABLE crianca(
	id int primary key not null auto_increment,
    nome varchar(100) not null,
    idade int not null,
    pontuacao int not null,
    senha varchar(50),
    cpf_responsavel int,
    
    foreign key (cpf_responsavel) references responsavel(cpf)
);

CREATE TABLE tarefas(
	id int primary key not null,
    titulo varchar(100) not null,
    img varchar(100),
    descricao varchar(500) not null,
    prazo varchar(50),
    status varchar(25),
    pontos int not null,
    id_crianca int,
    
    foreign key (id_crianca) references crianca(id)
);

/* TIPOS: 1= audio, 2= leitura, 3= audio e leitura */
CREATE TABLE livros(
	id int primary key not null,
    titulo varchar(100) not null,
    img varchar(100),
    descricao varchar(500) not null,
    prazo varchar(50),
    status varchar(25),
    pontos int not null,
    tipo int not null,
    id_crianca int,
    
    foreign key (id_crianca) references crianca(id)
);

CREATE TABLE jornada(
	id int primary key not null,
    titulo varchar(100) not null,
    img varchar(100),
    descricao varchar(500) not null,
    id_crianca int,
    
    foreign key (id_crianca) references crianca(id)
);