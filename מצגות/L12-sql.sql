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
