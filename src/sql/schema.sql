CREATE DATABASE IF NOT EXISTS lib;
USE lib;

CREATE TABLE authors (
    authorId INT unsigned PRIMARY KEY,
    fio TEXT NOT NULL,
    description TEXT,
);

CREATE TABLE books  (
    bookId BIGINT unsigned AUTO_INCREMENT PRIMARY KEY COMMENT 'Идентификатор',
    isdn TEXT,
    year INT,
    name TEXT NOT NULL,
);

CREATE TABLE files (
    bookId references books NOT NULL,
    format VARCHAR(5) NOT NULL
);

CREATE TABLE themes (
    themeId INT unsigned PRIMARY KEY,
    name TEXT,
);

CREATE TABLE book_themes (
    bookId references books NOT NULL,
    themeId references themes NOT NULL
);

CREATE TABLE book_authors (
    bookId references books NOT NULL,
    authorId references authors NOT NULL
);

CREATE TABLE book_references (
    sourceId references books,
    destinationId references books
);
