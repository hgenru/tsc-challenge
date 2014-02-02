tsc-challenge
=============

Тестовое задание для TSC.

Программа, которая делает ненавистную Тёме Лебедеву выключку. 


Запуск
======

Для запуска нам потребуется интерпритатор python версии 3.x

help:

    python3 justify.py -h

example:

    justify.py -i example.txt


Тесты
=====

Для тестов нужно поставить nosetests:

    easy_install3 nose

Запускать так:

    nosetests tests.py


Что умеем
=========

 * Юстифицировать
 * Расставлять отступы
 * Работать с юникодом(спасибо python3k!)


Что еще можно допилить
======================

 * Словари + мягкие переносы (тут нужно тоже что-то умное, иначе будут одни переносы)
 * Какой-нибудь супер-алгоритм, который не допускает огромных дыр
