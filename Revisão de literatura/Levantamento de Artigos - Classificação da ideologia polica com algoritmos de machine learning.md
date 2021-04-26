# Levantamento de Artigos - Classificação da ideologia polica com algoritmos de machine learning 
---

## 1.Political Ideology Detection Using Recursive Neural Networks

### Autores 
- Mohit Iyyer
- Peter Enns
- Jordan Boyd-Graber
- Philip Resnik

### Resumo 
As palavras de um indivíduo muitas vezes revelam sua ideologia política. Técnicas automatizadas existentes para identificar ideologia a partir do foco do texto em pacotes de palavras ou listas de palavras, ignorando a sintaxe. Inspirando-se em trabalhos recentes em análise de sentimento que modela com sucesso o aspecto composicional da linguagem, nós aplicar uma rede neural recursiva (RNN) quadro à tarefa de identificar a posição política evidenciada por uma frase. Para mostrar a importância da modelagem de elementos subsentenciais, fazemos crowdsourcing político anotações em nível de frase e sentença. Nosso modelo supera os modelos existentes em nosso conjunto de dados recém-anotado e um existente conjunto de dados.

### Abstract 
An individual’s words often reveal their political ideology. Existing automated techniques to identify ideology from text focus on bags of words or wordlists, ignoring syntax. Taking inspiration from recent work in sentiment analysis that successfully models the compositional aspect of language, we apply a recursive neural network (RNN) framework to the task of identifying the political position evinced by a sentence. To show the importance of modeling subsentential elements, we crowdsource political annotations at a phrase and sentence level. Our model outperforms existing models on our newly annotated dataset and an existing dataset.

### Fonte 
https://www.aclweb.org/anthology/P14-1105.pdf

---
## 2. Multi-view Models for Political Ideology Detection of News Articles

### Autores
- Vivek Kulkarni
- Steven Skiena
- Junting Ye
- William Yang Wang

### Resumo 
O título, o conteúdo e uma estrutura do link de um artigo de notícias costumam revelar sua ideologia política. No entanto, a maioria dos trabalhos existentes na detecção automática de ideologia política apenas alavancam textual dicas. Inspirando-se em avanços recentes na inferência neural, propomos um romance modelo de múltiplas visualizações baseado em atenção para alavancardicas de todas as visualizações acima para identificar o ideologia evidenciada por um artigo de notícias. Nosso modelo baseia-se nos avanços na aprendizagem de representação em processamento de linguagem natural e rede ciência para capturar pistas do conteúdo textual e da estrutura de rede de artigos de notícias. Avaliamos empiricamente nosso modelo em relação a um bateria de linhas de base e mostrar que nosso modelo supera o estado da arte em 10% pontos pontuação F1.

### Abstract
A news article’s title, content and link structure often reveal its political ideology. However, most existing works on automatic political ideology detection only leverage textual cues. Drawing inspiration from recent advances in neural inference, we propose a novel attention based multi-view model to leverage cues from all of the above views to identify the ideology evinced by a news article. Our model draws on advances in representation learning in natural language processing and network science to capture cues from both textual content and the network structure of news articles. We empirically evaluate our model against a battery of baselines and show that our model outperforms state of the art by 10 percentage points F1 score.

### Fonte 
https://www.aclweb.org/anthology/D18-1388.pdf

---
## 3. We Can Detect Your Bias: Predicting the Political Ideology of News Articles 

### Autores
- Ramy Baly
- Giovanni Da San Martino
- James Glass
- Preslav Nakov

### Resumo 
Exploramos a tarefa de prever a principal ideologia política ou o viés dos artigos de notícias. Primeiro, coletamos e lançamos um grande conjunto de dados de 34.737 artigos que foram anotados manualmente para ideologia política –esquerda, centro ou direita–,que é bem equilibrado entre os tópicos e meios de comunicação. Além disso, usamos uma configuração experimental desafiadora onde os exemplos de teste vêm de mídias que não foram vistas durante o treinamento, o que impede o modelo de aprender para detectar a fonte do artigo de notícias alvo em vez de prever sua ideologia política. De uma perspectiva de modelagem, propomos um adaptação adversarial da mídia, bem como uma perda de trigêmeos especialmente adaptada. Nós ainda adicionamos informações básicas sobre a fonte, e mostramos que é bastante útil para melhorar a previsão no nível do artigo. Nosso experimental os resultados mostram melhorias consideráveis sobre usando transformadores pré-treinados de última geração nesta configuração desafiadora.

