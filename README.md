<!DOCTYPE html>
<html lang ="pt-br">
<head>
<meta charset= "UTF-8">
</head>
<body>	
<a name = "home"></a>
	

	
	
<div align="center"><img width="30%"src="https://github.com/RayaneGomes97/Imagens/blob/master/img%20python.jpg"></div> <br><br>
<br><Br>

<table align ="center">
  <tr>
    <td align ="center" > Conteudo </td>
    <td align ="center">  Exercícios </td>
  </tr>
	
  <tr>
    <td> 
     <ol> 
	<li><a href = "#topico1">  Alterar título do tópico 1 </a> </li>
	<li><a href = "#topico2">  Alterar título do tópico 2 </a> </li>
	<li><a href = "#topico3">  Alterar título do tópico 3 </a> </li>
	<li><a href = "#topico4">  Alterar título do tópico 4 </a> </li>
	<li><a href = "#topico4">  Alterar título do tópico 5 </a> </li>
        <li><a href = "#modulos"> Utilizando módulos</a> </li>
        <li><a href = "#erro"> Tocando .mp3 em python [CÓDIGO COM ERRO] </a> </li>
        <li><a href = "#strings"> Manipulando strings  </a> </li>
        <li><a href = "#coresterminal"> Implementando cores no terminal </a> </li>	     
     </ol>
     </td><td> 
     <ol> 
        <li> <a href= "https://github.com/RayaneGomes97/Estudos-Python3/tree/master/Todos%20os%20exerc%C3%ADcios/Curso%20em%20V%C3%ADdeo%20-%20Gustavo%20Guanabara"> Exercicios - Curso em vídeo </a> </li>
     </ol>
    </tr>
</table>   <br>

💻 <- Clicando aqui você retornará ao menu


<!--------------------------------------------------------------------------------------------------- -->
<a name="topico1"></a>
<h2><a href="#home"> 💻</a> Alterar título do tópico 1 </h2>

<p> Acrescentar um conteudo aqui </>
<!--------------------------------------------------------------------------------------------------- -->
<a name="topico2"></a>
<h2><a href="#home"> 💻</a> Alterar título do tópico 2 </h2>

<p> Acrescentar um conteudo aqui </>
<!--------------------------------------------------------------------------------------------------- -->
<a name="topico3"></a>
<h2><a href="#home"> 💻</a> Alterar título do tópico 3 </h2>

<p> Acrescentar um conteudo aqui </>

<!--------------------------------------------------------------------------------------------------- -->
<a name="topico4"></a>
<h2><a href="#home"> 💻</a> Alterar título do tópico 4 </h2>

<p> Acrescentar um conteudo aqui </>

<!--------------------------------------------------------------------------------------------------- -->
<a name="topico5"></a>
<h2><a href="#home"> 💻</a> Alterar título do tópico 5 </h2>

<p> Acrescentar um conteudo aqui </>


<!--------------------------------------------------------------------------------------------------- -->
<a name="modulos"></a>
<h2><a href="#home"> 💻</a> Utilizando módulos </h2>

<p> Veja como carregar bibliotecas de funções e utilizar vários recursos adicionais nos seus programas utilizando módulos built-in e módulos externos. </p>

<table>
</tr><tr>
    <td> Biblioteca  </td>
    <td> Descrição </td>
</tr><tr>
    <td> Math  </td>
    <td> Este módulo fornece acesso às funções matemáticas definidas pelo padrão C. </td></tr
</tr><tr>
    <td> Random  </td>
    <td>Este módulo implementa geradores de números pseudo-aleatórios para várias distribuições.
</td></tr>
</table>

<p> Para acessar maiores informações acesse a documentação: https://docs.python.org/ </p>

<h3> Alguns métodos já vistos </h3>

<table>
</tr><tr>
    <th> Biblioteca MATH  </th>
    <th> Métodos </th>
</tr><tr>
    <td> math.pow  </td>
    <td> A função Math.pow() retorna a base elevada ao expoente power, ou seja, (base, expoente). </td>
</tr><tr>
    <td> math.floor  </td>
    <td> Retorna o valor de um número arredondado para baixo </td>
</tr><tr>
    <td> math.ceil  </td>
    <td> Retorna o valor de um número arredondado para cima </td>
</tr><tr>
    <td> math.hypot  </td>
    <td> Retorna a raiz quadrada do somátorio do quadrado de seus parâmetros. </td>
