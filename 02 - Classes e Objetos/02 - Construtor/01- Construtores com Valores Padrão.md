Imagine que uma conta bancária no banco **AluraInvest** geralmente é criada com limite de mil reais.

O código de criação de 3 objetos do tipo `Account` fica assim:
```
account1 = Account(1, "Fulano", 0.0, 1000.0)
account2 = Account(2, "Beltrano", 0.0, 1000.0)
account3 = Account(3, "Sicrano", 0.0, 2000.0)
```

Como podemos fazer no Python para economizar a escrita do código de criação de um objeto `Account`? Neste caso podemos supor que apenas as `accounts com limites especiais` precisariam passar tal argumento (no exemplo acima apenas `account3` tem um limite especial). Isso é feito colocando na declaração da função construtora `__init__` um valor padrão para o limite.

Assim:
```
class Account:

    def __init__(self, number, holder, balance, limit = 1000.0):
        self.number = number
        self.holder = holder
        self.balance = balance
        self.limit = limit
```

E o código de nossos 3 objetos ficaria assim:
```
account1 = Account(1, "Fulano", 0.0)
account2 = Account(2, "Beltrano", 0.0)
account3 = Account(3, "Sicrano", 0.0, 2000.0)
```