### Abstract
We explore the task of predicting the leading political ideology or bias of news articles. First, we collect and release a large dataset of 34,737 articles that were manually annotated for political ideology –left, center, or right–, which is well-balanced across both topics and media. We further use a challenging experimental setup where the test examples come from media that were not seen during training, which prevents the model from learning to detect the source of the target news article instead of predicting its political ideology. From a modeling perspective, we propose an adversarial media adaptation, as well as a specially adapted triplet loss. We further add background information about the source, and we show that it is quite helpful for improving article-level prediction. Our experimental results show very sizable improvements over using state-of-the-art pre-trained Transformers in this challenging setup.

### Fonte 
https://arxiv.org/pdf/2010.05338.pdf

---
## 4. Ideology Detection of Personalized Political News Coverage: A New Dataset

### Autores 
- Khudran Alzhrani


### Resumo
Seleção de palavras, estilo de escrita, seleção de histórias e muitos outros fatores desempenham um papel no enquadramento de artigos de notícias para caber no público-alvo ou para se alinhar com as crenças dos autores. Portanto, relatar fatos por si só não é evidência de jornalismo livre de preconceitos. Desde as eleições presidenciais dos Estados Unidos de 2016, os pesquisadores se concentraram na influência da mídia nos resultados das eleições. A atenção da mídia mudou de partidos políticos para candidatos. A mídia de notícias molda a percepção pública dos candidatos políticos por meio da personalização das notícias. Apesar de sua criticidade, não temos conhecimento de nenhum estudo que tenha examinado a personalização de notícias da perspectiva do aprendizado de máquina ou da rede neural profunda. Além disso, alguns candidatos acusam a mídia de favoritismo que prejudica suas chances de ganhar as eleições. Vários métodos foram introduzidos para colocar as fontes de notícias de um lado do espectro político ou do outro, mas a grande mídia afirma ser imparcial. Portanto, para evitar suposições imprecisas, apenas fontes de notícias que declararam claramente sua filiação política foram incluídas nesta pesquisa.
Neste artigo, construímos dois conjuntos de dados a partir de artigos de notícias escritos sobre os dois últimos presidentes dos EUA com relação à filiação política de sites de notícias. Vários modelos inteligentes foram desenvolvidos para prever automaticamente a afiliação política do artigo invisível personalizado. O principal objetivo desses modelos é detectar a ideologia política de artigos de notícias personalizados. Embora os conjuntos de dados recém-construídos sejam altamente desequilibrados, o desempenho dos modelos inteligentes é razoavelmente bom. Os resultados dos modelos inteligentes são relatados

### Abstract
Words selection, writing style, stories cherry-picking, and many other factors play a role in framing news articles to fit the targeted audience or to align with the authors' beliefs. Hence, reporting facts alone is not evidence of bias-free journalism. Since the 2016 United States presidential elections, researchers focused on the media influence on the results of the elections. The news media attention has deviated from political parties to candidates. The news media shapes public perception of political candidates through news personalization. Despite its criticality, we are not aware of any studies which have examined news personalization from the machine learning or deep neural network perspective. In addition, some candidates accuse the media of favoritism which jeopardizes their chances of winning elections. Multiple methods were introduced to place news sources on one side of the political spectrum or the other, yet the mainstream media claims to be unbiased. Therefore, to avoid inaccurate assumptions, only news sources that have stated clearly their political affiliation are included in this research.

In this paper, we constructed two datasets out of news articles written about the last two U.S. presidents with respect to news websites' political affiliation. Multiple intelligent models were developed to automatically predict the political affiliation of the personalized unseen article. The main objective of these models is to detect the political ideology of personalized news articles. Although the newly constructed datasets are highly imbalanced, the performance of the intelligent models is reasonably good. The results of the intelligent models are reported

### Fonte 
https://dl.acm.org/doi/10.1145/3388142.3388149

--- 

## 5. Ideology Detection with using Deep Neural Network

### Autores 
- Lee Hojoon
- Jeong Minbyul

### Resumos 
No campo político, existem muitas pesquisas tentando detectar a ideologia política dentro do texto. Tradicionalmente A tecnologia automatizada usada é BoW (Bag of Words), que só conta para frequência, ignorando o seqüência. No entanto, estudos recentes mostraram que o aprendizado profundo está apresentando um ótimo desempenho no sentimento análise. Portanto, aplicamos RNN (Recrusvie Neural Network), LSTM (Long-Term Short-Term Memory), e CNN (Rede Neural Convolucional) para detectar ideologia política em nível de sentença.

### Abstract 
In the political field, there are many researches trying to detect political ideology inside the text. Traditionally used automated techonology is BoW (Bag of Words) which only counts for frequency ignoring for the sequence. However, recent studies have shown that deep learning is showing great performance in sentiment analysis. Therefore, we apply RNN (Recrusvie Neural Network), LSTM (Long-Term Short-Term Memory), and CNN (Convolutional Neural Network) to detect political ideology in sentence level.

### Fonte 
https://joonleesky.github.io/assets/pdf/ideology_detection.pdf

