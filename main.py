import sys
from PyQt6.uic import loadUi
from PyQt6 import QtWidgets
from PyQt6.QtWidgets import QDialog, QApplication
from PyQt6.QtGui import QIcon
import sqlite3


class WelcomeScreen(QDialog):
    def __init__(self):
        super(WelcomeScreen, self).__init__()
        loadUi("welcomescreen.ui", self)
        self.login.clicked.connect(self.gotologin)
        self.create.clicked.connect(self.gotocreate)

    def gotologin(self):
        login = LoginScreen()
        widget.addWidget(login)
        widget.setCurrentIndex(widget.currentIndex() + 1)

    def gotocreate(self):
        create = CreateAccScreen()
        widget.addWidget(create)
        widget.setCurrentIndex(widget.currentIndex() + 1)


class LoginScreen(QDialog):
    def __init__(self):
        super(LoginScreen, self).__init__()
        loadUi("login.ui", self)
        self.passwordfield.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)
        self.login.clicked.connect(self.loginfunction)
        self.backHome.clicked.connect(self.back_to_home)

    def back_to_home(self):
        welcome_back = WelcomeScreen()
        widget.addWidget(welcome_back)
        widget.setCurrentIndex(widget.currentIndex() + 1)

    def loginfunction(self):
        user = self.emailfield.text()
        password = self.passwordfield.text()

        if len(user) == 0 or len(password) == 0:
            self.error.setText("Please input all fields.")
        else:
            try:
                conn = sqlite3.connect("cafe.db")
                cur = conn.cursor()
                query = 'SELECT id, password FROM customers WHERE username = ?'
                cur.execute(query, (user,))
                result = cur.fetchone()

                if result and result[1] == password:
                    print("Successfully logged in.")
                    fillprofile = Backcode()
                    widget.addWidget(fillprofile)
                    widget.setCurrentIndex(widget.currentIndex() + 1)
                    self.error.setText("")
                else:
                    self.error.setText("Username or password incorrect.")
            except Exception as e:
                self.error.setText("Database error: " + str(e))
            finally:
                conn.close()


class CreateAccScreen(QDialog):
    def __init__(self):
        super(CreateAccScreen, self).__init__()
        loadUi("createacc.ui", self)
        self.passwordfield.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)
        self.confirmpasswordfield.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)
        self.signup.clicked.connect(self.signupfunction)
        self.backHome.clicked.connect(self.back_to_home)

    def back_to_home(self):
        welcome_back = WelcomeScreen()
        widget.addWidget(welcome_back)
        widget.setCurrentIndex(widget.currentIndex() + 1)

    def signupfunction(self):
        user = self.emailfield.text()
        password = self.passwordfield.text()
        confirmpassword = self.confirmpasswordfield.text()

        if len(user) == 0 or len(password) == 0 or len(confirmpassword) == 0:
            self.error.setText("Please fill in all inputs.")
        elif password != confirmpassword:
            self.error.setText("Passwords do not match.")
        else:
            try:
                conn = sqlite3.connect("cafe.db")
                cur = conn.cursor()

                user_info = [user, password]
                cur.execute('INSERT INTO customers (username, password) VALUES (?, ?)', user_info)
                conn.commit()
                self.error.setText("Account created successfully!")
                fillprofile = Backcode()
                widget.addWidget(fillprofile)
                widget.setCurrentIndex(widget.currentIndex() + 1)

            except Exception as e:
                self.error.setText("Error creating account: " + str(e))
            finally:
                conn.close()


