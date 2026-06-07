No projeto a pasta de 'venv' estava inclusa, porém ela é bem extensa então retirei ela no momento de subir para o repositório.
Para testar e tudo mais, é necessário instalar e ligar o venv para realizar 2 terminais de cmd
No terminar 1 vai ativar o venv por 'venv\Scripts\activate' e quando estiver ligado, rodar 'rasa run actions'
Esse primeiro terminar vai ficar estático, e precisa estar ativo para realizar os testes com a IA.

No segundo terminal de cmd, também precisa ativar o venv com 'venv\Scripts\activate'
Porém a IA é ''ligada'' com o comando 'rasa shell --endpoints endpoints.yml'

A partir dai é possível digitar os comandos para verificar as funções que a IA foi treinada.