---
## 6. Opinion-aware Knowledge Graph for Political Ideology Detection

### Autores 
- Wei Chen
- Xiao Zhang
- Tengjiao Wang
- Bishan Yang
- Yi Li

### Resumo
Identificar a ideologia política do indivíduo a partir de seus discursos e textos escritos são importantes para analisar opiniões políticas e o comportamento do usuário em mídia social. Os métodos tradicionais de mineração de opinião contam com representações de saco de palavras para classificar textos em diferentes categorias de ideologia. Esses métodos são muito grosseiros para entender ideologias políticas. A chave para identificar diferentes ideologias é reconhecer as diferentes opiniões expressas em relação um tópico específico. Para modelar esse insight, classificamos as ideologias com base na distribuição de opiniões expressas em relação a entidades ou tópicos do mundo real. Especificamente, propomos uma nova abordagem para detecção de ideologia política que faz previsões com base em um gráfico de conhecimento de opinião. Nós mostram como construir esse gráfico integrando as opiniões e entidades-alvo extraídas de texto em uma base de conhecimento estruturada existente e mostrar como realizar inferência de ideologia por propagação de informação no gráfico. Resultados experimentais demonstram que nosso método atinge alta precisão na detecção de ideologias em comparação com linhas de base, incluindo LR, SVM e RNN

**Palavras-chaves**: IA e ciências sociais Processamento de linguagem natural: análise de sentimento e mineração de texto

### Abstract 
Identifying individual's political ideology from their speeches and written texts is important for analyzing political opinions and user behavior on social media. Traditional opinion mining methods rely on bag-of-words representations to classify texts into different ideology categories. Such methods are too coarse for understanding political ideologies. The key to identify different ideologies is to recognize different opinions expressed toward a specific topic. To model this insight, we classify ideologies based on the distribution of opinions expressed towards real-world entities or topics. Specifically, we propose a novel approach to political ideology detection that makes predictions based on an opinion-aware knowledge graph. We show how to construct such graph by integrating the opinions and targeted entities extracted from text into an existing structured knowledge base, and show how to perform ideology inference by information propagation on the graph. Experimental results demonstrate that our method achieves high accuracy in detecting ideologies compared to baselines including LR, SVM and RNN.

**Keywords**: AI and Social Sciences, Natural Language Processing, Sentiment Analysis and  Text Mining

### Fonte 
https://www.ijcai.org/Proceedings/2017/510

--- 

## 7. Ideology Detection for Twitter Users via Link Analysis

### Autores

- Yupeng Gu
- Ting Chen
- Yizhou Sun
- Bingyu Wang

### Resumos 
O problema da detecção de ideologia é estudar o posicionamento latente (político) para as pessoas, que é tradicionalmente estudado nos políticos de acordo com seus comportamentos de voto. Recentemente, mais e mais estudos começam a abordar o problema de detecção de ideologia para usuários comuns com base em seus comportamentos online que podem ser capturados pela mídia social, por exemplo, Twitter. No que nos diz respeito, a grande maioria dos existentes métodos de detecção de ideologia nas redes sociais simplificaram demais o problema como um problema de classificação binária (ou seja, liberal vs. conservador). Além disso, embora os links sociais possam desempenhar um papel crítico na decisão de ideologia, a maior parte do trabalho existente ignora os tipos heterogêneos de links nas redes sociais. Neste artigo, propomos detectar posições ideológicas numéricas para usuários do Twitter, de acordo com seu seguimento, menção e Retweetar links para um grupo selecionado de políticos. Um modelo probabilístico unificado é proposto que pode (1) integrar tipos heterogêneos de links juntos para determinar a ideologia das pessoas e (2) aprender automaticamente a qualidade de cada tipo de link ao decidir a ideologia de alguém. Experiências têm demonstrou as vantagens do nosso modelo em termos de classificação e classificação de inclinação política precisa

### Abstract 
The problem of ideology detection is to study the latent (political) placement for people, which is traditionally studied on politicians according to their voting behaviors. Recently, more and more studies begin to address the ideology detection problem for ordinary users based on their online behaviors that can be captured by social media, e.g., Twitter. As far as we are concerned, the vast majority of the existing methods on ideology detection on social media have oversimplified the problem as a binary classification problem (i.e., liberal vs. conservative). Moreover, though social links can play a critical role in deciding one’s ideology, most of the existing work ignores the heterogeneous types of links in social media. In this paper we propose to detect numerical ideology positions for Twitter users, according to their follow, mention, and retweet links to a selected set of politicians. A unified probabilistic model is proposed that can (1) integrate heterogeneous types of links together in determining people’s ideology, and (2) automatically learn the quality of each type of links in deciding one’s ideology. Experiments have demonstrated the advantages of our model in terms of both ranking and political leaning classification accuracy

