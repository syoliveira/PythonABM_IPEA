## Familia BeTa em *Python*

#### **Pergunta**
**1.** **Há clareza do objeto que quer estudar?**<br/>
**R:** Sim, O projeto *Familia BeTa* é um embrião, que pretendo desenvolver para a qualificação e posteriormente para o trabalho final, 
por isso, está aberto e poderá sofrer grandes e significativas alterações. 

**2.** **Qual a pergunta de pesquisa?** <br/>
**R:** Neste protótipo, a pergunta é : Qual o comportamento dos agentes frente a decição entre alugar ou comprar um imovel ?

**3.** **Se tem uma pergunta, tem uma hipótese? O que acha que ocorre?** <br/>
**R:** Sim, a hipótese e de que a renda e composição familiar é o fator de decisão entre aluguel e compra para este protótipo. 

**4.** **ABM é adequado para a pergunta?** <br/>
**R:** Sim, com todo a certeza, uma vez que é possivel com a ABM estabelecer experimentos randomizados que nos permitem simular a 
realidade, e suas complexidades. 

#### **Método/Processo I e II**  <br/>
## Familia BeTa em *Python*
**1.** **Se ABM for adequado, provavelmente, é fácil determinar:** <br/>
**2.** Os Agentes em si.
**R:** : Sim, os agentes são as familias, uma vez que são estas que precisam de moradia. 

**2.1** **Quais são os agentes? Pessoa física, eleitor, paciente,residências/famílias, grupos de interesse, bancos?** <br/>
**R:** São familias, formada por pessoas com renda entre R$ 1.045,00 e R$ 39.200,00, que podem ser compostas de casais com ou sem filhos, solteiros com ou sem filhos

**2.2** Qual é o processo a se replicar? É padrão? As regras são conhecidas? Há literatura?<br/>
**R:** Estou tentando replicar a composição da familia,e a renda destas e o valor de imovel que as familias podem compra ou alugar. 

**3.** Quais são as regras?** <br/>
**R:** o programa tem 1 input que é a quantidade de familias que desejamos formar. 

**3.1** São ações dos agentes?** <br/>
**R:** geração das familias, se casados, com ou sem filhos, e a renda do agente. -

**3.2** **São de origem behaviorista, probabilística, a partir de percepções, mercado, condicionais, baseadas em limites (thresholds). Eles são ad hoc?**<br/>
**R:** São probabilística, e quero, neste prototipo testar a composição de renda, familia e comprometimento de renda apenas. 

**4.** **Qual é o ambiente?** <br/>
**R:** um recorte de realidade, que admite o intervalo de renda entre o salario minimo vigente e o teto consitucional,composição de familia com até 3 filhos. 

**4.1** **Os outros agentes?**<br/>
**R:** o pragrama não interagem com outros agentes ainda, ou seja não está tomando decisão.

**4.2** **Como é o encontro entre os agentes?** <br/>
**R:** É feito de forma randomizada a composição da familia, a composição da renda e o comprometimento de 10% da renda por filho e 30% da renda para gasto com moradia. 

**4.3** **Como o ambiente muda?** <br/>
**R:** de acordo com o numero de familias. 

**4.4** **As ações são simultâneas? Ou uma após a outra? ** <br/>
**R:** São inicialmente simultâneas.

**5.** **Qual é o processo?** <br/>
**R:** Primeiro coloca-se o numero de familia, em seguida o programa vai randomizar a composição da familia, depois a renda e a poupança que pode variar entre 0 e 250 mil

**5.1** **O que ocorre em qual ordem?**<br/>
**R:** Familias, com interação entre renda, estado civil e numero de filhos, em seguida os tipos disponiveis de imoveis A, B ou C. 

**5.2** **Qual é o sistema inicial? Dotações, características?** <br/>
**R:** O sistema esta programado apra ser gerado pelo main, e portanto este gera todas as interações e criação do arquivo cvs de saida. 

**5.3** **Por quanto tempo a simulação roda? Faz diferença? Há compatibilidade observada?** <br/>
**R:** Não foi, inicialmente inserido um loop com fator de venha a parar o programa, ou seja, está programado para rodas conforme o numero de inputs incluidos no inicio do programa, com o numero de 
familias que pretendemos aleatorizar. 

**6.** Use o PROTOCOLO ODD [1] como guia na elaboração do projeto e do texto.<br/>


#### **Validação!!!**

**1.** **Antes de começar, é bom ter ideia de como vai validar o modelo (ABM)**.<br/>
**R:** A validação é com a formação do banco de dados. 

**2.** **Há dados empíricos que podem ser replicados?** <br/>
**R:** Ainda Não.

**3.** **O modelo replica o status quo?** <br/>
**R:**Sim, uma vez que estamos admitindo intevalo de salários reais, quantidade de filhos de acordo com a média nacional, estrutura familiar em que um dos componetes do casal pode ganhar
entre 0 e R$ 39.200,00 mês. 

**4.** **Idealmente, replica-se uma trajetória no tempo.**<br/>
**R:** Não, ainda não, é um protótipo incipiente. 

**5.** **Então, testam-se alternativas {pós-trajetória {e podem-se fazer algumas sugestões, recomendações, dado o contexto da pesquisa**.<br/>
**R:** Sim, podemos avaliar a tragetória, a composição das familias, a renda. 

**6.** **Essa literatura não está consolidada, mas em evolução.** <br/>
**R:** Não, mais irá funcionar com um experimento de realidade. 

**7.** **Minimamente, a questão da validação tem que ser discutida no texto!**<br/>
**R:** A validação ainda pode ser melhorada, conforme for apreciando os estudos teoricos da modelagem.


#### **Verificação e teste**

**1.** **Você tem certeza que o código faz o que você acha que faz?** <br/>
**R:** Sim,roda de maneira simples e promove as interações, conforme solicitada. Ainda gera ao final um gráfico com a relação da renda das familias. 

**2.** **Cada parte foi testada?** <br/>
**R:** Sim,todo o código foi testado durante a construção do programa. 

**3.** **Use print para verificar resultados intermediários!**<br/>
**R:** Sim, no main com o resultado agrupado. 

**4.** **Você utilizou debug para acompanhar o que ocorre com quando agente, a cada passo.**<br/>
**R:** Sim, o código foi construido no pycharm, e a saída aparece no terminal quando o "run" é comandado no Maim, em seguida é gerada uma planilha csv - "familia", 
e gera um gráfico com a renda das familias geradas.