class Backcode(QDialog):
    def __init__(self):
        super(Backcode, self).__init__()
        loadUi("menu.ui", self)
        self.spinBox_americano = self.findChild(QtWidgets.QSpinBox, 'americano')
        self.spinBox_applejuice = self.findChild(QtWidgets.QSpinBox, 'applejuice')
        self.spinBox_coldbrew = self.findChild(QtWidgets.QSpinBox, 'coldbrew')
        self.spinBox_cortado = self.findChild(QtWidgets.QSpinBox, 'cortado')
        self.spinBox_cuppo = self.findChild(QtWidgets.QSpinBox, 'cuppo')
        self.spinBox_dripcoffee = self.findChild(QtWidgets.QSpinBox, 'dripcoffee')
        self.spinBox_espresso = self.findChild(QtWidgets.QSpinBox, 'espresso')
        self.spinBox_icetea = self.findChild(QtWidgets.QSpinBox, 'icetea')
        self.spinBox_kambucha = self.findChild(QtWidgets.QSpinBox, 'kambucha')
        self.spinBox_latte = self.findChild(QtWidgets.QSpinBox, 'latte')
        self.spinBox_mocha = self.findChild(QtWidgets.QSpinBox, 'mocha')
        self.spinBox_soda = self.findChild(QtWidgets.QSpinBox, 'soda')
        self.spinBox_macchiato = self.findChild(QtWidgets.QSpinBox, 'macchiato')
        self.spinBox_tea = self.findChild(QtWidgets.QSpinBox, 'tea')

        self.finishbtn.clicked.connect(self.submit)
        self.ppbtn.clicked.connect(self.paymentp)

    def paymentp(self):
        payment_page = payp()
        widget.addWidget(payment_page)
        widget.setCurrentIndex(widget.currentIndex() + 1)
        print("Successfully submitted")

    def submit(self):
        try:
            self.value = self.spinBox_americano.value()
            self.value1 = self.spinBox_applejuice.value()
            self.value2 = self.spinBox_coldbrew.value()
            self.value3 = self.spinBox_cortado.value()
            self.value4 = self.spinBox_cuppo.value()
            self.value5 = self.spinBox_dripcoffee.value()
            self.value6 = self.spinBox_espresso.value()
            self.value7 = self.spinBox_icetea.value()
            self.value8 = self.spinBox_kambucha.value()
            self.value9 = self.spinBox_latte.value()
            self.value10 = self.spinBox_mocha.value()
            self.value11 = self.spinBox_soda.value()
            self.value12 = self.spinBox_macchiato.value()
            self.value13 = self.spinBox_tea.value()

            conn = sqlite3.connect("cafe.db")
            cur = conn.cursor()

            drink_list = [
                ("americano", self.value), ("applejuice", self.value1), ("coldbrew", self.value2),
                ("cortado", self.value3), ("cuppo", self.value4), ("dripcoffee", self.value5),
                ("espresso", self.value6), ("icetea", self.value7), ("kambucha", self.value8),
                ("latte", self.value9), ("mocha", self.value10), ("soda", self.value11),
                ("macchiato", self.value12), ("tea", self.value13)
            ]

            for drink, amount in drink_list:
                if amount > 0:
                    cur.execute('SELECT amount FROM menu WHERE drink_name = ?', (drink,))
                    stock = cur.fetchone()[0]
                    if stock < amount:
                        self.error.setText(f"Not enough {drink} in stock.")
                        return

            for drink, amount in drink_list:
                if amount > 0:
                    cur.execute('UPDATE menu SET amount = amount - ? WHERE drink_name = ?', (amount, drink))

            total_sum = sum([
                self.value * 3, self.value1 * 4, self.value2 * 4, self.value3 * 4,
                self.value4 * 4, self.value5 * 2.75, self.value6 * 3, self.value7 * 3.5,
                self.value8 * 5, self.value9 * 4.5, self.value10 * 4.5, self.value11 * 3,
                self.value12 * 3.5, self.value13 * 3
            ])

            user_id = self.user_id.text()
            cur.execute('SELECT id FROM customers WHERE username = ?', (user_id,))
            customer_id = cur.fetchone()

            if customer_id:
                # Save total_sum to the payments table
                cur.execute('INSERT OR REPLACE INTO payments (customer_id, price) VALUES (?, ?)', (customer_id[0], total_sum))
                conn.commit()
                self.error.setText(f"Order successful! Total: {total_sum}")
            else:
                self.error.setText("User not found.")

        except Exception as e:
            self.error.setText(f"Error: {str(e)}")
        finally:
            conn.close()


class payp(QDialog):
    def __init__(self):
        super(payp, self).__init__()
        loadUi("payp.ui", self)
        self.backHome.clicked.connect(self.back_to_home)
        try:
            conn = sqlite3.connect("cafe.db")
            cur = conn.cursor()
            cur.execute('SELECT order FROM payments ORDER BY id DESC LIMIT 1')
            global last_record
            last_record = cur.fetchone()
            conn.commit()
        except :
            self.error.setText("some trouble in connecting to database")
        finally:
            conn.close()
        self.error.setText(last_record)
        self.paybtn.clicked.connect(self.payp)
    def payp(self):
        pay = self.pay.text()
        if pay == last_record :
            self.error.setText("successfully paid")
            try :
                conn = sqlite3.connect("cafe.db")
                cur = conn.cursor()
                cur.execute('UPDATE customers SET price = price + 1')
                conn.commit()
                conn.close()
            except Exception as e:
                self.error.setText(f"Error: {str(e)}")
        else:
            self.error.setText("not enough")
    def back_to_home(self):
        welcome_back = Backcode()
        widget.addWidget(welcome_back)
        widget.setCurrentIndex(widget.currentIndex() + 1)

app = QApplication(sys.argv)
app.setApplicationName("My Cafe App")
app.setWindowIcon(QIcon("icon.png"))
welcome = WelcomeScreen()
widget = QtWidgets.QStackedWidget()
widget.addWidget(welcome)
widget.setFixedHeight(800)
widget.setFixedWidth(1200)
widget.show()

try:
    sys.exit(app.exec())
except:
    print("Exiting...")
#