### Fonte 
http://web.cs.ucla.edu/~yzsun/papers/2017_SBP_Ideology


--- 

## 8. Political Bias Analysis 

### Autores 
- Arkajyoti Misra
- Sanjib Basak


### Resumo 
Os dois principais partidos políticos dos EUA estão polarizados entre o liberal e ponto de vista conservador em uma infinidade de aspectos socioeconômicos e ambientais questões. Uma abordagem algorítmica para a detecção de tal viés é intelectualmente desafiadora e útil em áreas como previsão de eleições. Existe muito poucos estudos na literatura onde técnicas modernas de aprendizagem profunda são aplicadas para detectar a opinião pessoal ou o preconceito de um indivíduo. Neste trabalho, desenvolvemos uma rede LSTM que alcançou uma pontuação F1 de 0,718 em um conjunto de dados que consiste em declarações feitas no passado recente por candidatos eleitorais dos EUA


### Abstract 
The two major political parties in US are polarized between either the liberal and point of view on a multitude of socio-economical and environmental issues. An algorithmic approach towards detection of such bias is both intellectually challenging and useful in areas like election prediction. There exists very few studies in the literature where modern deep learning techniques are applied to detect the personal opinion or bias of an individual. In this work, we have developed an LSTM network that achieved an F1 score of 0.718 on a data set consisting of statements made in the recent past by US election candidates

### Fonte 
https://cs224d.stanford.edu/reports/MisraBasak.pdf

--- 

## 9. Mining Twitter for Fine-Grained Political Opinion Polarity Classification, Ideology Detection and Sarcasm Detection 

### Autores 

- Sandeepa Kannangara

### Resumo 
Neste artigo, propomos três modelos para a classificação da polaridade de opinião sociopolítica de postagens de microblog. Em primeiro lugar, será proposto um novo modelo probabilístico, o modelo Joint-Entity-Sentiment-Topic (JEST), que captura opiniões como uma combinação da entidade-alvo, sentimento e tópico. Em segundo lugar, um modelo para detecção de ideologia chamado JEST-Ideology será proposto para identificar a orientação de um indivíduo em relação a tópicos / questões e entidades-alvo, estendendo a estrutura de classificação de polaridade de opinião proposta. Finalmente, propomos um novo método para detectar com precisão as opiniões sarcásticas, utilizando a opinião e ideologia de baixa granularidade detectada

**Palavras-chaves:** Mineração de opinião refinada; Detecção de ideologia; Detecção de Sarcasmo 
### Abstract
In this paper, we propose three models for socio-political opinion polarity classification of microblog posts. Firstly, a novel probabilistic model, Joint-Entity-Sentiment-Topic (JEST) model, which captures opinions as a combination of the target entity, sentiment and topic, will be proposed. Secondly, a model for ideology detection called JEST-Ideology will be proposed to identify an individual’s orientation towards topics/issues and target entities by extending the proposed opinion polarity classification framework. Finally, we propose a novel method to accurately detect sarcastic opinions by utilizing detected fine-grained opinion and ideology

**Keywords**: Fine-Grained Opinion Mining; Ideology Detection; Sarcasm Detection

### Fonte 

https://uploads-ssl.webflow.com/5cd23e823ab9b1f01f815a54/5d10e3d7529e1c19e3e06723_Mining%20Twitter%20for%20FineGrained%20Political%20Opinion%20Polarity%20Classification%20Ideology%20Detection%20and%20Sarcasm%20Detection.pdf

--- 

## 10. Automatic detection of political opinions in Tweets

### Autores 
- Diana Maynard 
- Adam Funk

### Resumos 
Neste artigo, discutimos uma variedade de questões relacionadas à mineração de opinião a partir de microposts e os desafios que eles impõem a uma PNL, junto com um aplicativo de exemplo que desenvolvemos para determinar tendências políticas de um conjunto de tuítes pré-eleitorais. Enquanto houver uma série de ferramentas de análise de sentimento disponíveis que resumem tweets positivos, negativos e neutros sobre uma determinada palavra-chave ou tópico, ferramentas geralmente produzem resultados ruins e operam de uma forma bastante simplista forma, usando apenas a presença de certos adjetivos positivos e negativoscomo indicadores, ou técnicas de aprendizagem simples que não funcionam bem em microposts curtos. Por outro lado, ferramentas inteligentes que funcionam bem em filmes e comentários de clientes não podem ser usados em microposts devido a sua brevidade e falta de contexto. Nossos métodos usam uma variedade de técnicas sofisticadas de PNL para extrair mais e opiniões de maior qualidade, e incorporam contextos extralingüísticos em formação

**Palavras-chaves:** PNL, mineração de opinião, análise de mídia social
### Abstract 

