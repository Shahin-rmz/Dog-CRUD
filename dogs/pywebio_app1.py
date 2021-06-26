#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from pywebio.output import *
from pywebio.pin import *
from pywebio.session import hold,set_env
from .models import Dog
from functools import partial
from collections import OrderedDict

def page1():                    #defining the page
    set_env(title = 'Dog App')    #defining page title
    def tableFunc():                            #function of deleting the entries

        def deletion(self, primary_key):
            d = Dog.objects.get(pk = primary_key)
            d.delete()
            toast('row %s  deleted' %primary_key ,position ='right' ,color = 'warn')
            with use_scope('table1',clear = True):            #function of refreshing the screen after deleting
                put_table([[i.pk,i.nickname,i.weight,i.food,
                            put_buttons(['del'],onclick =partial(deletion,primary_key = i.pk)),                    #nested delete function inside refreshed page
                            put_buttons(['edit'],onclick = partial(popupfunc,iterative_key = i))]                                    #nested edit function inside refreshed page
                           for i in Dog.objects.all()],header = ['PK','Nick Name','Weight','Food'])


        with use_scope('table1',clear = True):                #refreshes the stable screen without 
            put_table([[i.pk,i.nickname,i.weight,i.food,
                        put_buttons(['del'],onclick =partial(deletion,primary_key = i.pk)),           #showing the delete and edit button inside a page without any change
                        put_buttons(['edit'],onclick = partial(popupfunc,iterative_key = i))]
                       for i in Dog.objects.all()],header = ['PK','Nick Name','Weight','Food'])

    
    def popupfunc(self,iterative_key):
        @popup('edit pop up')
        def show():
            put_row([put_input('NewName',placeholder = iterative_key.nickname,label = 'Nick Name'),None,
                     put_input('NewWeight',placeholder = iterative_key.weight, type = 'number',label = 'Weight'),None,
                     put_input('NewFood',placeholder = iterative_key.food, label = 'Food')])

            databasedict = {'nickname':'','weight':'','food':''}
            def updatefunc(self):

               databasedict.update({'nickname': pin.NewName})
               databasedict.update({'weight': pin.NewWeight})
               databasedict.update({'food': pin.NewFood})
               for key, value in databasedict.items():
                   if value != '' and value is not None:
                       e = Dog.objects.get(pk = iterative_key.pk)
                       setattr(e,key,value)
                       e.save()
                       tableFunc()
                       close_popup()
                       toast('row %s edited' %iterative_key.pk,position = 'right',color = 'success')

                       
                
            
            put_buttons(['submit'],onclick = partial(updatefunc))


        show()


    put_row([put_input('name' , ), None,                         #getting the inputs from user 
             put_input('weight',type = 'number',placeholder = 'insert an integer' ), None,
             put_input('food')])

    def ToDataBase(self):                         #inserting to database
        a = Dog(nickname = pin.name,weight = pin.weight, food = pin.food)
        a.save()
        tableFunc()

    put_buttons(['insert'],partial(ToDataBase)) #shows the button
    tableFunc()

    hold()