</tr><tr>
    <td> math.radius  </td>
    <td> Converte um ângulo de radianos em grau </td>
</tr><tr>
    <td> math.trunc  </td>
    <td> Retorna a parte inteira de um número, descartando suas casas decimais.. </td>
</tr>
</table>


	

<h3> Aprendendo a carregar biblioteca de funções </h3>

```
import math #Importando TODAS as funções da biblioteca math.

#Para  importar apenas algumas funções específicas, eis um exemplo de como seria:

#from math import sqrt           Dessa forma apenas sqrt seria importado

```

<h3> [EXAMPLO DE RANDOM] Gerando um número aleatório de 1 a 10 </h3>

```
import random
num = random.randint(1,10) #Gerando numeros aleatórios inteiros de 1 a 10 e armazenando na variavel num.

# OUTRO EXEMPLO: 

# num = random.random() Random da classe random gera números aleatórios (floats) entre 0 e 1.
print(num)
```

<table>
	<strong> OBS: </strong> Se você digitar import e clicar ctrl + espaço irá conseguir acesso a todas bibliotecas que você poderá importar. 
</table>

<!--------------------------------------------------------------------------------------------------- -->
<a name="erro"></a>
<h2><a href="#home"> 💻</a> Tocando um mp3 em python [Não funcionou!] </h2>

<h3> Observações: </h3>


<ul>
<li><strong> Módulo:          </strong> Usando módulos no Python [14 aulas] </li>
<li><strong> Aula:           </strong>  Exercício 21 - Tocando um mp3 </li>
<li><strong> Código com erro </strong>- 27/08/2020 </li>
<li><strong>Pesquisas indicam que o módulo Pygame sofreu atualizações. </strong>  </li>

</ul>

<p> Código proposto pela aula: </p>

```
import pygame

pygame.init() # É necessário inicializar a biblioteca pygame
pygame.mixer.music.load('ex021.mp3') # Arquivo precisa estar no mesmo caminho do projeto.
pygame.mixer.music.play()
pygame.event.wait()
```
<!--------------------------------------------------------------------------------------------------- -->
<a name="strings"></a>
<h2><a href="#home"> 💻</a> Manipulando Strings - Operadores e fatiamento de sequências </h2>

<p>O indice sempre inicia no zero e na contagem descartamos o ultimo indice. Exemplo: </p>

<p>frase = 'Curso em Vídeo' </p>

<table>
<thead>
  <tr>
    <th>C</th>
    <th>u</th>
    <th>r</th>
    <th>s</th>
    <th>o</th>
    <th></th>
    <th>e</th>
    <th>m</th>
    <th></th>
    <th>v</th>
    <th>i</th>
    <th>d</th>
    <th>e</th>
    <th>o</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td>0</td>
    <td>1</td>
    <td>2</td>
    <td>3</td>
    <td>4</td>
    <td>5</td>
    <td>6</td>
    <td>7</td>
    <td>8</td>
    <td>9</td>
    <td>10</td>
    <td>11</td>
    <td>12</td>
    <td>13</td>
  </tr>
</tbody>
</table>

<!-- ----------------------------------------------- -->

<table>
  <tr>
    <td>frase[0:6]</td>
    <td>Exibe o valor do indice 0 até o 5.</td>
  </tr><tr>
    <td>frase[9:13]</td>
    <td>Exibe o valor do indice 9 até o 12.</td>
  </tr><tr>
    <td>frase[9:]</td>
    <td>Exibe o valor do indice 9 até o final.</td>
  </tr><tr>
    <td>frase[2:11:3]</td>
    <td>Exibe o valor do indice 2 até o 11 pulando de 3 em 3.</td>
  </tr><tr> 
    <td>frase[9::2]</td>
    <td>Exibe o valor do indice 9 até o final pulando de 2 em 2.</td>
  </tr><tr>
</table>

<!-- ----------------------------------------------- -->
<table>
<thead>
  <tr>
    <th>len(frase)</th>
    <th>Contar a quantidade de caracteres da variavel frase</th>
  </tr>
</thead>
<tbody>
<tr>
    <td>len(frase)</td>
    <td>Exibe o comprimento da variavel frase. Irá exibir 13 na tela</td>
</tr><tr>
    <td>frase.count('o')</td>
    <td>Conta quantos caracteres 'o' existem na variavel frase</td>
</tr><tr>
    <td>frase.count('o',0,13)</td>
    <td>Conta quantos caracteres 'o' existem do intervalo do indice 0 até o 12</td>