In this paper, we discuss a variety of issues related to opinion mining from microposts, and the challenges they impose on an NLP system, along with an example application we have developed to determine political leanings from a set of pre-election tweets. While there are a number of sentiment analysis tools available which summarise positive, negative and neutral tweets about a given keyword or topic, these tools generally produce poor results, and operate in a fairly simplistic way, using only the presence of certain positive and negative adjectives as indicators, or simple learning techniques which do not work well on short microposts. On the other hand, intelligent tools which work well on movie and customer reviews cannot be used on microposts due to their brevity and lack of context. Our methods make use of a variety of sophisticated NLP techniques in order to extract more meaningful and higher quality opinions, and incorporate extra-linguistic contextual information

**Keywords**: NLP, opinion mining, social media analysi

### Fonte 
https://gate.ac.uk/sale/eswc11/opinion-mining.pdf

--- 

## 11. Ideology Detection in the Indian Mass Media

### Autores

- Navreet Kaur 
- Ankur Sharma

### Resumo 

Os preconceitos ideológicos nos meios de comunicação de massa podem moldar a opinião pública. Neste estudo, pretendemos compreender o viés ideológico na mídia de massa indiana, em termos da cobertura que fornece para declarações feitas por pessoas proeminentes sobre as principais políticas econômicas e de tecnologia. Nós construímos um sistema de ponta a ponta que começa com um artigo de notícias e o analisa para obter as declarações feitas por pessoas no artigo; nessas declarações, aplicamos uma rede neural recursiva baseada modelo para detectar se os enunciados expressam um viés ideológico ou não. O sistema então classifica a postura das afirmações não neutras. Para políticas econômicas, determinamos se as declarações expressam um ponto de vista pró ou contrário sobre a política, e para as políticas de tecnologia, nós determinamos se as declarações são positivas ou céticas em relação à tecnologia. O proposto método de pesquisa pode ser aplicado a outros domínios também e pode servir como base para contrastar autoexpressão nas redes sociais por pessoas proeminentes com a forma como os meios de comunicação de massa os retratam 

### Abstract 
Ideological biases in the mass media can shape public opinion. In this study, we aim to understand ideological bias in the Indian mass media, in terms of the coverage it provides to statements made by prominent people on key economic and technology policies. We build an end-to-end system that starts with a news article and parses it to obtain statements made by people in the article; on these statements, we apply a Recursive Neural Network based model to detect whether the statements express an ideological bias or not. The system then classifies the stance of the non-neutral statements. For economic policies, we determine if the statements express a pro or anti slant about the policy, and for technology policies, we determine if the statements are positive or skeptical about technology. The proposed research method can be applied to other domains as well and can serve as a basis to contrast social media self-expression by prominent people with how the mass media portrays them

### Fonte 
https://easychair.org/publications/preprint_open/fLrK

## 12. Exploring the Ideological Nature of Journalists’ Social Networks on Twitter and Associations with News Story Content

### Autores 
- John Wihbey
- Thalita Dias Coleman
- Kenneth Joseph
- David Lazer 

### Resumo 
O presente trabalho propõe o uso das mídias sociais como ferramenta para compreender melhor a relação entre o social de um jornalista rede e o conteúdo que produzem. Especificamente, perguntamos: o que é a relação entre a inclinação ideológica de um jornalista rede social no Twitter e o conteúdo de notícias que ele ou ela produz? Usando um novo conjunto de dados ligando mais de 500.000 artigos de notícias produzidos por 1.000 jornalistas em 25 veículos de notícias diferentes, mostramos um modesto correlação entre as ideologias de quem um jornalista segue Twitter e o conteúdo que ele produz. Esta pesquisa pode fornecem a base para uma maior autorreflexão entre os membros da mídia sobre como eles obtêm suas histórias e como sua própria prática pode ser colorido por suas redes online. Para os pesquisadores, as descobertas fornecer uma etapa nova e importante para melhor compreender o construção de histórias de mídia e a mecânica

### Abstract 
The present work proposes the use of social media as a tool for better understanding the relationship between a journalists’ social network and the content they produce. Specifically, we ask: what is the relationship between the ideological leaning of a journalist’s social network on Twitter and the news content he or she produces? Using a novel dataset linking over 500,000 news articles produced by 1,000 journalists at 25 different news outlets, we show a modest correlation between the ideologies of who a journalist follows on Twitter and the content he or she produces. This research can provide the basis for greater self-reflection among media members about how they source their stories and how their own practice may be colored by their online networks. For researchers, the findings furnish a novel and important step in better understanding the construction of media stories and the mechanic

### Fonte
https://static.poder360.com.br/2017/08/pesquisa.pdf

---

## 13. Predicting the Political Alignment of Twitter Users 

