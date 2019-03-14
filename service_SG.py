from flask import Flask, request
import sqlite3
import json
app = Flask(__name__)

@app.route('/blog', methods=['POST', 'GET'])
def sum():
    c=request.args.get("c",'')
    conn = sqlite3.connect('andmestik.db')
    cur = conn.cursor()
    if c:
        sql1 = """
        insert into LOG(LOG_DATE,LOG_TIME,LOG_TXT) 
        values (date('now'),time(time('now'), '+120 minutes'),'"""+c+"""'); """
        cur.execute(sql1)
    
    sql2="""select Program, 
        StartTime,
        EndTime,
        Duraction,
        Sheets,
        AverageTimePerSheet,
        SheetUtilizationRate,
        RealTime,
        EstTime,
        ToDate,
        Difference,
        Comment,
        Btype,
        Bname,
        Standard,
        Mtype,
        Mthicknes,
        SheetMass,
        SheetCode,
        Operaator,
        FeedbackDate,
        CustSegment,
        CustLine
        FROM SG WHERE Program LIKE '%"""+c+"""%';"""
    #sql2="""select LOG_NO, LOG_DATE, LOG_TIME, LOG_TXT FROM LOG; """
    cur.execute(sql2)
    res=cur.fetchall()
    #res=cur.fetchone
    cur.close()
    conn.commit()
    conn.close()
#    return str(res)
    return json.dumps(res)

app.run(debug=True, port=5000)