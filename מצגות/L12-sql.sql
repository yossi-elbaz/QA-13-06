/* להציג את כל הערים */

select *
from cities

/* להציג את כל מדינות */

select *
from countries

/* להציג את שמות המדינות */

select city
from cities

/* הצלבה בין עיר למדינה */

select city,countries.country
from cities
inner join countries on cities.country = countries.ID

select Products.Name,Products.Price,Products.Price*1.17 as Kolel_maam
from Products

select DISTINCT Category,price
from Products


select Category
from Products
group by Category
order by Category