### Autores 
- Michael D. Conover
- Bruno Gonçalves
- Jacob Ratkiewicz
- Alessandro Flammini 
- Filippo Menczer

### Resumo 
A ampla adoção de mídia social para comunicação política cria oportunidades sem precedentes para monitorar as opiniões de um grande número de politicamente ativos indivíduos em tempo real. No entanto, sem uma forma de distinguir entre usuários de alinhamentos políticos opostos, sinais conflitantes no nível individual pode, em geral, obscurecer os partidários diferenças de opinião que são importantes para a estratégia política. Neste artigo, descrevemos vários métodos para prever o alinhamento político dos usuários do Twitter com base no conteúdo e estrutura de sua comunicação política na corrida para o Eleições de meio de mandato de 2010 nos EUA. Usando um conjunto de dados de 1.000 indivíduos anotados manualmente, descobrimos que uma máquina de vetores de suporte (SVM) treinado em metadados de hashtag supera um SVM treinado no texto completo dos tweets dos usuários, produzindo previsões de afiliações com 91% de precisão. Aplicando análise semântica latente ao conteúdo dos tweets dos usuários, identificamos a estrutura oculta no dados fortemente associados à filiação política, mas não encontram essa detecção de tópico melhora o desempenho de previsão. Todos esses métodos baseados em conteúdo são superados por um classificador baseado na estrutura da comunidade segregada de informação política redes de difusão (95% de precisão). Concluímos com um prático aplicação desta máquina à publicidade política baseada na web, e delinear várias abordagens para o monitoramento da opinião pública com base nas técnicas aqui desenvolvidas.

### Abstract

The widespread adoption of social media for political communication creates unprecedented opportunities to
monitor the opinions of large numbers of politically active individuals in real time. However, without a way to distinguish between users of opposing political alignments, conflicting signals at the individual level may, in the aggregate, obscure partisan differences in opinion that are important to political strategy. In this article we describe several methods for predicting the political alignment of Twitter users based on the content and structure of their political communication in the run-up to the 2010 U.S. midterm elections. Using a data set of 1,000 manuallyannotated individuals, we find that a support vector machine (SVM) trained on hashtag metadata outperforms an SVM trained on the full text of users’ tweets, yielding predictions of political affiliations with 91% accuracy. Applying latent semantic analysis to the content of users’ tweets we identify hidden structure in the data strongly associated with political affiliation, but do not find that topic detection improves prediction performance. All of these content-based methods are outperformed by a classifier based on the segregated community structure of political information diffusion networks (95% accuracy). We conclude with a practical application of this machinery to web-based political advertising, and outline several approaches to public opinion monitoring based on the techniques developed herein.

### Fonte 

https://cnets.indiana.edu/wp-content/uploads/conover_prediction_socialcom_pdfexpress_ok_version.pdf

--- 

## 14. The Perils of Classifying Political Orientation From Text

### Autor 
- Hao Yan 
- Allen Lavoie 
- Sanmay Das

### Resumo 
A comunicação política geralmente assume formas linguísticas complexas. Compreender a ideologia política a partir do texto é uma tarefa metodológica importante em estudar as interações políticas entre as pessoas tanto na mídia nova quanto na tradicional. Portanto, tem havido uma enxurrada de pesquisas recentes que se baseiam ou propõem uma nova metodologia para a classificação da ideologia política a partir de dados de texto. Neste artigo, estudamos a eficácia dessas técnicas para classificar a ideologia no contexto da política dos Estados Unidos. Construímos três conjuntos de dados diferentes de textos conservadores e liberais em inglês a partir de (1) registros do congresso, (2) proeminentes sites de mídia conservadores e liberais, e (3) wikis conservadores e liberais, e aplicar algoritmos de classificação de texto com uma técnica de adaptação de domínio. Nosso os resultados são surpreendentemente negativos. Descobrimos que o desempenho de aprendizagem entre domínios, comparando a capacidade de generalizar de um desses conjuntos de dados para outro, é pobre, embora os algoritmos tenham um desempenho muito bom no conjunto de dados dentro testes de validação cruzada. Nós fornecemos evidências de que o mau desempenho é devido a diferenças nos conceitos que geram os verdadeiros rótulos nos conjuntos de dados, em vez do que a uma falha de métodos de adaptação de domínio. Nossos resultados sugerem a necessidade de extremo cuidado ao interpretar os resultados das metodologias de aprendizado de máquina para classificação do texto político em vários domínios. A única exceção ao nosso forte resultados negativos é que os métodos de classificação mostram alguma capacidade de generalizar do registro do congresso aos sites da mídia. Mostramos que isso se deve ao movimento temporal do uso de frases específicas de políticos para a mídia.

### Abstract 

