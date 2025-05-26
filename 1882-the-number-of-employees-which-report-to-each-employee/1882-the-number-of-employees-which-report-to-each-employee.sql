select m.employee_id, m.name,
count(*) reports_count,
round(avg(e.age)) average_age
from Employees m inner join Employees e
on m.employee_id = e.reports_to
group by m.employee_id
order by m.employee_id