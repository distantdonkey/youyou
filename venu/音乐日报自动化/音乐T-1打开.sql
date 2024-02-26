SELECT 运营分析报表.营销策划名称 AS `专题名称(活动名称）` ,
       运营分析报表.`发送成功用户数(最大值)` AS `覆盖量(万)`,
       round((运营分析报表.`页面访问用户数（UV）`/运营分析报表.`发送成功用户数(最大值)`),8) AS `打开率`,
       运营分析报表.`页面访问用户数（UV）`
FROM 运营分析报表
INNER JOIN 冬奥期间活动表格 ON 运营分析报表.子策划编码 = 冬奥期间活动表格.子策划编码
WHERE 运营分析报表.数据日期=date_sub(curdate() ,interval 1 DAY)
  AND 冬奥期间活动表格.客户端 IN ('咪咕音乐')
  AND 冬奥期间活动表格.下发日期 =date_sub(curdate() ,interval 1 DAY)
  AND 冬奥期间活动表格.渠道<>'5G消息'
ORDER BY 3 DESC;