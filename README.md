# SISSA
<h2>Sistema de Suporte ao Advogado construído com Django</h2>

O Sistema de Suporte ao Advogado nasceu há alguns anos quando eu ainda trabalhava prestando serviço ao Poder Judiciário aqui da Bahia. Eu percebi as dificuldades, tais como: custo, transporte e tempo gasto que os Advogados tinham em realizar diligências processuais junto ao Juiz responsável pelo processo e também o tempo que o Juiz responsável tinha que separar da sua jornada de trabalho para atender esses Advogados.

Como o Código de Processo Civil já havia previsto a criação de listas públicas com processos prontos para serem sentenciados, ordenados por data da conclusão, eu percebi que poderia acrescentar valor a todos os envolvidos tornando essa dinâmica transparente e funcional.

Inicialmente tentei implementar o projeto em Java, com JSF e Primefaces, inclusive, o projeto se tornou trabalho de faculdade e, apesar de incompleto, você pode encontra-lo aqui mesmo na minha conta no github. Infelizmente o custo para colocar o projeto no ar me afastou, visto que eu teria que arcar com todos eles se quisesse ver o projeto funcionando. Então decidi faze-lo utilizando o blogger, google forms e o google spreadsheets e ele está no ar até hoje no endereço varaciveldecandeias.net, mais de dois anos após a minha saída do trabalho.

Ao conhecer o Python e sobretudo o Django, eu senti a necessidade de tentar implementar a ideia original como forma de consolidar o meu aprendizado, afinal, na minha percepção, se eu conseguisse fazer um projeto 'original', o mais distante possível dos clones de outros sites ou dos exemplos de projeto que rodam a internet (que tem o seu valor e certamente você verá muitos deles nesse perfil), poderia considerar que de fato absorvi o conhecimento ao invés de ser um mero copiador de código.

Dito isso, devo deixar claro que todo o front-end do projeto foi feito pela ALURA e entregue durante o curso, eu apenas reaproveitei e modifiquei de forma sutil (Preciso aprender o bootstrap e relembrar as aulas das tecnologias front-end hahaha) já que o estudo foi sobre Django.

Algumas observações: O Django Admin é um recurso de brilhar os olhos, me senti muito bem em ver tudo pronto sem muito esforço e trabalhar com datas no django foi algo muito satisfatório, eu já estava pensando em como fazer as conversões para o formato do Banco de dados e depois converter novamente para mostrar ao usuário, mas simplesmente funcionou como magia, me senti o próprio Harry Potter (com a varinha quebrada quando precisei carregar a data no input date. Você vai entender mais a frente).

Porém, nem tudo são flores ou sapos de chocolate (que você fica sem figurinha ou chocolate, é... talvez seja como esse último), algumas dificuldades ao longo do projeto merecem ser pontuadas:

- A primeira dificuldade nasceu da conveniência de ter um modelo de User pronto no Django, o que facilita MUITO a nossa vida. Mas o que acontece se temos 2 perfis de User no projeto? No meu caso eu tinha o funcionário, que bastava os dados padrão do User, mas tinha também o Advogado que teria os atributos OAB e UF.

Após horas de pesquisas cheguei a duas conclusões. A primeira seria criar um Model de Advogado extendendo o AbstractUser e então adicionar os atributos necessários, mas aí me parece que eu teria que torna-lo padrão no settings.py, o que prejudicaria o perfil de funcionário que ficaria com atributos inúteis. A segunda opção, mais simples e que de fato foi implementada, seria criar o Model com o User como Chave estrangeira. Assim, em tese, eu conseguiria puxar todas as informações necessárias com SQL sem maiores dificuldades.

E assim nasceu a segunda dificuldade.

- Ao cadastrar uma diligência eu pego os dados do usuário logado para fazer a vinculação, mas como eu iria pegar a OAB desse usuário para mostrar na tela com a consulta padrão do Django (objects.filter())? 

Tentei inclusive fazer uma consulta direta com <code>Diligencias.objects.query()</code>, conforme SQL abaixo, mas pelo objeto 'diligência' não ter o campo 'OAB' deu erro ao recuperar os dados, a consulta direto no SGBD puxou os dados conforme esperado.

consulta para a lista de processos comuns: <code>select dd.processo, dd.tipo, dd.data_diligencia, aa.oab from advogados_advogado aa inner join auth_user au ON aa.user_id = au.id inner join diligencias_diligencia dd on dd.advogado_id = aa.id where dd.tipo <> 'Sentença' and dd.prioridade = false;</code> 

<b>SOLUÇÃO:</b> Problema resolvido mudando o string do model 'Advogado' para o username do usuário, a OAB e UF concatenada, foi mais fácil do que parecia.

- Outra dificuldade boba, mas que tem a ver com Javascript seria fazer um index na tabela para mostrar a posição de cada processo na lista, fiquei horas pesquisando e não encontrei como fazer (AINDA! Lok'tar Ogar!).
  
 <b>SOLUÇÃO:</b> Lendo a documentação do Django eu conheci a variável <code>forloop.counter</code> que faz exatamente o que eu estava precisando.
  
 - UPDATE 26/10/2021: Trabalhar com data me parece ser o maior pesadelo do desenvolvedor júnior, a variedade de formatos e a necessidade de adaptar seu armazenamento no banco e mostrar para o usuário de maneira familiar sempre me foi desafiador. No Django essa tarefa foi estranhamente fácil, porém, por falta de conhecimento em Javascript eu suponho, tive dificuldades de carregar a data do Banco de dados no <code>input type='date'</code> na tela de edição de diligência, simplesmente não funcionou. Como alternativa eu precisei carregar a data anteriormente cadastrada em um input simples e manter o input date apenas para possibilitar a alteração. Gambiarra bizarra.

Bom, This is It, espero que tenham se divertido lendo esse Readme como eu me diverti escrevendo e até o próximo commit.
