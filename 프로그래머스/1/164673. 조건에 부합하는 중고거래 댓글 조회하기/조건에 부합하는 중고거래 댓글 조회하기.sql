SELECT b.TITLE, b.BOARD_ID, r.REPLY_ID, r.WRITER_ID, r.CONTENTS, date_format(r.CREATED_DATE, '%Y-%m-%d') as CREATED_DATE
from used_goods_board b
inner join used_goods_reply r
on b.board_id = r.board_id
where b.created_date between '2022-10-01' and '2022-10-31'
order by r.created_date asc, b.title asc;