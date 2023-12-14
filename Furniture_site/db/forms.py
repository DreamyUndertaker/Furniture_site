from .models import Articles, Clients, Deposites, DepositsRegistration, ExchangeRates, Persons
from django.forms import ModelForm, TextInput

class ArticleForm(ModelForm):
    class Meta:
        model = Articles
        fields = ['title', 'full_text']

        widgets = {
            'title': TextInput(attrs={
                
                'placeholder': 'название жалобы'
            }),
            'full_text': TextInput(attrs={
                
                'placeholder': 'описание жалобы'
            }),
        }

class PersonsForm(ModelForm):
    class Meta:
        model = Persons
        fields = ['surnamePersons', 'namePersons', 'fatherNamePersons', 'jobTitlePersons', 'salaryPersons']
        widgets = {
            'surnamePersons': TextInput(attrs={

                'placeholder': 'Фамилия работника'
            }),
            'namePersons': TextInput(attrs={

                'placeholder': 'Имя работника'
            }),
            'fatherNamePersons': TextInput(attrs={

                'placeholder': 'Фамилия работника'
            }),
            'jobTitlePersons': TextInput(attrs={

                'placeholder': 'Должность работника'
            }),
            'salaryPersons': TextInput(attrs={

                'placeholder': 'ЗП работника'
            }),

        }
class DepositesForm(ModelForm):
    class Meta:
        model = Deposites
        fields = ['depositeCode', 'depositeName', 'minDepositePeriod', 'minDepositeValue', 'currencyCode', 'interestRate']
        widgets = {
            'depositeCode': TextInput(attrs={

                'placeholder': 'код вклада'
            }),
            'depositeName': TextInput(attrs={

                'placeholder': 'наименование депозита'
            }), 
            'minDepositePeriod': TextInput(attrs={

                'placeholder': 'минимальный срок вклада'
            }),
            'minDepositeValue': TextInput(attrs={

                'placeholder': 'минимальная сумма вклада'
            }),
            'currencyCode': TextInput(attrs={

                'placeholder': 'код валюты'
            }),
            'interestRate': TextInput(attrs={

                'placeholder': 'процентная ставка, годовая'
            }),
        }
class ClientsForm(ModelForm):
    class Meta:
        model = Clients
        fields = ['surnameClient', 'nameClient', 'fatherNameClient']

        widgets = {
            'surnameClient': TextInput(attrs={
                
                'placeholder': 'Фамилия'
            }),
            'nameClient': TextInput(attrs={
                
                'placeholder': 'Имя'
            }),
            'fatherNameClient': TextInput(attrs={
                
                'placeholder': 'Отчество'
            }),
        }
class ExchangeRatesForm(ModelForm):
    class Meta:
        model = ExchangeRates
        fields = ['ratesName', 'exchangeRate']

        widgets = {
            'ratesName': TextInput(attrs={
                
                'placeholder': 'Наименование'
            }),
            'exchangeRate': TextInput(attrs={
                
                'placeholder': 'Обменный курс'
            }),
        }
class DepositsRegistrationForm(ModelForm):
    class Meta:
        model = DepositsRegistration
        fields = [
            'surnameClient', 'nameClient', 'fatherNameClient', 'depositeCode', 
            'depositeDateStart', 'depositeDateEnd', 'depositeSum', 'depositeStatus',
            'surnamePersons', 'namePersons', 'fatherNamePersons'       
        ]

        widgets = {
            'surnameClient': TextInput(attrs={
                
                'placeholder': 'Фамилия клиента'
            }),
            'nameClient': TextInput(attrs={
                
                'placeholder': 'Имя клиента'
            }),
            'fatherNameClient': TextInput(attrs={
                
                'placeholder': 'Отчество клиента'
            }),
            'depositeCode': TextInput(attrs={
                
                'placeholder': 'Код вклада'
            }),
            'depositeDateStart': TextInput(attrs={
                
                'placeholder': 'Дата открытия вклада'
            }),
            'depositeDateEnd': TextInput(attrs={
                
                'placeholder': 'Дата закрытия вклада'
            }),
            'depositeSum': TextInput(attrs={
                
                'placeholder': 'Сумма вклада'
            }),
            'depositeStatus': TextInput(attrs={
                
                'placeholder': 'Статус вклада'
            }),
            'surnamePersons': TextInput(attrs={
                
                'placeholder': 'Фамилия работника'
            }),
            'namePersons': TextInput(attrs={
                
                'placeholder': 'Имя работника'
            }),
            'fatherNamePersons': TextInput(attrs={
                
                'placeholder': 'Отчество работника'
            }),
        }
