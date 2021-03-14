# SocketTcp
Implementação de um Socket TCP em Python.

# Atividade 1 - Programação com Sockets TCP
## Como utilizar: 
Instalar Python 3, executar o arquivo server.py e em outro terminal client.py.

### As mensagens de solicitação estão no formato String UTF:
* TIME<\br>
Retorna a hora do sistema como uma String UTF no formato HH:MM:SS
* DATE<\br>
Retorna a data do sistema como uma String UTF no formato DD/MM/AAAA
* FILES<\br>
Retorna os arquivos da pasta definida por padrao (p. ex. /home/user/shared)
Formato:<\br>
retorna um inteiro indicando o número de arquivos (int)
envia individualmente o nome de um arquivo como uma String UTF.
*DOWN nome-arquivo<\br>
Faz o download do arquivo nome-arquivo
Formato:<\br>
retorna um inteiro 0 se nome não existe ou retorna o tamanho do arquivo (int) em bytes.
recebe byte a byte e grava em um diretório padrão
* EXIT<\br>
Finaliza a conexão