Political communication often takes complex linguistic forms. Understanding political ideology from text is an important methodological task in studying political interactions between people in both new and traditional media. Therefore, there has been a spate of recent research that either relies on, or proposes new methodology for, the classification of political ideology from text data. In this paper, we study the effectiveness of these techniques for classifying ideology in the context of US politics. We construct three different datasets of conservative and liberal English texts from (1) the congressional record, (2) prominent conservative and liberal media websites, and (3) conservative and liberal wikis, and apply text classification algorithms with a domain adaptation technique. Our results are surprisingly negative. We find that the cross-domain learning performance, benchmarking the ability to generalize from one of these datasets to another, is poor, even though the algorithms perform very well in within-dataset cross-validation tests. We provide evidence that the poor performance is due to differences in the concepts that generate the true labels across datasets, rather than to a failure of domain adaptation methods. Our results suggest the need for extreme caution in interpreting the results of machine learning methodologies for classification of political text across domains. The one exception to our strongly negative results is that the classification methods show some ability to generalize from the congressional record to media websites. We show that this is likely because of the temporal movement of the use of specific phrases from politicians to the media.

### Fonte 
http://ceur-ws.org/Vol-1897/paper3.pdf

--- 

## 15. Inflating Topic Relevance with Ideology: A Case Study of Political Ideology Bias in Social Topic Detection Models 

### Autores

- Meiqi Guo 
- Rebecca Hwa
- Yu-Ru Lin
- Wen-Ting Chung

### Resumo 
Investigamos o impacto dos vieses da ideologia política nos dados de treinamento. Por meio de um conjunto de estudos de comparação, examinamos a propagação de vieses em vários modelos de PNL amplamente usados e seu efeito na precisão geral de recuperação. Nosso trabalho destaca a suscetibilidade de modelos grandes e complexos à propagação de vieses de entrada selecionada por humanos, o que pode levar a uma deterioração da precisão de recuperação, e a importância de controlar esses vieses. Finalmente, como forma de atenuar o viés, propomos aprender uma representação textual que seja invariante à ideologia política, ao mesmo tempo em que julgamos a relevância do tema.

### Abstract 
We investigate the impact of political ideology biases in training data. Through a set of comparison studies, we examine the propagation of biases in several widely-used NLP models and its effect on the overall retrieval accuracy. Our work highlights the susceptibility of large, complex models to propagating the biases from human-selected input, which may lead to a deterioration of retrieval accuracy, and the importance of controlling for these biases. Finally, as a way to mitigate the bias, we propose to learn a text representation that is invariant to political ideology while still judging topic relevance

### Fonte 
https://www.x-mol.com/paper/1333859881486295040

---
## 16. Automated detection of political ideology from text: a case study of newspapers in Uruguay

### Autores 

### Resumo 
Embora a reportagem objetiva seja o marco do jornalismo profissional, vários acadêmicos argumentaram que a mídia é ideologicamente tendenciosa. A associação da imprensa escrita (jornais) aos partidos políticos há muito é reconhecida no Uruguai. No entanto, a falta de estudos que demonstrem empiricamente e meçam a extensão do viés ideológico em relação às filiações políticas tem impedido os estudiosos de abordar a diversidade ideológica dos jornais. Aqui, o autor descreve o uso de processamento de linguagem natural e algoritmos de aprendizado de máquina não supervisionado em conjunto com análise de gráfico de rede para investigar a tendência política de cinco jornais que publicaram um total de 530 artigos de notícias sobre dois candidatos políticos de partidos opostos durante o ciclo eleitoral de 2019.


### Abstract
Although objective reporting is the landmark of professional journalism, several academics have argued that the media is ideologically biased. The association of the printed press (newspapers) with political parties have long been acknowledged in Uruguay. However, the lack of studies that empirically demonstrate and measure the extent of ideological bias towards political affiliations has prevented scholars from addressing the ideological diversity of newspapers. Here, the author describes the use of natural language processing and unsupervised machine learning algorithms in conjunction with network graph analysis to investigate the political leaning of five newspapers that published a total of 530 news articles on two political candidates from opposing parties during the election cycle of 2019.

### Fonte 
https://www.martincalvino.co/post/2019/11/12/automated-detection-of-political-ideology-from-text-a-case-study-of-newspapers-in-uruguay

---

## 17. Fair and Balanced? Quantifying Media Bias through Crowdsourced Content Analysis 

### Autores 
- Ceren Budak 
- Sharad Goel
- Justin M. Rao

