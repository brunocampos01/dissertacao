Federated Learning

### Cenário
- data silos: são dados isolados e distribuídos. Dataset fragmentado
- privacidade: não pode mover os dados (regulamentação ou por o usuário não permitir) ou o custo não compensa mover esse dados p cloud
- ataque de alteração de aprendizagem, decoberta de dados

### Origin Data
- fog/Edge computing
  - celulares
  - cameras
  - smartwatch

### Motivation
- dataset fragmentado e isolado. Como fazer modelos q aproveitam esses dados sem transferir ?
- modelos atuais que compartilham dados, (transfer learning ??). Eficiencia e segurança ? 
- transferencia de dados para um lugar seguro. Como fica a relação de confiança ?

### Exemplo Real
- Predição de palavras, ex google keyboard (gboard)

### Federated Learning

- Treinar um modelo onde os dados estão e depois envia somente os parametros do modelo para a cloud
- No ambiente central se faz o concenso da modelagem
- computação federada: é uma aplicação exec em uma variedade de ambientes
- Embora cada cliente em tais sistemas contribua com dados e poder de processamento para computar um resultado pelo sistema ambém nos esforçamos para preservar a privacidade e o anonimato de cada cliente.

#### Training
step 1: servidor manda o modelo inicial para os participantes da federação 
step 2: os participantes começam a treinar o modelo com seus dados e em seguida mandam o modelo atualizado para o servidor central
step 3: o servidor central agrega (média pondera) todos e reenvia para os partifipantes


#### Inference

---

smart warehouse
- manutenção preventiva
- saber quanto tempo uma máquina esta funcionado
