/* ����� �� �� ����� */

select *
from cities

/* ����� �� �� ������ */

select *
from countries

/* ����� �� ���� ������� */

select city
from cities

/* ����� ��� ��� ������ */

select city,countries.country
from cities
inner join countries on cities.country = countries.ID
