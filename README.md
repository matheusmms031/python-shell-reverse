# Shell reverse em Python
Essa é uma shell reversa criada em Python, nela é possível executar apenas alguns comandos na máquina host, não podendo utilizar todos os comandos disponíveis no CMD ou no terminal Linux.
<br>
<div align='center'>
  <img src='image2.png' height='150'>
</div>

## Instalando o necessário

Aqui está um passo a passo do que deve ser feito para utilizar a Shell Reversa da melhor maneira possível.

### Download do repositório

Antes de tudo é necessário fazer o download do repositório, pode ser utilizando o `git` ou caso queira fazendo pelo próprio site do GITHUB que logo em seguida é preciso extrair essa pasta .ZIP no local desejado.

### Instalando dependências

Para a utilização dessa shell reversa é necessário que as duas máquinas tenham o `Python 3.9.X` instalado, juntamente com uma biblioteca super importante que é a `psutil`, para isso basta digitar no terminal:
```
pip install psutil
```

> [!IMPORTANT]
> Caso algo de erro é sugerido que ***revise a versão do Python instalada, pois essa precisa ser superior ou igual a 3.9.***

## Configurando
Caso queira mudar a porta que será aberta na máquina servidora isso é possível, basta entrar no arquivo [main.py](./main.py) e alterar a linha **102** para a porta desejada,
como é esboçado no código abaixo:
```py
HOST = PORTA DESEJADA
```

## Executando
### Como funciona?
A máquina que vai rodar a Shell, que no caso será a servidora deverá executar o arquivo [main.py](./main.py), logo em seguida a máquina client deve executar o arquivo [client.py](./client.py) com os seguintes parametros:

```bash
python client.py -i IP DA MAQUINA SERVIDORA -p PORTA DA APLICAÇÃO
```

Assim estará pronto para uso.
