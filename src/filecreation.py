import xlsxwriter 
  
def export_excel(a,trannum):
    workbook = xlsxwriter.Workbook('TagDetailsFiles/TagDetails_'+ trannum +'.xlsx') 
    worksheet = workbook.add_worksheet("My sheet")    
    d = a
    bold = workbook.add_format({'bold': True})
    worksheet.write(0,0,"Tag",bold)
    worksheet.write(0,1,"Value", bold)
    worksheet.write(0,2,"Name",bold)
    row = 1
    col = 0
    

    #for tag in d.keys():
    #    worksheet.write(row, col, tag)
 
    for key, value  in d.items():   
        worksheet.write(row, col, key) 
        worksheet.write(row, col + 1, value[0]) 
        worksheet.write(row,col+2, value[1])
        if(len(value)==3):
            if type(value[2]) != type([]):
                worksheet.write(row,col+3, value[2])
        
        row += 1
    workbook.close()

