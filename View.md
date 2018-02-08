# views

'''sql
create view article_det as select substring(path,position('e/' in path)+2) as article_title, status, time from log;
'''

'''sql
create view article_details as select articles.author as article_id, article_det.article_title, article_det.status, article_det.time 
from articles, article_det where articles.slug = article_det.article_title;
'''

'''sql
create view day_log as select DATE(time), status, count(status) as status_count 
from log where status IN ('200 OK', '404 NOT FOUND') 
group by DATE, status order by DATE;
'''

'''sql
create view log_calc as(
select DATE, Request_success, Request_failure, (cast(Request_failure as float)/ (cast(Request_success as float)
+ cast(Request_failure as float))*100) as Error_percentage from (
select DATE,
max(case when status = '200 OK' then status_count END) as Request_success,
max(case when status = '404 NOT FOUND' then status_count END) as Request_failure 
from day_log group by DATE) as error_log);
'''
