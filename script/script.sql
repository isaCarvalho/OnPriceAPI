DROP TABLE IF EXISTS products;
DROP TABLE IF EXISTS stores;
DROP SEQUENCE IF EXISTS products_seq;
DROP SEQUENCE IF EXISTS stores_seq;

CREATE TABLE stores (
	id int primary key,
	name varchar(255) not null,
	password varchar(32) not null,
	cnpj varchar(255) not null unique,
	street varchar(255) not null,
	number varchar(11) not null,
	bairro varchar(255) not null,
	city varchar(255) not null,
	uf varchar(12) not null,
	time varchar(255) not null
);

CREATE SEQUENCE stores_seq START 1 INCREMENT 1 MINVALUE 1;
ALTER TABLE stores ALTER COLUMN id SET DEFAULT nextval('stores_seq');

CREATE TABLE products (
	id int PRIMARY KEY,
	name varchar(255) NOT NULL,
	category varchar(255) NOT NULL,
	price varchar(30) NOT NULL,
	quantity int not null,
	unity varchar(255) not null,
	stamp varchar(255) not null,
	id_store int not null references stores(id) on delete cascade
);

CREATE SEQUENCE products_seq START 1 INCREMENT 1 MINVALUE 1;
ALTER TABLE products ALTER COLUMN id SET DEFAULT nextval('products_seq');

INSERT INTO stores (name, password, cnpj, street, number, bairro, city, uf, time) VALUES
('Mercado 1', '123456', '987654321', 'Teste', '2', 'Teste', 'Teste', 'RJ', '19:00'),
('Mercado 2', '123456', '98452', 'Teste', '1', 'Teste', 'Teste', 'SC', '18:00'),
('Mercado 3', '45612', '65489', 'Teste', '3', 'Teste', 'Teste', 'SP', '17:00');

INSERT INTO products (name, category, price, quantity, unity, stamp, id_store) VALUES
('Papel Higienico', 'Limpeza', 'R$ 7,99', 1, 'Pacote', 'Elite', 1),
('Papel Higienico', 'Limpeza', 'R$ 9,99', 1, 'Pacote', 'Neve', 1),
('Papel Higienico', 'Limpeza', 'R$ 5,99', 1, 'Pacote', 'Fofinho', 1),
('Tomate', 'Frutas', 'R$ 1,99', 1, 'Kg', 'Fazendinha', 2),
('Manga', 'Frutas', 'R$ 2,99', 1, 'Unidade', 'Fazendinha', 2),
('Alcatra', 'Carnes', 'R$ 20,99', 1, 'Kg', 'Carne', 3);

SELECT * FROM stores;

SELECT * FROM products;
