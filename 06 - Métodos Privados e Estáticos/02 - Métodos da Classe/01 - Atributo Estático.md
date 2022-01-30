Conhecemos nessa aula os métodos estáticos que podem ser chamados a partir da classe, sem ter um objeto criado. No exemplo abaixo criamos uma classe `Circle` que possui um método estático `get_pi()`:

```
class Circle:

    @staticmethod
    def get_pi():
        return 3.14
```

E agora podemos usar esse método estático a partir da classe:

```
Circle.get_pi()
3.14
```

Repare que o método existe apenas para devolver o valor do `PI`. Nada errado com isso, mas já que usamos um valor simples não bastaria usar um **atributo** simples? Em outras palavras, será que é preciso criar um método? A resposta é não pois podemos usar um atributo da classe. Veja como é simples:

```
class Circle:

    PI = 3.14
```

Repare que não usamos `self` e o atributo nem foi definido dentro do __init__. O atributo faz parte da classe, ou seja, é um atributo estático que pode ser usado sem ter criado um objeto. Veja como fica simples:

```
Circulo.PI
3.14
```