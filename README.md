# sissa
Sistema de Suporte ao Advogado construído com Django

O Sistema de Suporte ao Advogado nasceu há alguns anos quando eu ainda trabalhava prestando serviço ao Poder Judiciário aqui da Bahia. Eu percebi as dificuldades, tais como custo, transporte, tempo gasto, que os Advogados tinham em realizar diligências processuais junto ao Juiz responsável pelo processo e também o tempo que o Juiz responsável tinha que separar da sua jornada de trabalho para atender esses Advogados.

Como o Código de Processo Civil já havia previsto a criação de listas públicas com processos prontos para serem sentenciados, ordenados por data da conclusão, eu percebi que poderia acrescentar valor a todos os envolvidos.

Inicialmente tentei implementar o projeto em Java, com JSF e Primefaces, inclusive, o projeto se tornou trabalho de faculdade e, apesar de incompleto, você pode encontra-lo aqui mesmo na minha conta no github. Infelizmente o custo para colocar o projeto no ar me afastou, visto que eu teria que arcar com todos eles se quisesse ver o projeto no ar. Então decidi faze-lo utilizando o blogger, google forms e o google spreadsheets e ele está no ar até hoje no endereço varaciveldecandeias.net, mais de dois anos após a minha saída do trabalho.

Ao conhecer o Python e sobretudo o Django, eu senti a necessidade de tentar implementar a ideia original como forma de consolidar o meu aprendizado, afinal, na minha percepção, se eu conseguisse fazer um projeto 'original', o mais distante possível dos clones de outros sites, poderia considerar que de fato absorvi o conhecimento ao invés de ser um mero copiador de código.

Dito isso, devo deixar claro que todo o front-end do projeto foi feito pela ALURA e eu apenas reaproveitei e modifiquei de forma sutil (Preciso aprender o bootstrap e relembrar as aulas das tecnoligas front-end hahaha).

Algumas dificuldades ao longo do projeto merecem ser pontuadas:

- A primeira dificuldade nasceu da conveniência de ter um modelo de User pronto no Django, o que facilita MUITO a nossa vida. Mas o que acontece se temos 2 perfis de User no projeto? No meu caso eu tinha o funcionário, que bastava os dados padrão do User, mas tinha também o Advogado que teria os atributos OAB e UF.

Após horas de pesquisas cheguei a duas conclusões. A primeira seria criar um Model de Advogado extendendo o AbstractUser e então adicionar os atributos necessários, mas aí me parece que eu teria que torna-lo padrão no settings.py, o que prejudicaria o perfil de funcionário que ficaria com atributos inúteis. A segunda opção, mais simples e que de fato foi implementada, seria criar o Model com o User como Chave estrangeira. Assim, em tese, eu conseguiria puxar todas as informações necessárias com SQL sem maiores dificuldades.

E assim nasceu a segunda dificuldade.

- Ao cadastrar uma diligência eu pego os dados do usuário logado para fazer a vinculação, mas como eu iria pegar a OAB desse usuário para mostrar na tela com a consulta padrão do Django (objects.filter())? 

No momento que escrevi esse texto me ocorreu que eu poderia passar uma consulta SQL com o 'query' ou 'raw' e brincar a vontade com as possibilidades, mas teria outra forma?

- Outra dificuldade boba, mas que tem a ver com Javascript seria fazer um index na tabela para mostrar a posição de cada processo na lista, fiquei horas pesquisando e não encontrei como fazer.
