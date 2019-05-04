# BAT Papo
## Descrição

Necessito de um serviço de comunicação via texto chamado de BAT-Papo (Caso tenham nomes melhores, fiquem a vontade). 

### Cliente
Um cliente deve suportar as seguintes as seguintes funcionalidades:

* Um cliente, ao ser criado, deve solicitar ao usuário qual será o seu ID. O cliente deve registrar o ID do usuário no servidor. 
* Após receber a confirmação de registro do servidor, o cliente deve estar habilitado para, ao mesmo tempo, poder enviar mensagens para outros usuários baseados em seus IDs, ou receber mensagens  de outros usuários.
* O cliente deve ser capaz de obter a lista de usuários logados no servidor.
* Caso seja enviado uma mensagem para um usuário inexistente, o servidor deve informar que o destinatário não existe.

### Servidor
Um servidor deve suportar as seguintes funcionalidades:

* Um servidor deve aceitar o registro de novos clientes em função dos seus IDs
* Um servidor deve encaminhar mensagens de um cliente para outro baseados em seus IDS
* Um servidor deve disponibilizar a lista de IDs registrados quando necessário
* O servidor deve informar que a mensagem não pode ser enviada porque o usuário de destino não existe.

## Informações 

* O trabalho deve ser entregue até 25/05/2019.
* O trabalho irá valar 3 pontos na nossa VP2.
* O trabalho é individual
* O trabalho deve ser entregue via email, ou github link.