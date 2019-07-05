from flask import Flask,render_template,request
import sqlite3 as sql
app=Flask(__name__)

@app.route('/')
def home():
	return render_template('home2.html')

@app.route('/admin')
def admin():
	return render_template('admin.html')

@app.route('/login')
def login():
	return render_template('login.html')




@app.route('/userverify',methods=['POST','GET'])
def userverify():
	if request.method=='POST':

		uname=request.form['an']
		pws=request.form['pws']
		con=sql.connect("database.db")
		con.row_factory=sql.Row
		cur=con.cursor()
		qry="SELECT * FROM myuser2 WHERE name='"+uname+"' and pass='"+pws+"'"
		cur.execute(qry)
		rows=cur.fetchall()
		if (rows):
		    return render_template('book2.html',rows=rows)
		else:
			msg="User name or Password is incorrect, make sure you have Signed Up before Login"
			return render_template("result.html",msg=msg)





@app.route('/adminverify',methods=['POST','GET'])
def adminverify():
	if request.method=='POST':

		name=request.form['an']
		pw=request.form['pws']
		if(name=='admin' and pw=='admin'):
			con=sql.connect("database.db")
			con.row_factory=sql.Row
			cur=con.cursor()
			cur1=con.cursor()
			cur2=con.cursor()
			cur.execute("select count(*) from myuser2")
			cur1.execute("select count(*) from pbookings")
			cur2.execute("select count(*) from lost3")
			c1=cur.fetchall()
			c2=cur1.fetchall()
			c3=cur2.fetchall()
			return render_template('ahome.html',c1=c1,c2=c2,c3=c3)
		else:
			return render_template('home2.html')

@app.route('/adminhome')
def adminhome():
	return render_template('ahome.html')

@app.route('/userdetails')      
def userdetails():
	con=sql.connect("database.db")
	con.row_factory=sql.Row
	cur=con.cursor()
	cur.execute("select*from myuser2")
	rows=cur.fetchall()
	return render_template("listuser.html",rows=rows)

@app.route('/bookingdetails')      
def bookingdetails():
	con=sql.connect("database.db")
	con.row_factory=sql.Row
	cur=con.cursor()
	cur.execute("select * from pbookings")
	rows=cur.fetchall()
	return render_template("bookinglist.html",rows=rows)


@app.route('/addfd')
def addfd():
	return render_template('foods.html')

@app.route('/addgm')
def addgm():
	return render_template('games.html')


@app.route('/addreg')
def addreg():
	return render_template('register.html')




@app.route('/addres')
def addres():
	return render_template('res.html')

@app.route('/addtic')
def addtic():
	return render_template('tic.html')

@app.route('/addoff')
def addoffer():
	return render_template('offer.html')

@app.route('/addtime')
def addtime():
	return render_template('time.html')

@app.route('/adduser',methods=['POST','GET'])          #add record
def adduser():
	if request.method=='POST':
		try:
			name=request.form['name']
			email=request.form['email']
			phone=request.form['phone']
			pw=request.form['pw']

			with sql.connect("database.db") as con:
				cur=con.cursor()
				qry="INSERT INTO myuser2(name,email,phone,pass) VALUES('"+ name +"','"+ email +"','"+ phone +"','"+ pw +"')"
				cur.execute(qry)
				con.commit()
				msg="Record successfully added"
		except:
			con.rollback()
			msg="error in insertion operation"

		finally:
			return render_template("home2.html",msg=msg)
			con.close()


@app.route('/addbook',methods=['POST','GET'])          #add record
def addbook():
	qry=''
	msg=''
	qry1=''
	if request.method=='POST':
		try:
			bname=request.form['nm']
			ch=request.form['ch']
			ad=request.form['ad']
			sen=request.form['sen']
			dy=request.form['dy']
			mn=request.form['mn']
			yr=request.form['yr']
			mp=request.form['mp']
			fname=request.form['mysort']
			qt=request.form['qt']
			with sql.connect("database.db") as con:
				cur=con.cursor()
				qry1="INSERT INTO pbookings(name,child,adults,senior,mode,myday,month,year,food, quantity) VALUES('"+ bname +"',"+ ch + ","+ ad +","+ sen +",'"+ mp +"',"+ dy +","+ mn +","+ yr +",'"+ fname +"',"+ qt +")"
				cur.execute(qry1)
				con.commit()
				msg="Record successfully added"
		except: 
			con.rollback()
			msg="error in insertion operation"

		finally:
			con.row_factory=sql.Row
			cur=con.cursor()
			cur.execute("select * from pbookings where rowid = (select max(rowid) from pbookings)")
			rows=cur.fetchall();
			return render_template("listorder1.html",rows=rows)
			con.close()
	else:
		return render_template("home2.html")


