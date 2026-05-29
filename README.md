# 🐝 Vigia da Colmeia

📌 Sobre o Projeto

O **Vigia da Colmeia** é um sistema inteligente de monitoramento de colmeias desenvolvido pela equipe do **CETI Professor Petronio Portela**, como projeto para o programa **Piauí Para o Mundo**.

O projeto tem como objetivo auxiliar apicultores no acompanhamento remoto da saúde das colmeias através da coleta e análise de dados ambientais, permitindo identificar situações de risco como:

* superaquecimento;
* estresse sonoro;
* possível abandono da colmeia;
* falhas de comunicação;
* colmeias offline.

A proposta busca unir:

* tecnologia;
* bioeconomia;
* sustentabilidade;
* Internet das Coisas (IoT);
* inteligência de monitoramento.

---

 🎯 Objetivo

Criar uma solução acessível e inteligente para monitoramento de colmeias em tempo real, auxiliando produtores rurais e apicultores na prevenção de perdas e no aumento da produtividade.

---

 🌎 Contexto

A apicultura possui grande importância econômica e ambiental no estado do Piauí, especialmente nas regiões semiáridas.

Muitos produtores ainda realizam o monitoramento das colmeias manualmente, o que dificulta:

* identificar problemas rapidamente;
* prevenir perdas;
* acompanhar o comportamento das abelhas em tempo real.

O Vigia da Colmeia surge como uma alternativa tecnológica de baixo custo para aproximar a inovação da realidade do campo.

---

 ⚙️ Funcionamento do Sistema

O sistema simula uma arquitetura semelhante a uma rede LoRa real.

 Fluxo do sistema:

```text
Sensores
↓
ESP32 Transmissor
↓
Comunicação LoRa Simulada
↓
ESP32 Gateway/Receptor
↓ HTTP
Servidor Flask
↓ SQLite
Dashboard Streamlit
```

---

# 🧠 Funcionalidades

 ✅ Monitoramento em tempo real

O sistema monitora:

* temperatura da colmeia;
* intensidade sonora;
* status da colmeia.

---

 ✅ Dashboard interativo

O dashboard exibe:

* colmeias ativas;
* colmeias offline;
* temperatura;
* intensidade sonora;
* alertas;
* histórico de leituras;
* gráficos em tempo real.

---

 ✅ Sistema de alertas inteligentes

O sistema detecta:

* superaquecimento;
* estresse sonoro;
* perda de comunicação;
* colmeias inativas.

---

 ✅ Simulação de múltiplas colmeias

O sistema permite monitorar várias colmeias simultaneamente.

---

 ✅ Atualização automática

Os dados do dashboard são atualizados automaticamente em tempo real.

---

 ✅ Banco de dados integrado

Todas as leituras são armazenadas em banco SQLite para:

* histórico;
* análise futura;
* geração de relatórios.

---

 ✅ Arquitetura IoT

O projeto utiliza uma estrutura inspirada em sistemas reais de:

* IoT;
* LoRa;
* gateways de comunicação;
* monitoramento remoto.

---

 🛠️ Tecnologias Utilizadas

 Linguagens

* Python

---

 Bibliotecas e Frameworks

 Backend

* Flask
* Requests

 Dashboard

* Streamlit
* Pandas

 Banco de Dados

* SQLite3

 Comunicação

* Socket TCP (simulação LoRa)

 Utilidades

* JSON
* Random
* Datetime
* Time

---

 📦 Dependências do Projeto

Instale todas as dependências com:

```bash
pip install flask
pip install streamlit
pip install pandas
pip install requests
```

---

# 🚀 Como Executar o Projeto

 1️⃣ Iniciar o servidor Flask

```bash
python server.py
```

---

 2️⃣ Iniciar o receptor/gateway

```bash
python receptor.py
```

---

 3️⃣ Iniciar o transmissor

```bash
python transmissor.py
```

---

 4️⃣ Iniciar o dashboard

```bash
python -m streamlit run dashboard.py
```

---

 🖥️ Dashboard

O dashboard pode ser acessado em:

```text
http://localhost:8501
```

---

 📊 Estrutura do Projeto

```text
PIAUI PARA O MUNDO
│
├── SERVIDOR
│   ├── server.py
│   ├── dashboard.py
│   ├── colmeia.db
│
├── TRANSMISSOR
│   ├── transmissor.py
│
├── RECEPTOR
│   ├── receptor.py
│
├── logo.jpg
│
└── README.md
```

---

 🔬 Futuras Implementações

* Integração com módulos LoRa reais;
* Aplicativo mobile;
* Integração com WhatsApp;
* Inteligência Artificial para análise comportamental;
* Sensores físicos reais;
* Painel web online;
* Hospedagem em nuvem.

---

 🐝 Impacto Esperado

O projeto busca:

* democratizar o acesso à tecnologia na apicultura;
* reduzir perdas em colmeias;
* fortalecer a bioeconomia local;
* incentivar a inovação no semiárido;
* aproximar jovens da tecnologia e sustentabilidade.

---

 👨‍💻 Equipe
 renan gomes, 
 joao vitor, 
 vitor hugo, 
 isabely, 
 lorrany,

 professor orientador:
 Rai Araujo

Projeto desenvolvido por estudantes do:
 CETI  Petronio Portela

para o programa:

 Piauí Para o Mundo

---

 📄 Licença

Projeto desenvolvido para fins educacionais e científicos.
