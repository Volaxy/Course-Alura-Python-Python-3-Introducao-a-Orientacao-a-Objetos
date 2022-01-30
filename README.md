# Python 3 - Introdução a Orientação a Objetos

Curso da Alura sobre Orientação à Objetos no Python

## Objetivo Final &#x1F3AF;

Criar uma classe de Conta para simular uma conta de banco usando orientação à objetos

URL do curso -> [Python 3 - Introdução a Orientação a Objetos](https://cursos.alura.com.br/course/python-3-intro-orientacao-objetos/faq)

![Python 3 - Introdução a Orientação a Objetos](https://www.alura.com.br/assets/api/share/curso-python-3-intro-orientacao-objetos.png)

## 01 - O Problema do Paradigma Procedural &#x1F516;
* Dicionário.
* Funções.
* Encapsulamento de código.

### 01 - Dados da Conta
* `from FILE import FUNCTION` importa uma funçao específica de um determinado arquivo.
* Utilizar conjunto de dados como *dicionário* para guardar grandes quantidades de dados semelhantes não é uma boa prática.

### 02 - Dados e Compotamento
* Sem orientação à objetos, é possível criar diferentes variáveis contendo diferentes valores.

## 02 - Classes e Objetos &#x1F516;
* Classes.
* Objetos.
* Função construtora.
* Endereço e referência de objetos.
* Atributos de classe.
* Acesso aos atributos através do objeto.

### 01 - Classe e Objeto
* Criar uma **classe**.
* Criar objetos para criar diferentes tipo de variáveis com características iguais.
* Usar a palavra `pass` para indicar para o compilador que o código ainda será escrito, evitando erros de sintaxe do compilador.
* Criar uma classe usando `CLASS_NAME()`.

### 02 - Construtor
* As características de uma **classe** se chamam **atributos**.
* A função `def __init__(self)` é chamada automaticamente ao construir um objeto.
* O parâmetro `self` é o valor de referência para o **objeto** criado.
* Em `Orientação a Objetos`, as variáveis são denominadas **referências**.
* Em `Orientação a Objetos`, as características são chamadas de **Atributos**.

### 03 - Acessando Atributos
* Para acessar os **Atributos** de determinada classe, usamos `OBJECT_NAME.ATTIBUTE`, acessando primeiro a referência para o objeto criado, em seguida o nome do **atributo**.

## 03 - Implementando Métodos &#x1F516;
* Métodos, que definem o comportamento de uma classe.
* Criação de métodos.
* Como chamar métodos através do objeto.
* Acesso aos atributos através do `self`.
* *Garbage Collector*.
* O tipo `None`.

### 01 - Usando Métodos
* Acessar os métodos através de `OBJECT.METHOD()`.
* O valor `self` nos parâmetros do método é preenchida automaticamente quando o método é chamado.
* A palavra reservada `self` se refere ao objeto atual em que ela está inserida.

### 02 - None e Coletor de Lixo
* Quando um objeto fica sem referência, como:
```
acc = Account(1, "Anny", 500, 1000)
acc = Account(2, "Bia", 500, 1000)
```

A variável `acc` fica sem uma referência para o objeto criado.

Dentro da máquina virtual do Python, existe um processo que descarta as variáveis sem referência, essa ferramenta se chama **Garbage Collector**.
* A palavra reservada `None` desvincula o valor ou referência de uma variável (equivalente ao `null` do Java ou C#).

## 04 - Encapsulamento &#x1F516;
* Atributos privados.
* Encapsulamento de código.
* Encapsulamento da manipulação dos atributos nos métodos.
* Coesão do código.

### 01 - Atributos Privados
* `__` antes do nome do **atributo** o torna um **atributo privado**.
* O **Python** avisa ao desenvolvedor sobre **atributos privados** colocando `_CLASSNAME__ATTIRBUTE` ao acessar os atributos da classe.
* A ação de tornar privado o acesso aos atributos, no mundo Orientado a Objetos, chamamos de **encapsulamento**.

### 02 - Encapsulamento
* Deixar os métodos mais claros utilizando o `self`.

## 05 - Usando Propriedades &#x1F516;
* Métodos de leitura dos atributos, os ***getters***.
* Métodos de modifição dos atributos, os ***setters***.
* Propriedades.

### 01 - Getters e Setters
* Criar métodos **get** usando o `get_ATTRIBUTE` para retornar um atributo.
* Criar métodos **set** usando o `set_ATTRIBUTE` para definir um atributo.

### 02 - Propriedades
* Usar o `@property` para definir uma propriedade de um **atributo** funcionando como um **getter**.
* Usar o `@ATTRIBUTE.setter` para definir um **setter** de um **atributo**.
* A função `title()` retorna a primeira letra da string em maiúscula.

## 06 - Métodos Privados e Estáticos &#x1F516;
* Métodos privados.
* Métodos da classe, os métodos estáticos.

### 01 - Métodos Privados
* Criar **funções privadas** com `__FUNCTION_NAME()`.

### 02 - Métodos da Classe
* Um ***static method*** pertence à **Classe** e não ao **Objeto**.
* Definir um ***static method*** com `@staticmethod`.
* Um **decorator** é uma palavra chave que é precedida por `@`.
* Usar **atributos estáticos**.