@app.route('/deleteuser/<name>',methods=['POST','GET'])
def deleteuser(name):
	if request.method=='GET':
		try:
			with sql.connect("database.db") as con:
				cur=con.cursor()
				qry="DELETE FROM myuser2 WHERE name='" + name + "'"
				cur.execute(qry)
				con.commit()
				msg="Record deleted successfully"
		except Exception as zd:
			print(zd)
			con.rollback()
			msg="error in deletion operation"
		finally:
			return render_template("result1.html",msg=qry)
			con.close()

@app.route('/deletebook/<name>',methods=['POST','GET'])
def deletebook(name):
	if request.method=='GET':
		try:
			with sql.connect("database.db") as con:
				cur=con.cursor()
				cur.execute("DELETE FROM pbookings WHERE name='" + name + "'")
				con.commit()
				msg="Record deleted successfully"
		except Exception as zd:
			print(zd)
			con.rollback()
			msg="error in deletion operation"
		finally:
			return render_template("result1.html",msg=msg)
			con.close()


@app.route('/addfound')
def addfound():
	return render_template('foundform.html')

@app.route('/addfoundlist',methods=['POST','GET'])          #add record
def addfoundlist():
	if request.method=='POST':
		try:
			obj=request.form['obj']
			typ=request.form['type']
			color=request.form['color']
			date1=request.form['date1']
			with sql.connect("database.db") as con:
				cur=con.cursor()
				qry="INSERT INTO lost3(object,type,color,date1) VALUES('"+ obj +"','"+ typ +"','"+ color +"','"+ date1 +"')"
				cur.execute(qry)
				con.commit()
				msg="Record successfully added"
		except:
			con.rollback()
			msg="error in insertion operation"

		finally:
			return render_template("ahome.html",msg=msg)
			con.close()

@app.route('/founddetails')      
def founddetails():
	con=sql.connect("database.db")
	con.row_factory=sql.Row
	cur=con.cursor()
	cur.execute("select * from lost3")
	rows=cur.fetchall()
	return render_template("foundlist.html",rows=rows)

@app.route('/lostverify',methods=['POST','GET'])
def lostverify():
	if request.method=='POST':

		oname=request.form['on']
		otype=request.form['otype']
		ocolour=request.form['ocolour']
		con=sql.connect("database.db")
		con.row_factory=sql.Row
		cur=con.cursor()
		qry="SELECT * FROM lost3 WHERE object='"+oname+"' and type='"+otype+"' and color='"+ocolour+"'"
		cur.execute(qry)
		rows=cur.fetchall()
		if (rows):
			msg="WE HAVE FOUND YOUR OBJECT PLEASE CONTACT US"
			return render_template("result1.html",msg=msg)
		else:
			msg="WE HAVE NOT FOUND YOUR OBJECT, CHECK ONCE AGAIN AFTER 24 HOURS "
			return render_template("result1.html",msg=msg)



@app.route('/addcmp')
def addcmp():
	return render_template('login1.html')

@app.route('/userverify1',methods=['POST','GET'])
def userverify1():
	if request.method=='POST':

		uname=request.form['an']
		pws=request.form['pws']
		con=sql.connect("database.db")
		con.row_factory=sql.Row
		cur=con.cursor()
		qry="SELECT * FROM myuser2 WHERE name='"+uname+"' and pass='"+pws+"'"
		cur.execute(qry)
		rows=cur.fetchall()
		if (rows):
		    return render_template('lostform.html',rows=rows)
		else:
			msg="User name or Password is incorrect, make sure you have Signed Up before Login"
			return render_template("result.html",msg=msg)

@app.route('/lost')
def lost():
	return render_template('lostform.html')		


if __name__=='__main__':
	app.run(debug=True)
