# Resolução do problema e comentários

## Endpoints

**POST** - `.../api/v1/formatters/wrap/`

Este endpoint recebe uma string independente de quantos parágrafos houver, e opcionalmente recebe um número que define o tamanho máximo em caracteres que o texto final deve ter, sendo por padrão 50 caracteres caso o campo não seja preenchido. Retorna o texto formatado com cada linha do texto de acordo com o número máximo de caracteres desejado.

**POST** - `.../api/v1/formatters/justify/`

Este endpoint recebe uma string independente de quantos parágrafos houver, e opcionalmente recebe um número que define o tamanho máximo em caracteres que o texto final deve ter, sendo por padrão 50 caracteres caso o campo não seja preenchido. Retorna o texto formatado e **justificado** com cada linha do texto de acordo com o número máximo de caracteres desejado, adequando os espaçamentos para preencher o espaço faltante nas linhas.


## Comentários

Apesar de minha especialidade ser com Django Rest Framework, como o desafio deixava em aberto qual tecnologia python usar, optei por usar FastAPI pois seria algo mais simples e o escopo do Django seria grande demais para isso.

Apesar da simplicidade optei por usar uma estrutura de arquivos mais bem elaborada, para ficar com uma leitura de código mais otimizada, então usei meu próprio boilerplate no qual vendo trabalhando [aqui](https://github.com/mts-lucas/furious-api), que segue a estrutura recomendada na própria documentação do FastAPI.

Quanto a implementação, a primeiro momento tentei utilizar uma solução própria para efetuar a formatação, mas enquanto pesquisava descobri que já havia um módulo nativo que executava essa tarefa, então optei por utilizar como alternativa mais segura, implementando apenas o algoritmo que justifica o texto. Contudo como pode se notar no histórico de commits, acabei tendo que refatorar ambos os códigos devido problemas com linhas em branco. Durante os testes manuais que apliquei não estava levando em conta que o usuário gostaria que as linhas em branco fossem mantidas, então tive de readequar os algoritmos para lidar com elas, o que me leva ao ultimo ponto, a formatação das entradas.

Durante meus testes, percebi que o usuário pode tentar mandar um texto com espaços usando `ENTER` ao invés de `\n`, o que levanta a e **exception 422**. Contudo optei por não levar em conta essa formatação, pois pensando no caso de uso, se o usuário está interagindo com a API diretamente ele tem noção das exception que podem se geradas com a formatação usando `ENTER`, e se essa API for integrada a uma aplicação frontend, os próprios inputs usados, já ajustam o texto para o formato adequado. Assim tratar dessa ocasião traria muito mais complexidade do que esse desafio se propõe e por isso optei por não faze-lo. Uma alternativa viável seria personalizar as mensagens de exception para esse caso em específico, sinalizando ao usuário o porque o erro.

Ademais o restando da implementação, segue apenas o proposta na estrutura padrão de um projeto fastAPI, não precisando pontuar seu código.