</tr><tr>
    <td>frase.find('deo')</td>
    <td>Irá apontar em quais indice vezes encontrou 'deo'. Nesse exemplo acima exibiria 11. Se a string 'deo' não existisse ele retornaria -1</td>
  </tr><tr>
    <td>'Curso' in frase</td>
    <td> Operador in Verifica se existe uma palavra na sring, irá retornar true ou false.</td>
  </tr><tr>
    <td>frase.replace('Python','android')</td>
    <td> Irá encontrar 'Python' e substituir por 'Android'.</td>
  </tr><tr>
    <td>frase.upper()</td>
    <td> É um método responsável a tornar todas os caracteres da string em MAIUSCULO. </td>
  </tr><tr>
    <td>frase.lower()</td>
    <td> É um método responsável a tornar todas os caracteres da string em minusculo. </td>
  </tr><tr>
    <td>frase.capitalize()</td>
    <td> Transforma  todos caracteres em minusculo e torna apenas o primeiro e maiusculo </td>
  </tr><tr>
    <td>frase.title()</td>
    <td> Analise as palavras da string e coloca todos caracteres iniciais em maiusculo </td>
  </tr><tr>
    <td>frase.title('')</td>
    <td> Analise as palavras da string e coloca todos caracteres iniciais em maiusculo </td>
  </tr><tr>
    <td>frase.strip('')</td>
    <td> Remove todos espaços inuteis que existir no inicio e depois do final da string. </td>
  </tr><tr>
    <td>frase.rstrip()</td>
    <td> Remove os espaços inuteis somente do lado direito, ou seja, os ultimos espaços da string. </td>
  </tr><tr>
    <td>frase.lstrip()</td>
    <td> Remove os espaços inuteis somente do lado esquerdo, ou seja, os primeiros espaços da string. </td>
  </tr>
</tbody>
</table>
<!-- -------------- -->
<h3> Divisãoo de strings </h3>

<table>
  <tr>
    <td>frase.split()</td>
    <td> Irá dividir as palavras e criar uma indexação nova para elas. Em outras palavras, ele irá gerar uma lista para cada palavra da cadeia de caracteres. Exemplo: </p>
</table>
<table>

  <tr>
    <th>C</th>
    <th>u</th>
    <th>r</th>
    <th>s</th>
    <th>o</th>
    <th></th>
    <th>e</th>
    <th>m</th>
    <th></th>
    <th>v</th>
    <th>i</th>
    <th>d</th>
    <th>e</th>
    <th>o</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td>0</td>
    <td>1</td>
    <td>2</td>
    <td>3</td>
    <td>4</td>
    <td></td>
    <td>0</td>
    <td>1</td>
    <td></td>
    <td>0</td>
    <td>1</td>
    <td>2</td>
    <td>3</td>
    <td>4</td>
  </tr>
</table>
<!--- ----------->

<table>
  <tr>
    <td>'-'.jon(frase)</td>
    <td> Irá separar todas as palavras com hífem - invés de espaçamento. </p>
</table>
<table>
<thead>
  <tr>
    <th>C</th>
    <th>u</th>
    <th>r</th>
    <th>s</th>
    <th>o</th>
    <th>-</th>
    <th>e</th>
    <th>m</th>
    <th>-</th>
    <th>v</th>
    <th>i</th>
    <th>d</th>
    <th>e</th>
    <th>o</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td>0</td>
    <td>1</td>
    <td>2</td>
    <td>3</td>
    <td>4</td>
    <td>5</td>
    <td>6</td>
    <td>7</td>
    <td>8</td>
    <td>9</td>
    <td>10</td>
    <td>11</td>
    <td>12</td>
    <td>13</td>
  </tr>
</tbody>
</table
<!--------------------------------------------------------------------------------------------------- -->
<a name="condicao"></a>
<h2><a href="#coresterminal"> 💻</a> Implementando cores no terminal </h2>

<img src = "https://github.com/RayaneGomes97/Estudos_Python3/blob/master/imagens%20%5Bpersonaliza%C3%A7%C3%A3o%5D/ansi-example.png">

<h3> Exemplo: </h3>

<img src = "https://github.com/RayaneGomes97/Estudos_Python3/blob/master/imagens%20%5Bpersonaliza%C3%A7%C3%A3o%5D/ansi-example-2.png">

</body>
</html>
