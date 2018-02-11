# Views

```sql
create view article_path AS 
select author, title, slug, concat ('/article/',slug) as article_name, lead, body, time, id 
from articles;
```

```sql
create view article_info AS
select article_path.author as article_id, article_path.slug as article_title, log.status, log.time 
from log, article_path 
where article_path.article_name = log.path;
```

```sql
create view day_log AS 
select DATE(time), status, count(status) as status_count 
from log where status IN ('200 OK', '404 NOT FOUND') 
group by DATE, status order by DATE;
```

```sql
create view log_calc AS
(
select DATE, Request_success, Request_failure, 
(cast(Request_failure as float)/ (cast(Request_success as float)+ cast(Request_failure as float))*100) as Error_percentage 
from (
select DATE,
max(case when status = '200 OK' then status_count END) as Request_success,
max(case when status = '404 NOT FOUND' then status_count END) as Request_failure 
from day_log group by DATE) as error_log);
```