### Resumos
É amplamente aceito que as organizações de notícias exibem preconceito ideológico, mas quantificar rigorosamente tal inclinação tem se mostrado metodologicamente desafiador. Por meio de uma combinação de técnicas de aprendizado de máquina e crowdsourcing, investigamos a seleção e o enquadramento de questões políticas nos 15 principais veículos de notícias dos EUA. Começando com 803.146 notícias publicadas em 12 meses, primeiro usamos algoritmos de aprendizado supervisionado para identificar 14% dos artigos relativos a eventos políticos. Em seguida, recrutamos 749 juízes humanos online para classificar um subconjunto aleatório de 10.950 desses artigos políticos de acordo com o tópico e a posição ideológica. Nossa análise produz uma ordem ideológica de pontos de venda consistente com o trabalho anterior. Descobrimos, no entanto, que os meios de comunicação são consideravelmente mais semelhantes do que geralmente se acredita. Especificamente, com exceção de escândalos políticos, descobrimos que as principais organizações de notícias apresentam os tópicos de uma maneira amplamente apartidária, não colocando nem democratas nem republicanos em uma luz particularmente favorável ou desfavorável. Além disso, novamente com a exceção de escândalos políticos, há pouca evidência de diferenças sistemáticas na seleção de histórias, com todos os principais veículos de notícias cobrindo uma ampla variedade de tópicos com frequência em grande parte não relacionada à posição ideológica do veículo. Finalmente, descobrimos que as organizações de notícias expressam seu viés ideológico não defendendo diretamente um partido político preferido, mas sim criticando desproporcionalmente um dos lados, uma convenção que modera ainda mais as diferenças gerais.

### Abstract 
It is widely thought that news organizations exhibit ideological bias, but rigorously quantifying such slant has proven methodologically challenging. Through a combination of machine learning and crowdsourcing techniques, we investigate the selection and framing of political issues in 15 major U.S. news outlets. Starting with 803,146 news stories published over 12 months, we first used supervised learning algorithms to identify the 14% of articles pertaining to political events. We then recruited 749 online human judges to classify a random subset of 10,950 of these political articles according to topic and ideological position. Our analysis yields an ideological ordering of outlets consistent with prior work. We find, however, that news outlets are considerably more similar than generally believed. Specifically, with the exception of political scandals, we find that major news organizations present topics in a largely non-partisan manner, casting neither Democrats nor Republicans in a particularly favorable or unfavorable light. Moreover, again with the exception of political scandals, there is little evidence of systematic differences in story selection, with all major news outlets covering a wide variety of topics with frequency largely unrelated to the outlet’s ideological position. Finally, we find that news organizations express their ideological bias not by directly advocating for a preferred political party, but rather by disproportionately criticizing one side, a convention that further moderates overall differences.

### Fonte 
https://www8.gsb.columbia.edu/media/sites/media/files/JustinRaoMediaBias.pdf

--- 

### 18.Partisan public health: how does political ideology influence support for COVID-19 related misinformation?

### Autores 
- Nicholas Francis Havey

### Resumo 
Este estudo analisa mais de 4.000 tweets relacionados a seis tópicos de desinformação sobre a pandemia COVID-19: o uso de hidroxicloroquina como tratamento, o uso de água sanitária como medida preventiva, Bill Gates causando intencionalmente o vírus, o Partido Comunista Chinês causando intencionalmente o vírus, e o Deep State causando o vírus para arruinar a economia e ameaçar as chances de reeleição do presidente Trump. Em 5 de 6 tópicos (excluindo alvejante), os conservadores dominam o discurso no Twitter. Os conservadores também são mais propensos do que seus pares liberais a acreditar e promover teorias de conspiração de que o Partido Comunista Chinês, Bill Gates e o Estado Profundo estão trabalhando em conjunto para infectar a população e decretar um estado de vigilância. A desinformação relacionada à pandemia foi anteriormente associada à menor adesão às recomendações de saúde pública e aos efeitos adversos à saúde, e as evidências da atual pandemia indicam que a adesão às recomendações de saúde pública é totalmente partidária. Este estudo sugere que a polarização política e informativa facilitada por plataformas de mídia social como o Twitter pode ter consequências terríveis para a saúde pública.


### Abstract 
This study analyzes over 4000 tweets related to six misinformation topics about the COVID-19 pandemic: the use of hydroxychloroquine as treatment, the use of bleach as a preventative measure, Bill Gates intentionally causing the virus, the Chinese Communist Party intentionally causing the virus, and the Deep State causing the virus to ruin the economy and threaten President Trump’s reelection chances. Across 5 of 6 topics (excluding bleach), conservatives dominate the discourse on Twitter. Conservatives are also more likely than their liberal peers to believe in and push conspiracy theories that the Chinese Communist Party, Bill Gates, and the Deep State are working in conjunction to infect the population and enact a surveillance state. Pandemic related misinformation has previously been associated with decreased adherence to public health recommendations and adverse health effects and evidence from the current pandemic indicates that adherence to public health recommendations is starkly partisan. This study suggests that the political and informational polarization further facilitated by social media platforms such as Twitter may have dire consequences for public health.

### Fonte 
https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7604541/