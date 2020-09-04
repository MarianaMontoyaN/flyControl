#-*- utf-8 -*-
'''
Written in Python 3.7 
Developed by: MARIANA MONTOYA NARANJO
'''

from tkinter import ttk
from tkinter import *
from tkinter import messagebox
from package import Package
from flight import Flight
from database import database
from dollar_today import dollar_today_scrap
from price_ticket import calculate_price 


'''
MAIN VIEW
'''
class view():

    def __init__(self, window):
        window.title('SOFKA AIRLINES')

        self.option_flight = IntVar()
        self.option_flight_buggage = IntVar()

        window.resizable(False, True)

        #----------------
        # PRICE TICKET
        #----------------

        #Container Frame
        frame1 = LabelFrame(window, text = 'COTIZAR PASAJE')
        frame1.grid(row=0, column=0, columnspan = 3, pady =20)

        # Distance Input
        Label(frame1, text = 'Distancia (Km): ').grid(row = 1, column = 0)
        self.distance = Entry(frame1)
        self.distance.focus()
        self.distance.grid(row = 1, column = 1)

        # Days Input
        Label(frame1, text = 'Días: ').grid(row = 2, column = 0)
        self.days = Entry(frame1)
        self.days.grid(row = 2, column = 1)

        # Button Add Product 
        ttk.Button(frame1, text = 'COTIZAR', command=self.calculate_price_ticket).grid(row = 3, columnspan = 2, sticky = W + E)

        # Output Messages 
        self.message = Label(text = '', fg = 'red')
        self.message.grid(row = 3, column = 0, columnspan = 2, sticky = W + E)

        #----------------
        # PRICE BUGGAGGE
        #----------------

        #Container Frame
        frame2 = LabelFrame(window, text = 'COTIZAR EQUIPAJE')
        frame2.grid(row=4, column=0, columnspan = 3, pady =20)
        
        # Weight Input
        Label(frame2, text = 'Peso (Kg): ').grid(row = 5, column = 0)
        self.weight = Entry(frame2)
        self.weight.focus()
        self.weight.grid(row = 5, column = 1)

        # Flight Input
        Label(frame2, text = 'Vuelo: ').grid(row = 6, column = 0)

        Radiobutton(frame2, text="SA747-1", variable=self.option_flight_buggage, value=1).grid(row = 7, column = 0, columnspan = 1, sticky = W + E, padx=40)
        Radiobutton(frame2, text="SA747-2", variable=self.option_flight_buggage, value=2).grid(row = 7, column = 1, columnspan = 1, sticky = W + E, padx=40)
        Radiobutton(frame2, text="SA747-3", variable=self.option_flight_buggage, value=3).grid(row = 7, column = 2, columnspan = 1, sticky = W + E, padx=40)

        # Button Add Product 
        ttk.Button(frame2, text = 'COTIZAR', command=self.calculate_price_buggagge).grid(row = 8, column = 1, columnspan = 1, sticky = W + E)

        # Output Messages 
        self.message2 = Label(text = '', fg = 'red')
        self.message2.grid(row = 9, column = 0, columnspan = 2, sticky = W + E)

        #----------------
        # INFORMATION FLIGHT
        #----------------

        Label(window, text="INFORMACIÓN DE VUELO").grid(row = 10, column = 0, columnspan = 2, sticky = W + E)

        #Container Frame
        frame3 = LabelFrame(window, text = 'SELECCIONA UN VUELO', width=500)
        frame3.config(width=200)
        frame3.grid(row=11, column=0, columnspan = 3, pady =20)

        Radiobutton(frame3, text="SA747-1", variable=self.option_flight, value=1).grid(row = 11, column = 0, columnspan = 1, sticky = W + E, padx=40)
        Radiobutton(frame3, text="SA747-2", variable=self.option_flight, value=2).grid(row = 11, column = 1, columnspan = 1, sticky = W + E, padx=40)
        Radiobutton(frame3, text="SA747-3", variable=self.option_flight, value=3).grid(row = 11, column = 2, columnspan = 1, sticky = W + E, padx=40)
        ttk.Button(frame3, text = 'BUSCAR', command=self.show_information_flight).grid(row = 12, column=0, columnspan = 1, sticky = W + E)
        ttk.Button(frame3, text = 'MAS INFORMACIÓN', command=self.show_information_flight_additional).grid(row = 12, column=2, columnspan = 1, sticky = W + E)

        # Table
        self.tree = ttk.Treeview(height = 12, columns = ('#1', '#2', '#3', '#4'))
        self.tree.grid(row = 13, column =0, columnspan=2)
        
        self.tree.heading('#1', text = 'ID Paquete', anchor = CENTER)
        self.tree.heading('#2', text = 'Peso (Kg)', anchor = CENTER)
        self.tree.heading('#3', text = 'Precio (COP)', anchor = CENTER)
        self.tree.heading('#4', text = 'Precio (USD)', anchor = CENTER)
        self.tree['show'] = 'headings'


    '''
    FUNCTION OF THE BUTTONS AND DATA VALIDATION
    '''
    
    def calculate_price_ticket(self):
            
        if self.distance.get() == '0' or self.days.get() == '0':
            messagebox.showwarning('ERROR', 'Ingrese un valor válido')
            self.distance.delete(0, END)
            self.days.delete(0, END)
            return
        
        try:
            distance = float(self.distance.get())
            days = int(self.days.get())

        except:
            self.distance.delete(0, END)
            self.days.delete(0, END)
            messagebox.showwarning('ERROR', 'Ingrese un valor válido')
            return

        self.distance.delete(0, END)
        self.days.delete(0, END)

        result_price_ticket, discount = calculate_price(days, distance)

        self.message['text'] = 'PRECIO: COP {}'.format(result_price_ticket)

        if discount == True:
            messagebox.showinfo('DESCUENTO', 'Su viaje aplicó para un descuento del 30% ¡FELICITACIONES!')
        
            

    def calculate_price_buggagge(self):

        try:
            weight = int(self.weight.get())
        
        except:
            self.weight.delete(0,END)
            messagebox.showwarning('ERROR', 'Ingrese un valor válido')
            return


        if weight > 500:
            messagebox.showwarning('ERROR', 'El peso del paquete no puede sobrepasar los 500 Kg')
            self.weight.delete(0,END)
            return

        if weight == 0:
            messagebox.showwarning('ERROR', 'Ingrese un valor válido')
            self.weight.delete(0,END)
            return

        if self.option_flight_buggage.get() == 0:
            messagebox.showwarning('ERROR', 'Seleccione un vuelo')
            self.weight.delete(0,END)
            return

        else:
            response = messagebox.askquestion('ACTUALIZAR TMR', '¿DESEA ACTUALIZAR EL TMR AL DÍA DE HOY?')
            if response == 'yes':
                try:
                    dollar_today = dollar_today_scrap()
                    
                except:
                    dollar_today = 3500
                    messagebox.showwarning('ALERTA', 'El precio del dolar ha sido calculado con el TMR por defecto de COP 3500. Verifique la conexión a internet para actualizar TMR')

            else:

                dollar_today = 3500
                messagebox.showwarning('ALERTA', 'El precio del dolar ha sido calculado con el TMR por defecto de COP 3500')
            
            pesos = Package(weight, dollar_today).price_pesos
            dollars = Package(weight, dollar_today).price_dollar

            self.message2['text'] = 'PRECIO: COP {} - USD {} (TMR = {})'.format(pesos, dollars, dollar_today)
            
            flight = str(self.option_flight_buggage.get())
            object_Flight = Flight('vuelo'+flight)
            capacity = object_Flight.add_package(weight, pesos, dollars)
            self.option_flight.set(self.option_flight_buggage.get())
            self.show_information_flight()

            if capacity == False :
                messagebox.showwarning('ALERTA', 'No se agrego tu paquete. \n Limite máximo de carga alcanzado. Elija otro vuelo')

        self.weight.delete(0,END)

    
    def show_information_flight(self):

        self.tree.delete(*self.tree.get_children())

        if self.option_flight.get() == 0:
            messagebox.showwarning('ERROR', 'Seleccione un vuelo')
            return

        flight = str(self.option_flight.get())

        list_packages = database.show_packages('vuelo'+flight)

        for package in list_packages:
            self.tree.insert('', 0, values=('SA747'+'-'+flight+'-'+str(package[0]), package[1], package[2], package[3]))

    def show_information_flight_additional(self):

        number_flight = str(self.option_flight.get())

        flight = Flight('vuelo'+number_flight)
        number_packages = flight.number_packages
        package_ligther, package_heavier = flight.heavier_lighter_package()
        average_weight = flight.average_weight()
        total_pesos = flight.income_pesos()
        total_dollars = flight.income_dollars()
        total_weight = flight.total_weight

        messagebox.showinfo('INFORMACIÓN ADICIONAL', 'En el vuelo: {} \n\n Hay {} paquetes \n El paquete más pesado pesa: {} Kg \n El paquete más liviano pesa: {} Kg \n El peso promedio de un paquete es: {} Kg\n La carga total es de: {} Kg \n\n Ingresos por concepto de carga: \n COP {} \n USD {}'.format('SA747-'+number_flight, number_packages, package_heavier, package_ligther, average_weight, total_weight, total_pesos, total_dollars))


if __name__ == '__main__':

    window = Tk()
    show = view(window)
    

    exists = database.create_db()
    
    print('BASE DATOS CREADA')

    if exists == False:

        database.default_data(3500)
        print('TABLAS CREADA')

    window.mainloop()
    