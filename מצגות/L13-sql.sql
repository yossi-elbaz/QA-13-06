insert into Products
values ('King2',87,86,'toy',1)

update Products set Price = 200
where Name = 'King' and Category != 'game'

delete from Products
where ID = 87