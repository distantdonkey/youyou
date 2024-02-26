import win32com.client as client

xl_app = client.gencache.EnsureDispatch("Excel.Application")
wb = xl_app.Workbooks.Open(r'D:\0刘宇\日报\1206\阅读数据表.xlsx')

doc_app = client.gencache.EnsureDispatch("Word.Application")
doc = doc_app.Documents.Open(r'D:\0刘宇\日报\1206\20231204阅读日报.docx')

rng = doc.Range()
rng.Find.Execute('各活动用户发展效果如下(T-2)：')
rng.MoveStart(Unit=4, Count=1)
wb.Worksheets('日').Shapes(2).Copy()
rng.Paste()

rng = doc.Range()
rng.Find.Execute('各活动打开率如下(T-1)：')
rng.MoveStart(Unit=4, Count=1)
wb.Worksheets('日').Shapes(1).Copy()
rng.Paste()

wb.Close()
doc.Save()
doc.Close()