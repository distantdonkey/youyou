SELECT 运营指标监控报表.营销策划名称 AS `专题名称(活动名称）` ,
       运营指标监控报表.`发送成功用户数(最大值)` AS `覆盖量(万)`,
       round((运营指标监控报表.日累计手机号码拉新量/运营指标监控报表.`发送成功用户数(最大值)`),8) AS `拉新率`,
       运营指标监控报表.`日累计手机号码拉新量`
FROM 运营指标监控报表
INNER JOIN 冬奥期间活动表格 ON 运营指标监控报表.子策划编码 = 冬奥期间活动表格.子策划编码
WHERE 运营指标监控报表.数据日期=date_sub(curdate() ,interval 2 DAY)
  AND 冬奥期间活动表格.客户端 ='咪咕音乐'
  AND 冬奥期间活动表格.下发日期 =date_sub(curdate() ,interval 2 DAY)
ORDER BY 3 DESC;