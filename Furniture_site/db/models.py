from django.db import models


# Create your models here.
class Articles(models.Model):
    title = models.CharField('название', max_length=50)
    full_text = models.TextField('содержание')
    
    def __str__(self):
        return f'Заявка: {self.title}'
    
    class Meta:
        verbose_name = 'заявка'
        verbose_name_plural = 'заявок'

class Persons(models.Model):
    surnamePersons = models.TextField('Фамилия')
    namePersons = models.TextField('Имя')
    fatherNamePersons = models.TextField('Отчество')
    jobTitlePersons = models.TextField('Должности')
    salaryPersons = models.PositiveBigIntegerField('Оклад')

    def __str__(self):
        return f'Сотрудники банка и их должности: {self.title}'
    class Meta:
        verbose_name = 'Сотрудники банка'
        verbose_name_plural = 'Сострудников банка'

class Deposites(models.Model):
    CHOICES_CATEGORY = (
        ('Cumulative', 'накопительный'),
        ('Universal', 'универсальный')
    )
    CHOICES_CURRENCY = (
        ('Rub', 'Рубли'),
        ('Us', 'Доллары'),
        ('Eu', 'Евро')
    )
    depositeCode = models.IntegerField('Код вклада')
    depositeName = models.CharField(
        'Наименование депозита',
        max_length=10, 
        choices=CHOICES_CATEGORY
        )
    minDepositePeriod = models.IntegerField('Минимальный срок вклада')
    minDepositeValue = models.IntegerField('Минимальная сумма вклада')
    currencyCode = models.CharField(
        'Код валюты', 
        max_length=6, 
        choices=CHOICES_CURRENCY
        )
    interestRate = models.IntegerField('Процентная ставка, годовая')

    def __str__(self):
        return f'Виды вкладов: {self.title}'
    class Meta:
        verbose_name = 'Виды вкладов'
        verbose_name_plural = 'Виды вкладов'

class ExchangeRates(models.Model):
    CHOICES_RATE = (
        ('rub', 'рубли'),
        ('us', 'доллары США'),
        ('eu', 'евро')
    )
    ratesName = models.CharField('Наименование', choices=CHOICES_RATE, max_length=40)
    exchangeRate = models.FloatField('Обменный курс')

    def __str__(self):
        return f'Обменный курс : {self.title}'
    class Meta:
        verbose_name = 'Обменный курс'
        verbose_name_plural = 'Обменный курс'

class Clients(models.Model):
    surnameClient = models.TextField('Фамилия')
    nameClient = models.TextField('Имя')
    fatherNameClient = models.TextField('Отчество')

    def __str__(self):
        return f'Клиенты банка: {self.title}'
    class Meta:
        verbose_name = 'Клиенты банка'
        verbose_name_plural = 'Клиентов банка'

class DepositsRegistration(models.Model):
    surnameClient = models.TextField('Фамилия')
    nameClient = models.TextField('Имя')
    fatherNameClient = models.TextField('Отчество')

    depositeCode = models.IntegerField('Код вклада')
    depositeDateStart = models.DateField('дата открытия вклада')
    depositeDateEnd = models.DateField('дата закрытия вклада')
    depositeSum = models.IntegerField('сумма вкалада')
    CHOICES_STATUS = (
        ('close', 'закрыт'),
        ('in progress', 'действует')
    )
    depositeStatus = models.CharField('Статус вклада', choices=CHOICES_STATUS, max_length=20)
    surnamePersons = models.TextField('Фамилия')
    namePersons = models.TextField('Имя')
    fatherNamePersons = models.TextField('Отчество')

    def __str__(self):
        return f'Регистрация вкладов: {self.title}'
    class Meta:
        verbose_name = 'Регистрация вкладов'
        verbose_name_plural = 'Регистрация вкладов'



    

